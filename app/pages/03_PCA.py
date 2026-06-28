import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA

# ── CONFIGURACIÓN ─────────────────────────────────────────────────────────
st.set_page_config(page_title="PCA", page_icon="🔬", layout="wide")

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
st.title("🔬 Análisis de Componentes Principales (PCA)")
st.markdown("Escalamiento, reducción de dimensionalidad e interpretación de componentes.")

st.divider()

# ── CARGA Y PREPARACIÓN ───────────────────────────────────────────────────
@st.cache_data
def preparar_datos():
    url = "https://raw.githubusercontent.com/Danielafz/PI_Mineria_Datos_I/main/data/processed/streaming_users_clean.csv"
    df = pd.read_csv(url)
    df['last_login_date'] = pd.to_datetime(df['last_login_date'])
    fecha_referencia = pd.Timestamp('today').normalize()
    df['dias_desde_login'] = (fecha_referencia - df['last_login_date']).dt.days.abs()
    le = LabelEncoder()
    for col in ['subscription_plan', 'country', 'favorite_genre']:
        df[col + '_enc'] = le.fit_transform(df[col].astype(str))
    columnas_pca = [
        'age', 'monthly_watch_time_mins', 'customer_support_tickets',
        'dias_desde_login', 'subscription_plan_enc', 'country_enc', 'favorite_genre_enc'
    ]
    df_pca = df[columnas_pca].copy()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df_pca)
    pca = PCA()
    pca.fit(X_scaled)
    return pca, X_scaled, columnas_pca

pca, X_scaled, columnas_pca = preparar_datos()
varianza_explicada = pca.explained_variance_ratio_
varianza_acumulada = np.cumsum(varianza_explicada)

# ── VARIABLES UTILIZADAS ──────────────────────────────────────────────────
st.markdown("## 1. Variables utilizadas")
st.markdown("""
<div class="info-card">
    <p>Se utilizaron <b>7 variables</b> para el análisis PCA. Las variables categóricas
    fueron codificadas con Label Encoding y la fecha fue transformada en días
    transcurridos desde el último login.</p>
</div>
""", unsafe_allow_html=True)

variables = pd.DataFrame({
    'Variable': columnas_pca,
    'Tipo original': ['Numérica', 'Numérica', 'Numérica', 'Fecha → Numérica',
                      'Categórica → Numérica', 'Categórica → Numérica', 'Categórica → Numérica'],
    'Descripción': [
        'Edad del usuario',
        'Minutos de consumo mensual',
        'Tickets al soporte técnico',
        'Días desde el último acceso',
        'Plan de suscripción codificado',
        'País codificado',
        'Género favorito codificado'
    ]
})
st.dataframe(variables, use_container_width=True, hide_index=True)

st.divider()

# ── ESCALAMIENTO ──────────────────────────────────────────────────────────
st.markdown("## 2. Escalamiento aplicado")
st.markdown("""
<div class="info-card">
    <p>⚖️ Se aplicó <b>StandardScaler</b> para transformar todas las variables a media = 0
    y desviación estándar = 1. Esto es necesario porque PCA es sensible a la escala:
    sin escalar, variables con valores grandes como <code>dias_desde_login</code> (media 1608)
    dominarían artificialmente las componentes por encima de variables como
    <code>subscription_plan_enc</code> (media 0.75).</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── VARIANZA EXPLICADA ────────────────────────────────────────────────────
st.markdown("## 3. Varianza explicada")

col1, col2, col3 = st.columns(3)
col1.metric("📊 Varianza PC1", f"{varianza_explicada[0]*100:.2f}%")
col2.metric("🎯 Componentes para 80%", "5")
col3.metric("🎯 Componentes para 90%", "6")

# Scree Plot
st.markdown("### 📉 Scree Plot")
componentes = list(range(1, len(varianza_explicada) + 1))

fig1 = go.Figure()
fig1.add_trace(go.Bar(
    x=componentes, y=varianza_explicada * 100,
    name='Varianza individual', marker_color='#1E6FBA'
))
fig1.add_trace(go.Scatter(
    x=componentes, y=varianza_acumulada * 100,
    name='Varianza acumulada', mode='lines+markers',
    line=dict(color='#FF6B35', width=2)
))
fig1.add_hline(y=80, line_dash='dash', line_color='orange', annotation_text='80%')
fig1.add_hline(y=90, line_dash='dash', line_color='red', annotation_text='90%')
fig1.update_layout(
    title='Varianza explicada por componente principal',
    xaxis_title='Componente Principal',
    yaxis_title='Varianza (%)',
    xaxis=dict(tickmode='linear'),
    plot_bgcolor='white',
    paper_bgcolor='#F8F9FA'
)
st.plotly_chart(fig1, use_container_width=True)

st.divider()

# Heatmap de Loadings
st.markdown("### 🔥 Heatmap de Loadings")
st.markdown("Contribución de cada variable a las primeras 3 componentes principales.")

pca3 = PCA(n_components=3)
pca3.fit(X_scaled)

loadings = pd.DataFrame(
    pca3.components_.T,
    index=columnas_pca,
    columns=['PC1', 'PC2', 'PC3']
)

fig2 = px.imshow(
    loadings,
    text_auto='.2f',
    color_continuous_scale='RdBu_r',
    color_continuous_midpoint=0,
    title='Heatmap de Loadings — contribución de variables a cada componente',
    aspect='auto'
)
fig2.update_layout(paper_bgcolor='#F8F9FA')
st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ── INTERPRETACIÓN ────────────────────────────────────────────────────────
st.markdown("## 4. Interpretación")
st.markdown("""
<div class="info-card">
    <p>🔵 <b>PC1 — Perfil de consumo (21.83% de la varianza)</b><br>
    Dominada por monthly_watch_time_mins y subscription_plan_enc (ambas con loading 0.71).
    Captura el comportamiento de consumo del usuario.</p>
    <p>🟢 <b>PC2 — Perfil geográfico y actividad (14.64% de la varianza)</b><br>
    Dominada por country_enc (0.68) y dias_desde_login (0.63). Captura la combinación
    entre el país del usuario y su nivel de actividad reciente.</p>
    <p>🟡 <b>PC3 — Perfil demográfico (14.46% de la varianza)</b><br>
    Dominada por age (0.67) y favorite_genre_enc (-0.50). Asocia la edad del usuario
    con sus preferencias de género.</p>
    <p>⚠️ <b>Conclusión:</b> La varianza se distribuye de forma pareja entre las 7 componentes.
    Se necesitan 5 componentes para explicar el 80% de la varianza, confirmando que
    el dataset no tiene correlaciones fuertes entre variables.</p>
</div>
""", unsafe_allow_html=True)