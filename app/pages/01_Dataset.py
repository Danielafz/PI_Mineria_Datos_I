import streamlit as st
import pandas as pd

# ── CONFIGURACIÓN ─────────────────────────────────────────────────────────
st.set_page_config(page_title="Dataset", page_icon="📂", layout="wide")

# ── CSS PERSONALIZADO ─────────────────────────────────────────────────────
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
    * { font-family: 'Poppins', sans-serif !important; }
    .stApp { background-color: #F8F9FA; }
    h1 { color: #1E6FBA; font-weight: 700; }
    h2 { color: #1A1A2E; border-left: 5px solid #1E6FBA; padding-left: 10px; font-weight: 600; }
    h3 { color: #1E6FBA; font-weight: 600; }
    [data-testid="stSidebar"] { background-color: #1A1A2E; }
    [data-testid="stSidebar"] * { color: white !important; font-family: 'Poppins', sans-serif !important; }
    [data-testid="metric-container"] {
        background-color: white;
        border: 1px solid #1E6FBA;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    }
    .info-card {
        background: white;
        border-radius: 12px;
        padding: 20px 25px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.08);
        border-top: 4px solid #1E6FBA;
        margin-bottom: 15px;
    }
    .info-card p { margin: 8px 0; font-size: 0.95rem; }
    </style>
""", unsafe_allow_html=True)

# ── TÍTULO ────────────────────────────────────────────────────────────────
st.title("📂 Dataset")
st.markdown("Descripción general, calidad y transformaciones aplicadas.")

st.divider()

# ── CARGA DEL DATASET ─────────────────────────────────────────────────────
@st.cache_data
def cargar_datos():
    url = "https://raw.githubusercontent.com/Danielafz/PI_Mineria_Datos_I/main/data/processed/streaming_users_clean.csv"
    return pd.read_csv(url)

df = cargar_datos()

# ── DESCRIPCIÓN GENERAL ───────────────────────────────────────────────────
st.markdown("### 📌 Descripción general")
st.markdown("""
<div class="info-card">
    <p>El dataset contiene registros de usuarios de una plataforma de streaming.
    Cada fila representa un usuario con información sobre su plan de suscripción,
    consumo de contenido, preferencias de género, país de origen y actividad reciente.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
col1.metric("🗂️ Filas (dataset limpio)", "7.003")
col2.metric("📊 Columnas", "8")
col3.metric("✅ Retención de datos", "85.8%")

st.divider()

# ── CALIDAD INICIAL ───────────────────────────────────────────────────────
st.markdown("### 🔍 Calidad inicial del dataset")

col1, col2, col3, col4 = st.columns(4)
col1.metric("📋 Filas originales", "8.160")
col2.metric("⚠️ Valores faltantes", "753")
col3.metric("🔁 Duplicados", "126")
col4.metric("❌ Valores imposibles", "Detectados")

st.divider()

# ── TRANSFORMACIONES ──────────────────────────────────────────────────────
st.markdown("### 🔧 Transformaciones aplicadas")
st.markdown("""
<div class="info-card">
    <p>🗑️ <b>Eliminación de duplicados:</b> se eliminaron 126 registros duplicados.</p>
    <p>🔤 <b>Normalización de categóricas:</b> se unificaron mayúsculas/minúsculas y espacios
    en subscription_plan, country y favorite_genre.</p>
    <p>📥 <b>Imputación de valores faltantes:</b> se imputaron con mediana para variables
    numéricas y con moda para variables categóricas.</p>
    <p>🚫 <b>Eliminación de valores imposibles:</b> se eliminaron registros con valores
    fuera del rango lógico en variables numéricas.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── VISTA PREVIA ──────────────────────────────────────────────────────────
st.markdown("### 👀 Vista previa del dataset limpio")
st.dataframe(df.head(10), use_container_width=True)

st.markdown("### 📊 Estadísticas descriptivas")
st.dataframe(df.describe().round(2), use_container_width=True)