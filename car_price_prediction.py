import streamlit as st
import pickle
import numpy as np

# Charger le modèle pickle
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))

# Fonction pour effectuer la prédiction
def predict_price(present_price, kms_driven, fuel_type, seller_type, transmission, number_of_year):
    # Mapper le type de carburant
    fuel_type_mapping = {'Petrol': 2, 'Diesel': 1, 'CNG': 0}
    fuel_type = fuel_type_mapping[fuel_type]

    # Mapper le type de vendeur
    seller_type_mapping = {'Individual': 1, 'Dealer': 0}
    seller_type = seller_type_mapping[seller_type]

    # Mapper le type de transmission
    transmission_mapping = {'Mannual': 1, 'Automatic': 0}
    transmission = transmission_mapping[transmission]

    # Effectuer la prédiction
    prediction = model.predict([[present_price, np.log(kms_driven), fuel_type, seller_type, transmission, number_of_year]])
    return round(prediction[0], 2)

# Interface utilisateur Streamlit
def main():
    st.title("Price Prediction App")

    # Collecter les entrées utilisateur
    present_price = st.number_input("Prix en showroom ", min_value=0.0)
    kms_driven = st.number_input("Kilomètres parcourus", min_value=0,max_value=500000)
    fuel_type = st.selectbox("Type de carburant", ['Petrol', 'Diesel', 'CNG'])
    seller_type = st.selectbox("Type de vendeur", ['Individual', 'Dealer'])
    transmission = st.selectbox("Type de transmission", ['Mannual', 'Automatic'])
    number_of_year = st.slider("Nombre d'années", 0, 50, 5)

    # Bouton de prédiction
    if st.button("Calculer le prix de vente"):
        prediction = predict_price(present_price, kms_driven, fuel_type, seller_type, transmission, number_of_year)
        st.success(f"Selon notre modèle prédictif, vous pouvez estimer la vente de votre voiture à {prediction} .")

if __name__ == "__main__":
    main()