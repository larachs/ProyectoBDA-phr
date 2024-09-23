import streamlit as st

st.title("🎈SummitSphere, gestionamos tu evento!")

########SUBIR ARCHIVOS 
    # Descripción
st.write('Por favor, sube tus archivos.')

    # Botón para subir archivos
archivos_subidos = st.file_uploader("Selecciona archivos", accept_multiple_files=True)

    # Si se suben archivos, mostrar detalles
if archivos_subidos:
    st.write(f"Se han subido {len(archivos_subidos)} archivos.")
    for archivo in archivos_subidos:
        st.write(f"Nombre: {archivo.name}, Tipo: {archivo.type}, Tamaño: {archivo.size} bytes")

##### SUPUESTA CONEXION
from neo4j import GraphDatabase
import logging

logging.basicConfig(level=logging.INFO)

URI = "bolt://localhost:7687"
AUTH = ("neo4j", "PabloHilaRache")

try:
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        print("Connection established successfully.")
except Exception as e:
    print(f"Error: {e}")
