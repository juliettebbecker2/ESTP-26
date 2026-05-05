#conda activate ESTP
# sreamlit run TP_streamlit.py

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

st.write("Hello, Streamlit !")

#Title and subtitle
st.title("TP ESTP jour 5 - Streamlit")
st.subheader("This is a subheader")
st.markdown("This is a markdown text. You can use **bold** and *italic*.")

#Utilisation de la sidebar
st.sidebar.header("Options")
nom = st.sidebar.text_input("Entrez votre nom")
if nom:
    st.sidebar.success(f"Bonjour, {nom}!")

#Choix dans une liste déroulante
graph_type = st.sidebar.selectbox("Type de graphique",["ligne","barres","aucun"])

#Chargement de fichiers
uploaded_file = st.file_uploader("Choisissez un fichier CSV", type = "csv")
if uploaded_file is not None:
    st.write("Fichier chargé avec succès!")
    df = pd.read_csv(uploaded_file)   #lecture du fichier CSV par pandas
    st.dataframe(df.head())          #affichage du dataframe dans Streamlit

    #Graphique
    if graph_type !="aucun":
        col_numeric = df.select_dtypes(include = 'number').columns.tolist()
        col = st.selectbox("Choisissez une colonne numérique", col_numeric)
        if graph_type == "ligne":
            st.line_chart(df)
        elif graph_type == "barres":
            st.bar_chart(df)

#slider pour sélectionner une valeur
age = st.slider("Sélectionner votre âge", 0, 100,5)
st.write(f"Votre âge est : {age}")


#checkbox
if st.checkbox("Afficher un message secret"):
    st.write("Voici le message secret : Streamlit est génial !")

#Spinner pour lancer une tâche en cours
if st.button("Lancer une tâche longue"):
    with st.spinner("Traitement en cours..."):
        time.sleep(5)
    st.success("Tâche terminée !")

