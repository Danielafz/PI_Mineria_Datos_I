import streamlit as st
import pandas as pd
import plotly.express as px

# ── CONFIGURACIÓN ─────────────────────────────────────────────────────────
st.set_page_config(page_title="EDA", page_icon="📈", layout="wide")

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
    </style>
""", unsafe_allow_html=True)

# ── TÍTULO ────────────────────────────────────────────────────────────────
st.title("📈 Análisis Exploratorio de Datos")
st.markdown("5 visualizaciones con interpretación — univariado, bivariado y multivariado.")

st.divider()

# ── CARGA DEL DATASET ─────────────────────────────────────────────────────
@st.cache_data
def cargar_datos():
    url = "https://raw.githubusercontent.com/Danielafz/PI_Mineria_Datos_I/main/data/processed/streaming_users_clean.csv"
    return pd.read_csv(url)

df = cargar_datos()

# ── ANÁLISIS UNIVARIADO ───────────────────────────────────────────────────
st.markdown("## 1. Análisis Univariado")

# Visualización 1
st.markdown("### 📊 Distribución de usuarios por plan de suscripción")
conteo = df['subscription_plan'].value_counts().reset_index()
conteo.columns = ['Plan', 'Cantidad']
fig1 = px.bar(
    conteo, x='Plan', y='Cantidad', color='Plan',
    text='Cantidad',
    title='Distribución por plan de suscripción',
    color_discrete_map={'Básico': '#28A745', 'Estándar': '#FFC107', 'Premium': '#DC3545'}
)
fig1.update_layout(plot_bgcolor='white', paper_bgcolor='#F8F9FA')
st.plotly_chart(fig1, use_container_width=True)
st.markdown("""
<div class="info-card">
    <p>📌 <b>Interpretación:</b> El 44.75% de los usuarios tiene plan Básico, el 35.36% Estándar
    y el 19.89% Premium. La plataforma tiene una base de usuarios orientada a planes
    económicos. Menos de un quinto de los usuarios elige el plan más caro.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# Visualización 2
st.markdown("### 👥 Distribución de edades de los usuarios")
fig2 = px.histogram(
    df, x='age', nbins=30,
    color_discrete_sequence=['#1E6FBA'],
    title='Distribución de edades',
    labels={'age': 'Edad', 'count': 'Frecuencia'}
)
fig2.update_layout(plot_bgcolor='white', paper_bgcolor='#F8F9FA')
st.plotly_chart(fig2, use_container_width=True)
st.markdown("""
<div class="info-card">
    <p>📌 <b>Interpretación:</b> La media de edad es 33.4 años y la mediana es 33 años,
    con mayor concentración entre los 25 y 45 años. La distribución es
    aproximadamente simétrica, lo que indica que la plataforma es utilizada
    principalmente por adultos jóvenes y de mediana edad.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── ANÁLISIS BIVARIADO ────────────────────────────────────────────────────
st.markdown("## 2. Análisis Bivariado")

# Visualización 3
st.markdown("### 📦 Tiempo de visualización según plan de suscripción")
fig3 = px.box(
    df, x='subscription_plan', y='monthly_watch_time_mins',
    color='subscription_plan',
    title='Tiempo de visualización por plan',
    labels={
        'subscription_plan': 'Plan',
        'monthly_watch_time_mins': 'Minutos mensuales'
    },
    color_discrete_map={'Básico': '#28A745', 'Estándar': '#FFC107', 'Premium': '#DC3545'}
)
fig3.update_layout(plot_bgcolor='white', paper_bgcolor='#F8F9FA')
st.plotly_chart(fig3, use_container_width=True)
st.markdown("""
<div class="info-card">
    <p>📌 <b>Interpretación:</b> La mediana de visualización mensual es 1088.88 minutos para
    Premium, 838.95 para Estándar y 551.90 para Básico. Existe una relación clara
    entre el plan contratado y el consumo de contenido: los usuarios Premium
    consumen casi el doble que los Básico.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# Visualización 4
st.markdown("### 🔵 Relación entre edad y tiempo de visualización")
fig4 = px.scatter(
    df, x='age', y='monthly_watch_time_mins',
    color='subscription_plan', opacity=0.5,
    title='Edad vs. Tiempo de visualización',
    labels={
        'age': 'Edad',
        'monthly_watch_time_mins': 'Minutos mensuales',
        'subscription_plan': 'Plan'
    },
    color_discrete_map={'Básico': '#28A745', 'Estándar': '#FFC107', 'Premium': '#DC3545'}
)
fig4.update_layout(plot_bgcolor='white', paper_bgcolor='#F8F9FA')
st.plotly_chart(fig4, use_container_width=True)
st.markdown("""
<div class="info-card">
    <p>📌 <b>Interpretación:</b> El coeficiente de correlación entre edad y tiempo de
    visualización es 0.003, prácticamente cero. La edad no tiene influencia
    en el tiempo de visualización. El consumo de contenido es independiente
    de la edad del usuario.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── ANÁLISIS MULTIVARIADO ─────────────────────────────────────────────────
st.markdown("## 3. Análisis Multivariado")

# Visualización 5
st.markdown("### 🗺️ Distribución de géneros por país")
fig5 = px.density_heatmap(
    df, x='country', y='favorite_genre',
    title='Distribución de géneros por país',
    labels={'country': 'País', 'favorite_genre': 'Género favorito'},
    color_continuous_scale='Blues'
)
fig5.update_layout(plot_bgcolor='white', paper_bgcolor='#F8F9FA')
st.plotly_chart(fig5, use_container_width=True)
st.markdown("""
<div class="info-card">
    <p>📌 <b>Interpretación:</b> La distribución de géneros por país es homogénea en todos
    los casos. No existen preferencias culturales marcadas por país: los gustos
    de los usuarios son similares independientemente de su origen. El plan de
    suscripción es el factor más determinante en el comportamiento, por encima
    del país o del género favorito.</p>
</div>
""", unsafe_allow_html=True)