import streamlit as st

st.title("🎈SummitSphere, gestionamos tu evento!")


## Conexion con NEO4J
from neo4j import GraphDatabase

# Conexión con Neo4j
uri = "bolt://localhost:7687"  # O reemplázalo por el URI que obtuviste
user = "larachs"  # Tu usuario
password = "PROYECTO-BDA"  # La contraseña de tu DBMS
driver = GraphDatabase.driver(uri, auth=(user, password))

# Función para cargar los archivos a Neo4j
def guardar_archivo_en_neo4j(nombre, tipo, tamano, contenido):
    with driver.session() as session:
        session.run(
            """
            CREATE (a:Archivo {nombre: $nombre, tipo: $tipo, tamano: $tamano, contenido: $contenido})
            """,
            nombre=nombre, tipo=tipo, tamano=tamano, contenido=contenido
        )

# Configurar la aplicación en Streamlit
st.title("Subir Archivos a Neo4j")

# Subir múltiples archivos
archivos_subidos = st.file_uploader("Selecciona archivos", accept_multiple_files=True)

if archivos_subidos:
    for archivo in archivos_subidos:
        # Convertir el archivo en bytes
        contenido = archivo.read()
        
        # Guardar metadatos e información del archivo en Neo4j
        guardar_archivo_en_neo4j(archivo.name, archivo.type, archivo.size, contenido)
        
        st.success(f"Archivo {archivo.name} subido y guardado en Neo4j.")

# Cerrar conexión cuando la app termina
driver.close()