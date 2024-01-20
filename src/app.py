import streamlit as st

def buscar_jugador_similar(nombre, posicion, edad, habilidad):
    nombres_similares = ["Messi", "Ronaldo", "Neymar", "Mbappé"]
    return nombres_similares

def main():
    # Personalización de colores con HTML/CSS
    st.markdown("""
        <style>
        .main {background-color: #F5F5F5;}
        .reportview-container .markdown-text-container {color: #4F4F4F;}
        </style>
        """, unsafe_allow_html=True)

    st.title("Buscador de Jugadores de Fútbol Similares")

    # Mensaje de bienvenida
    st.markdown("### Bienvenido al buscador de jugadores de fútbol. Encuentra jugadores similares basados en tus criterios.")

    nombre = st.text_input("Nombre del Jugador:")
    posicion = st.selectbox("Posición:", ["Delantero", "Centrocampista", "Defensa", "Portero"])
    edad = st.slider("Edad:", min_value=18, max_value=40, value=25)
    habilidad = st.slider("Habilidad (1-100):", min_value=1, max_value=100, value=50)

    if st.button("Buscar Jugador Similar"):
        jugadores_similares = buscar_jugador_similar(nombre, posicion, edad, habilidad)
        if jugadores_similares:
            st.success(f"Jugadores similares a {nombre}: {', '.join(jugadores_similares)}")
        else:
            st.warning("No se encontraron jugadores similares.")

if __name__ == "__main__":
    main()
