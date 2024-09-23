import streamlit as st
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

st.title("🎈SummitSphere, gestionamos tu evento!")



URI = "bolt://localhost:7687" 
AUTH = ("neo4j", "PabloHilaRache")  # Tus credenciales

try:
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        print("Conexión exitosa a Neo4j.")
        st.write("Conexión exitosa a Neo4j.")
except Exception as e:
    print(f"Error al conectarse a Neo4j: {e}")
    st.write(f"Error al conectarse a Neo4j: {e}")
    st.write("ME CAGO EN TODO")
