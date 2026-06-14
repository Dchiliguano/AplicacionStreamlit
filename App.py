import streamlit as st
import pandas as pd
import plotly.express as px


st.title('Aplicación para Oil & Gas')
st.sidebar.title ('Parametros')
st.sidebar.image('Python.png',width=300)
Modulo=st.sidebar.selectbox('Seleccione un modulo',['Modulo 1', 'Modulo 2','Modulo 3'])
if Modulo=='Modulo 1':
    st.write('Estas en el modulo 1')
    ge = st.number_input('Ingrese la gravedad especifica',min_value=0.1,max_value=1.0,value=0.7 )
    api=(141.5/ge-131.5)
    st.write('El grado API es:',api)
elif Modulo=='Modulo 2':
    columna1,columna2 = st.columns(2)
    with columna1:
        st.write('Estas en el modulo 2')
        data=pd.read_excel('Data/Resultados.xlsx')  
        st.write(data)
    with columna2:
        figura=px.line(data_frame=data,x='Mes', y='Produccion Mensual')
        st.write (figura)
else :
    st.write('Estas en el modulo 3')
    archivo = st.file_uploader('Sube tu archivo csv o excel',type=['csv','xlsx'])
    if archivo is not None: 
        if archivo.name.endswith('.csv'):
            data_cargado=pd.read_csv(archivo)
        elif archivo.name.endswith('.xlsx'):
            data_cargado=pd.read_excel(archivo)
        else :
            st.write('Formato no admitido')
        st.write(data_cargado)
    else : 
        st.write ('Por favor sube tu archivo')