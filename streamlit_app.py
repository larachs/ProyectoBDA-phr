import streamlit as st

st.title("🎈SummitSphere, gestionamos tu evento!")



def conexionBDA(): 
    URI="bolt://localhost:7687"
    NEO4J_USER="neo4j"
    NEO4J_PASSWORD="PabloHilaRache"

    # Descripción
    st.write('Por favor, sube tus archivos.')

    # Botón para subir archivos
    archivos_subidos = st.file_uploader("Selecciona archivos", accept_multiple_files=True)

    # Si se suben archivos, mostrar detalles
    if archivos_subidos:
        st.write(f"Se han subido {len(archivos_subidos)} archivos.")
        for archivo in archivos_subidos:
            st.write(f"Nombre: {archivo.name}, Tipo: {archivo.type}, Tamaño: {archivo.size} bytes")

    import dotenv
    import os
    from neo4j import GraphDatabase

    load_status = dotenv.load_dotenv("Neo4j-a0a2fa1d-Created-2023-11-06.txt")
    if load_status is False:
        raise RuntimeError('Environment variables not loaded.')

    URI = os.getenv("bolt://localhost:7687")
    AUTH = (os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))

    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        print("Connection established.")