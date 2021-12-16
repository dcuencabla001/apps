import streamlit as st
import pandas as pd

st.image(image='logoEroski.png')

st.title('Carga Diaria Plataforma')
st.header('Subir el archivo en formato CSV con la carga diaria de la plataforma')

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    #df.to_csv('out.csv')
    st.header("archivo guardado correctamente")
    #st.write("archivo guardado correctamente")