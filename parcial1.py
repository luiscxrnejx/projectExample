import pandas as pd 
import streamlit as st 
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Reporte ISIC PROM')
st.header('Reporte Parcial 1')
st. subheader('Ingenieria en sistemas computacionales')

excel_file = 'DatosFinalesP1.xlsx'
sheet_namee = 'Datos Limpios'

df = pd.read_excel('C:/Users/luis-/Dash Python/DatosFinalesP1.xlsx', sheet_name='Datos Limpios')

st.dataframe(df)