import pandas as pd
import streamlit as st
import plotly.express as px


# Create app
df = pd.read_csv(
    '/Users/guita/Documents/TripleTen/Sprint7_WebApp/vehicles_us.csv')

st.header("Proyecto Sprint 7 - Aplicación Web")

st.subheader("Análisis de datos de ventas de vehículos")
st.write("Esta aplicación permite filtrar y visualizar datos de ventas de vehículos en Estados Unidos por marca y precio. "
         "Dichos datos se verán reflejdos en la siguiente tabla presentandose de menor a mayor precio.")
col1, col2 = st.columns(2)
with col1:
    model = st.selectbox(
        "Marcas de autos:",
        ('Acura', 'BMW', 'Buick', 'Cadillac', 'Chevrolet', 'Chrysler',
         'Dodge', 'Ford', 'GMC', 'Honda', 'Hyundai', 'Jeep', 'Kia',
         'Mercedes-Benz', 'Nissan', 'Ram', 'Subaru', 'Toyota', 'Volkswagen'),
        index=None,
        placeholder="Selecciona la marca....",)

with col2:
    price_x = st.slider('Filtro por precio:', 5, 100,
                        df['price'].max())  # Widget de slicer

# Presentación de la tabla de acuerdo al slicer de precios
if model == None:
    st.write((df[df['price'] <= price_x]).sort_values(
        by='price', ascending=True))
else:
    st.write(df[(df['price'] <= price_x) & (
        df['model'].str.contains(model.lower()))].sort_values(by='price', ascending=True))

st.write("Esta aplicación también permite visualizar gráficos interactivos de los datos de ventas de vehículos por combustible.")

col3, col4 = st.columns(2)
with col3:
    st.write("Selecciona el tipo de combustible:")
    gas = st.checkbox("gasoline")
    diesel = st.checkbox("diesel")

with col4:
    hybrid = st.checkbox("hybrid")
    other = st.checkbox("other")
    electric = st.checkbox("electric")

# Crear lista de combustibles seleccionados
selected_fuels = []
if gas:
    selected_fuels.append("gas")
if diesel:
    selected_fuels.append("diesel")
if hybrid:
    selected_fuels.append("hybrid")
if other:
    selected_fuels.append("other")
if electric:
    selected_fuels.append("electric")

# Filtrar DataFrame solo si hay seleccionados
if selected_fuels:
    df_filtered = df[df['fuel'].isin(selected_fuels)]
else:
    df_filtered = df.copy()  # si no hay seleccionados, mostramos todo

# crear un hisstograma
fig = px.histogram(df_filtered, x="price",
                   nbins=60,
                   title="Histograma de precios de vehículos")
# mostrar un gráfico Plotly interactivo
st.plotly_chart(fig, use_container_width=True)

st.write("Correlación entre marcas de vehículos y precios")

scatter_button = st.button('Construir gráfico de dispersión')  # crear un botón
if scatter_button:  # al hacer clic en el

    # vehicle_condition = df.pivot_table(index='condition', aggfunc='count')['price'].reset_index(name='condition_quantity').sort_values('condition_quantity')
    # crear un gráfico de dispersión
    fig_scatter = px.scatter(df, x="price", y="condition",
                             title="Gráfico de dispersión de condiciones de vehículos",
                             labels={"condition": "Condición del vehículo", "condition_quantity": "Cantidad de vehículos"})
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)
