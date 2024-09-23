import streamlit as st
from neo4j import GraphDatabase

st.title("🎈SummitSphere, gestionamos tu evento!")


# Configuración de la conexión a Neo4j
uri = "bolt://localhost:7687"  # Utiliza el puerto Bolt que te proporcionaron
driver = GraphDatabase.driver(uri, auth=("neo4j", "PabloHilaRache"))  # Reemplaza "password" con tu contraseña

# Función para guardar los archivos en Neo4j
def guardar_archivos_en_neo4j(archivos_subidos):
    # Conectar a Neo4j
    with driver:
        with driver.session() as session:
            for archivo in archivos_subidos:
                # Crear un nodo para cada archivo
                session.write_transaction(
                    crear_nodo_archivo,
                    archivo.name,
                    archivo.type,
                    archivo.size
                )
                st.write(f"Archivo '{archivo.name}' guardado en la base de datos.")

def crear_nodo_archivo(tx, nombre, tipo, tamaño):
    # Crear un nodo con las propiedades del archivo
    tx.run(
        """
        CREATE (a:Archivo {nombre: $nombre, tipo: $tipo, tamaño: $tamaño})
        """,
        nombre=nombre, tipo=tipo, tamaño=tamaño
    )

# Descripción
st.write('Por favor, sube tus archivos para guardarlos en Neo4j')

# Botón para subir archivos
archivos_subidos = st.file_uploader("Selecciona archivos", accept_multiple_files=True)

# Botón para ejecutar la carga a Neo4j
if st.button("Guardar en Neo4j"):
    if archivos_subidos:
        guardar_archivos_en_neo4j(archivos_subidos)
    else:
        st.warning("No se han subido archivos aún.")

