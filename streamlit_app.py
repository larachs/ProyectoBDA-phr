import streamlit as st

st.title("🎈SummitSphere, gestionamos tu evento!")


##### SUPUESTA CONEXION
from neo4j import GraphDatabase

# Configuración de la conexión a Neo4j
uri = "bolt://localhost:7687"  # Utiliza el puerto Bolt que te proporcionaron
driver = GraphDatabase.driver(uri, auth=("neo4j", "PabloHilaRache"))  # Reemplaza "password" con tu contraseña


