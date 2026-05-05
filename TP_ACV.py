#L'objectif de ce TP est d'analyser la base de données E+C-
#D'analyser les données et de visualiser les résultats à l'aide de graphiques interactifs.
#Utiliser une application Streamlit pour présenter les résultats de manière interactive.    

#Instrutions pour exécuter l'application depuis VS CODE:
#1. Ouvrir le terminal intégré de VS Code (Ctrl + `)    
#2. Activer l'environnement conda (conda activate ESTP)
#3. Lancer l'application Streamlit (streamlit run TP_ACV.py)

#Step1:importation des bibliothèques nécessaires



import streamlit as st
import numpy as np
import pandas as pd

#Step2:Présentation de l'application
st.title("Analyse de la base de données E+C-")
st.write("Cette application permet d'analyser la base de données E+C- et de visualiser les résultats à l'aide de graphiques interactifs.")  

#Step3:Chargement de la base de données
uploaded_file = st.file_uploader("Téléversez un fichier Excel", type=["xlsx", "xls"])
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, header=[0, 1])
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.droplevel(0)
    st.write("Fichier chargé avec succès.")
    st.dataframe(df.head(5))
else:
    st.info("Veuillez téléverser un fichier Excel pour afficher les 5 premières lignes.")

# Step 4: Plotly scatter plot
if uploaded_file is not None:
    st.subheader("Graphique de dispersion (Scatter Plot)")
    y_column = st.selectbox("Sélectionnez la colonne pour l'axe Y", df.columns)
    fig = px.scatter(df, y=y_column, title=f"Scatter Plot de la colonne '{y_column}'")
    st.plotly_chart(fig, use_container_width=True)