import streamlit as st

st.title("🎈SummitSphere, gestionamos tu evento!")


# Descripción
st.write('Por favor, sube tus archivos, para gestionar de la mejor manera tu evento')

# Botón para subir archivos
archivos_subidos = st.file_uploader("Seleccionar archivos", accept_multiple_files=True)

# Si se suben archivos, mostrar detalles
if archivos_subidos:
    st.write(f"Se han subido {len(archivos_subidos)} archivos.")
    for archivo in archivos_subidos:
        st.write(f"Nombre: {archivo.name}, Tipo: {archivo.type}, Tamaño: {archivo.size} bytes")
