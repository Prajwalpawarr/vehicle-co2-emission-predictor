
from flask import Flask, render_template, request
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import Ridge
import pickle

app = Flask(__name__)

# Load and preprocess the dataset
df=pd.read_csv(r'D:\Data Science ExcelR\Project\co2data.csv')
df[['make', 'model', 'vehicle_class']] = df[['make', 'model', 'vehicle_class']].applymap(lambda x: x.lower())
df_final = df[["engine_size", "transmission", 'fuel_type', "fuel_consumption_comb(mpg)", 'co2_emissions']]
df_final = df_final.drop_duplicates()

# Preprocess features and target
X = df_final[["engine_size", "transmission", 'fuel_type', "fuel_consumption_comb(mpg)"]]
y = df_final["co2_emissions"]

# One-hot encoding categorical variables
X = pd.get_dummies(X, columns=['fuel_type'])

# Label encode 'transmission' feature
le = LabelEncoder()
X['transmission'] = le.fit_transform(X['transmission'])

# Standardize features
SS = StandardScaler()
X_standardized = SS.fit_transform(X)

# Model training
ridge_reg = Ridge(alpha=100)
ridge_reg.fit(X_standardized, y)

# Save the model and preprocessing objects
with open('model.pkl', 'wb') as model_file:
    pickle.dump((ridge_reg, SS, le), model_file)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')


# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    engine_size = float(request.form['engine_size'])
    transmission = request.form['transmission']
    fuel_consumption_comb_mpg = int(request.form['fuel_consumption_comb_mpg'])
    fuel_type = request.form['fuel_type']

    # Preprocess user input
    user_input = pd.DataFrame([[engine_size, transmission, fuel_consumption_comb_mpg, fuel_type]],
                              columns=['engine_size', 'transmission', 'fuel_consumption_comb(mpg)', 'fuel_type'])
    user_input = pd.get_dummies(user_input, columns=['fuel_type'])
    print(user_input,user_input.shape)


    # Load the model and preprocessing objects
    with open('model.pkl', 'rb') as model_file:
        model, SS, le = pickle.load(model_file)

    # Label encode 'transmission' feature
    user_input['transmission'] = le.transform(user_input['transmission'])

    # Reorder columns to match model input
    user_input = user_input.reindex(columns=X.columns, fill_value=0)

    # Standardize user input
    user_input_standardized = SS.transform(user_input)
    print(user_input_standardized,user_input_standardized.shape)

    # Make prediction using the trained model
    prediction = model.predict(user_input_standardized)[0]

    # Round the prediction to two decimal places
    rounded_prediction = round(prediction, 2)

    # Render result template with rounded prediction
    return render_template('result.html', prediction=rounded_prediction)



if __name__ == '__main__':
    app.run(debug=True)
