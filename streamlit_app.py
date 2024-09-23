import streamlit as st

st.title("🎈SummitSphere, gestionamos tu evento!")


import os
from neo4j import GraphDatabase
import dotenv



# Cargar las variables de entorno desde un archivo .env
dotenv.load_dotenv("Neo4j-a0a2fa1d-Created-2023-11-06.txt")

# Obtener la URI y las credenciales de Neo4j desde las variables de entorno
URI = os.getenv("bolt://localhost:7687")
USERNAME = os.getenv("neo4j")
PASSWORD = os.getenv("PabloHilaRache")

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
