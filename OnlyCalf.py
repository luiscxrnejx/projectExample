import pandas as pd 
import streamlit as st 
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='OnlyCalf')
st.header('ITSOEH')
st.subheader('SEMESTRE  ENERO - JUNIO 2021, INDICADORES DE NIVEL DE DESEMPEÑO ,PRIMER PARCIAL, INGENIERÍA  EN  SISTEMAS  COMPUTACIONALES, INGENIERÍA  EN  SISTEMAS  COMPUTACIONALES')

excel_file = st.file_uploader('Cargar archivo de calificacion del primer parcial',type="xlsx")

analysis = st.sidebar.selectbox ('Seleccionar una opción', ['Reporte por parcial', 'Reporte Final', 'Reporte Final Idionio','Fuente final idonea'])

df = pd.read_excel(excel_file)
st.dataframe(df)


