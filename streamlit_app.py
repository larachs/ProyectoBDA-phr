import streamlit as st
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

st.title("🎈SummitSphere, gestionamos tu evento!")


# Configuración de la conexión a Neo4jj
uri = "bolt://127.0.0.1:7687:7687"  # Utiliza el puerto Bolt que te proporcionaron
driver = GraphDatabase.driver(uri, auth=("neo4j", "PabloHilaRache"))  # Reemplaza "password" con tu contraseña



def guardar_archivos_en_neo4j(archivos_subidos):
    try:
        with driver.session() as session:
            for archivo in archivos_subidos:
                session.write_transaction(
                    crear_nodo_archivo,
                    archivo.name,
                    archivo.type,
                    archivo.size
                )
                st.write(f"Archivo '{archivo.name}' guardado en la base de datos.")
    except ServiceUnavailable as e:
        st.error("Error al conectarse a Neo4j: " + str(e))
    except Exception as e:
        st.error("Ocurrió un error: " + str(e))


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

driver.close()