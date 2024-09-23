import streamlit as st
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

st.title("🎈SummitSphere, gestionamos tu evento!")


# Configuración de la conexión a Neo4jj
uri = "bolt://localhost:7687"  # Utiliza el puerto Bolt que te proporcionaron
driver = GraphDatabase.driver(uri, auth=("neo4j", "PabloHilaRache"))  # Reemplaza "password" con tu contraseña



# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
URI = "<bolt://localhost:7687>"
AUTH = ("<neo4j>", "<PabloHilaRache>")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()
    print("Connection established.")
    st.write("Connection established")