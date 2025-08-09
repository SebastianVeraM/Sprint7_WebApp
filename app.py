import pandas as pd
import streamlit as st
import plotly.express as px


# Create app
df = pd.read_csv(
    '/Users/guita/Documents/TripleTen/Sprint7_WebApp/vehicles_us.csv')

st.header("Proyecto Sprint 7 - Aplicación Web")


car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.button('Construir histograma')  # crear un botón
graph_button = st.button('Construir gráfico de dispersión')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

    hist_button = st.button('Construir histograma')  # crear un botón

if graph_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
