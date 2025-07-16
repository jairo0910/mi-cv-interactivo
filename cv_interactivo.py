import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd

# ========================================
# CONFIGURACION INICIAL
# ========================================
st.set_page_config(
    page_title="CV Interactivo | Tu Nombre",
    page_icon="??",
    layout="wide"
)

# ========================================
# FUNCIONES REUTILIZABLES
# ========================================
def skill_bar(skill_name, level):
    st.markdown(f"**{skill_name}**")
    st.progress(level)

# ========================================
# SIDEBAR (CONTACTO)
# ========================================
with st.sidebar:
    # Foto de perfil (reemplaza con tu imagen)
    try:
        image = Image.open("foto_perfil.jpg")
        st.image(image, width=200)
    except:
        st.warning("?? Sube tu foto como 'foto_perfil.jpg'")

    st.markdown("## ?? Informacion de Contacto")
    st.write("?? **Email:** tu@email.com")
    st.write("?? **Telefono:** +123456789")
    st.write("?? **LinkedIn:** [linkedin.com/tuperfil](https://linkedin.com)")
    st.write("?? **GitHub:** [github.com/tuperfil](https://github.com)")

    # Boton de descarga (opcional)
    with open("CV.pdf", "rb") as file:
        st.download_button(
            label="?? Descargar CV en PDF",
            data=file,
            file_name="CV_Interactivo.pdf",
            mime="application/pdf"
        )

# ========================================
# SECCION PRINCIPAL
# ========================================
st.title("Tu Nombre Completo")
st.markdown("### ?? Desarrollador Full Stack | Especialista en Python")

# Divisor visual
st.markdown("---")

# ========================================
# COLUMNAS: PERFIL + HABILIDADES
# ========================================
col1, col2 = st.columns([2, 3])

with col1:
    st.markdown("### ????? Sobre Mi")
    st.write("""
    !Hola! Soy un apasionado desarrollador con experiencia en:
    - Desarrollo web con Python y JavaScript
    - Analisis de datos
    - Automatizacion de procesos
    - Machine Learning basico
    """)

with col2:
    st.markdown("### ?? Habilidades Tecnicas")
    
    # Grafico de habilidades (usando Plotly)
    skills_data = {
        "Habilidad": ["Python", "SQL", "Streamlit", "JavaScript", "Git"],
        "Nivel": [90, 85, 80, 75, 70]
    }
    fig = px.bar(
        skills_data, 
        x="Habilidad", 
        y="Nivel",
        color="Habilidad",
        title="Nivel de Habilidades"
    )
    st.plotly_chart(fig, use_container_width=True)

# ========================================
# EXPERIENCIA LABORAL (CON EXPANDERS)
# ========================================
st.markdown("---")
st.markdown("## ?? Experiencia Profesional")

with st.expander("?? **Desarrollador Full Stack en Empresa XYZ (2020-Presente)**"):
    st.markdown("""
    - Lidere el desarrollo de una aplicacion web con **Streamlit y React**.
    - Optimice consultas SQL reduciendo tiempos de respuesta en **40%**.
    - Implemente pipelines de ETL para procesar datos diarios.
    """)

with st.expander("?? **Analista de Datos en ABC Corp (2018-2020)**"):
    st.markdown("""
    - Cree dashboards interactivos con **Plotly y Power BI**.
    - Automatice reportes mensuales usando **Python y Pandas**.
    """)

# ========================================
# PROYECTOS DESTACADOS
# ========================================
st.markdown("---")
st.markdown("## ?? Proyectos Destacados")

proj_col1, proj_col2 = st.columns(2)

with proj_col1:
    with st.expander("?? Chatbot con IA"):
        st.markdown("""
        - Chatbot para servicio al cliente usando **GPT-3**.
        - Integracion con Slack y WhatsApp.
        - [Ver codigo en GitHub](https://github.com)
        """)
        st.image("https://via.placeholder.com/300x150", caption="Captura del proyecto")

with proj_col2:
    with st.expander("?? Analisis de Datos en Tiempo Real"):
        st.markdown("""
        - Sistema de monitoreo con **Streamlit y AWS**.
        - Visualizacion interactiva de datos financieros.
        """)

# ========================================
# FORMULARIO DE CONTACTO
# ========================================
st.markdown("---")
st.markdown("## ?? Contactame")

with st.form(key='contact_form'):
    name = st.text_input("Nombre completo")
    email = st.text_input("Email")
    message = st.text_area("Mensaje")
    submit_button = st.form_submit_button("Enviar mensaje")
    
    if submit_button:
        st.success(f"!Gracias {name}! Tu mensaje ha sido enviado (simulacion).")

# ========================================
# ESTILO PERSONALIZADO (CSS)
# ========================================
st.markdown("""
<style>
    .stProgress > div > div > div > div {
        background-color: #2a3f5f;
    }
    .st-bb {
        background-color: #f0f2f6;
    }
    .st-at {
        background-color: #ffffff;
    }
    div[data-testid="stExpander"] div[role="button"] p {
        font-size: 18px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)