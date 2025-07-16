import streamlit as st
import plotly.express as px
import pandas as pd

# ========================================
# CONFIGURACIÓN INICIAL
# ========================================
st.set_page_config(
    page_title="CV Interactivo | Tu Nombre",
    page_icon="🚀",  # Emoji estándar
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
    # Foto de perfil usando solo Streamlit
    try:
        st.image("foto_perfil.jpg", width=200)  # Streamlit maneja la imagen directamente
    except:
        st.warning("⚠️ Sube tu foto como 'foto_perfil.jpg'")

    st.markdown("## 📌 Información de Contacto")
    st.write("📧 **Email:** tu@email.com")
    st.write("📱 **Teléfono:** +123456789")
    st.write("🌐 **LinkedIn:** [linkedin.com/tuperfil](https://linkedin.com)")
    st.write("💻 **GitHub:** [github.com/tuperfil](https://github.com)")

    # Botón de descarga (opcional)
    try:
        with open("CV.pdf", "rb") as file:
            st.download_button(
                label="⬇️ Descargar CV en PDF",
                data=file,
                file_name="CV_Interactivo.pdf",
                mime="application/pdf"
            )
    except:
        st.warning("PDF no encontrado")

# ========================================
# SECCIÓN PRINCIPAL
# ========================================
st.title("Tu Nombre Completo")
st.markdown("### 🎯 Desarrollador Full Stack | Especialista en Python")

# Divisor visual
st.markdown("---")

# ========================================
# COLUMNAS: PERFIL + HABILIDADES
# ========================================
col1, col2 = st.columns([2, 3])

with col1:
    st.markdown("### 🧑‍💻 Sobre Mí")
    st.write("""
    ¡Hola! Soy un apasionado desarrollador con experiencia en:
    - Desarrollo web con Python y JavaScript
    - Análisis de datos
    - Automatización de procesos
    - Machine Learning básico
    """)

with col2:
    st.markdown("### 🛠 Habilidades Técnicas")
    
    # Gráfico de habilidades (usando Plotly)
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
st.markdown("## 💼 Experiencia Profesional")

with st.expander("🚀 **Desarrollador Full Stack en Empresa XYZ (2020-Presente)**"):
    st.markdown("""
    - Lideré el desarrollo de una aplicación web con **Streamlit y React**
    - Optimicé consultas SQL reduciendo tiempos de respuesta en **40%**
    - Implementé pipelines de ETL para procesar datos diarios
    """)

with st.expander("📊 **Analista de Datos en ABC Corp (2018-2020)**"):
    st.markdown("""
    - Creé dashboards interactivos con **Plotly y Power BI**
    - Automaticé reportes mensuales usando **Python y Pandas**
    """)

# ========================================
# PROYECTOS DESTACADOS
# ========================================
st.markdown("---")
st.markdown("## 🏆 Proyectos Destacados")

proj_col1, proj_col2 = st.columns(2)

with proj_col1:
    with st.expander("🤖 Chatbot con IA"):
        st.markdown("""
        - Chatbot para servicio al cliente usando **GPT-3**
        - Integración con Slack y WhatsApp
        - [Ver código en GitHub](https://github.com)
        """)
        st.image("https://via.placeholder.com/300x150", caption="Captura del proyecto")

with proj_col2:
    with st.expander("📈 Análisis de Datos en Tiempo Real"):
        st.markdown("""
        - Sistema de monitoreo con **Streamlit y AWS**
        - Visualización interactiva de datos financieros
        """)

# ========================================
# FORMULARIO DE CONTACTO
# ========================================
st.markdown("---")
st.markdown("## 📩 Contáctame")

with st.form(key='contact_form'):
    name = st.text_input("Nombre completo")
    email = st.text_input("Email")
    message = st.text_area("Mensaje")
    submit_button = st.form_submit_button("Enviar mensaje")
    
    if submit_button:
        st.success(f"¡Gracias {name}! Tu mensaje ha sido enviado (simulación).")

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