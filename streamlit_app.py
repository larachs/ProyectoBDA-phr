import streamlit as st

st.title("🎈SummitSphere, gestionamos tu evento!")




import os
from neo4j import GraphDatabase

# Conexión a Neo4j sin Aura
URI = "bolt://localhost:7687"  # Cambia esto si es remoto, ej: "bolt://<ip-remota>:7687"
USERNAME = "neo4j"  # Reemplaza con tu usuario
PASSWORD = "PabloHilaRache"  # Reemplaza con tu contraseña

# Función para conectar y verificar la conexión con Neo4j
def conectar_neo4j(uri, user, password):
    try:
        driver = GraphDatabase.driver(uri, auth=(user, password))
        driver.verify_connectivity()  # Verifica la conectividad
        st.success("Conexión a Neo4j establecida.")
        return driver
    except Exception as e:
        st.error(f"Error al conectar con Neo4j: {e}")
        return None

# Conectar a Neo4j
driver = conectar_neo4j(URI, USERNAME, PASSWORD)

# Cerrar la conexión cuando ya no sea necesaria
if driver:
    with driver.session() as session:
        st.write("Ejecutando consultas en Neo4j...")
        # Aquí puedes agregar tus consultas a la base de datos usando el session
        # Ejemplo: session.run("MATCH (n) RETURN n")
    driver.close()  # Cerrar el driver
