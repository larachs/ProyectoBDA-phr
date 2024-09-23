import streamlit as st

st.title("🎈SummitSphere, gestionamos tu evento!")


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
