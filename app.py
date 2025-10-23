import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir histograma')

print("App de Sprint 7: Roberto Pinto")

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig_1 = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_1, use_container_width=True)

disp_button = st.button('Construir un gráfico de dispersión')

if disp_button:
    st.write("Creación de un gráfico de dispersión entre precio y kilometraje")
    fig_2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_2, use_container_width=True)
