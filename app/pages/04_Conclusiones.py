import streamlit as st

# ── CONFIGURACIÓN ─────────────────────────────────────────────────────────
st.set_page_config(page_title="Conclusiones", page_icon="📝", layout="wide")

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
    .info-card {
        background: white;
        border-radius: 12px;
        padding: 20px 25px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.08);
        border-top: 4px solid #1E6FBA;
        margin-bottom: 15px;
    }
    .info-card p { margin: 8px 0; font-size: 0.95rem; }
    .card-warning {
        background: white;
        border-radius: 12px;
        padding: 20px 25px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.08);
        border-top: 4px solid #FFA500;
        margin-bottom: 15px;
    }
    .card-success {
        background: white;
        border-radius: 12px;
        padding: 20px 25px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.08);
        border-top: 4px solid #28A745;
        margin-bottom: 15px;
    }
    .card-warning p, .card-success p { margin: 8px 0; font-size: 0.95rem; }
    </style>
""", unsafe_allow_html=True)

# ── TÍTULO ────────────────────────────────────────────────────────────────
st.title("📝 Conclusiones")
st.markdown("Hallazgos, limitaciones y próximos pasos del proyecto.")

st.divider()

# ── HALLAZGO PRINCIPAL ────────────────────────────────────────────────────
st.markdown("## 1. Hallazgos principales")

st.markdown("""
<div class="info-card">
    <p>🏆 <b>El plan de suscripción es el factor más determinante en el uso de la plataforma.</b>
    Los usuarios Premium consumen casi el doble de contenido que los usuarios Básico,
    independientemente de su edad o país de origen. Este resultado fue consistente
    a lo largo del análisis exploratorio y fue confirmado por el PCA, donde la PC1
    está dominada por el tiempo de visualización y el plan contratado.</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>📊 Hallazgos del EDA</h3>
        <p>📌 El <b>44.75%</b> de los usuarios tiene plan Básico, el <b>35.36%</b> Estándar
        y el <b>19.89%</b> Premium.</p>
        <p>📌 La mediana de visualización es <b>1088.88 min</b> para Premium,
        <b>838.95 min</b> para Estándar y <b>551.90 min</b> para Básico.</p>
        <p>📌 La correlación entre edad y tiempo de visualización es <b>0.003</b>
        (prácticamente cero).</p>
        <p>📌 Los géneros se distribuyen de forma <b>homogénea</b> entre países.
        No existen preferencias culturales marcadas.</p>
        <p>📌 La plataforma es utilizada principalmente por adultos jóvenes
        con media de edad de <b>33.4 años</b>.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h3>🔬 Hallazgos del PCA</h3>
        <p>📌 La <b>PC1</b> explica el <b>21.83%</b> de la varianza y está dominada
        por monthly_watch_time_mins y subscription_plan_enc.</p>
        <p>📌 Se necesitan <b>5 componentes</b> para explicar el 80% de la varianza.</p>
        <p>📌 La varianza se distribuye de forma <b>pareja</b> entre las 7 componentes,
        lo que indica baja correlación entre variables.</p>
        <p>📌 El PCA confirma que el <b>perfil de consumo</b> es la dimensión más
        relevante del dataset.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ── LIMITACIONES ──────────────────────────────────────────────────────────
st.markdown("## 2. Limitaciones")
st.markdown("""
<div class="card-warning">
    <p>⚠️ El dataset no incluye información sobre ingresos, ocupación ni nivel educativo,
    lo que limita la posibilidad de explicar por qué ciertos usuarios eligen
    planes más costosos.</p>
    <p>⚠️ El Label Encoding aplicado a variables nominales introduce un orden numérico
    artificial que puede afectar la interpretación de los componentes del PCA.</p>
    <p>⚠️ La baja correlación entre variables limita la capacidad de PCA para concentrar
    la varianza en pocas componentes.</p>
    <p>⚠️ El alcance de las conclusiones se encuentra condicionado por la información
    disponible y por las decisiones documentadas durante el proceso.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── PRÓXIMOS PASOS ────────────────────────────────────────────────────────
st.markdown("## 3. Próximos pasos")
st.markdown("""
<div class="card-success">
    <p>✅ Una mejora futura podría consistir en incorporar variables adicionales como
    historial de pagos o tiempo de permanencia en la plataforma, que permitirían
    ampliar el alcance del análisis.</p>
    <p>✅ Aplicar One-Hot Encoding en lugar de Label Encoding para las variables
    nominales mejoraría la calidad del análisis PCA.</p>
    <p>✅ Una mejora futura podría consistir en aplicar técnicas de clustering sobre
    los componentes principales para identificar segmentos de usuarios con
    comportamientos similares.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── ENLACES ───────────────────────────────────────────────────────────────
st.markdown("## 4. Enlaces del proyecto")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="info-card">
        <p>🔗 <a href="https://github.com/Danielafz/PI_Mineria_Datos_I" target="_blank">
        Ver repositorio en GitHub</a></p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="info-card">
        <p>📓 Notebooks disponibles en la carpeta <code>notebooks/</code> del repositorio</p>
    </div>
    """, unsafe_allow_html=True)