# Proyecto Integrador — Minería de Datos I

## Información general

**Integrantes:** Daniela Fernández — Julio Nahuel Gomez  
**Carrera:** Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial  
**Institución:** Instituto Tecnológico de Santiago del Estero (ITSE)  
**Materia:** Minería de Datos I  
**Profesor:** Fernando Elias Mubarqui  
**Año:** 2026  

---

## Objetivo del proyecto

Aplicar los contenidos de Minería de Datos I para construir un análisis reproducible
de un dataset de usuarios de una plataforma de streaming. El proyecto incluye
inspección inicial, limpieza y preparación de datos, análisis exploratorio univariado,
bivariado y multivariado, escalamiento y reducción de dimensionalidad mediante PCA,
y comunicación de resultados a través de una aplicación pública en Streamlit.
Las decisiones tomadas en cada etapa están justificadas con evidencia observada
durante el proceso.

---

## Dataset

El dataset provisto por la cátedra contiene registros de usuarios de una plataforma
de streaming. Cada fila representa un usuario con las siguientes variables:
plan de suscripción (Básico, Estándar, Premium), minutos de consumo mensual,
género favorito de contenido, país de origen, fecha de último login y cantidad
de tickets al soporte técnico.

- Dataset original: 8.160 filas, 8 columnas — disponible en `data/raw/`
- Dataset procesado: 7.003 filas, 8 columnas — disponible en `data/processed/`

---

## Estructura del repositorio
PI_Mineria_Datos_I/

├── README.md

├── requirements.txt

├── data/

│   ├── raw/

│   └── processed/

├── notebooks/

│   ├── 01_inspeccion_inicial.ipynb

│   ├── 02_calidad_y_limpieza.ipynb

│   ├── 03_eda.ipynb

│   ├── 04_pca.ipynb

│   └── 05_conclusiones.ipynb

├── app/

│   ├── Home.py

│   └── pages/

│       ├── 01_Dataset.py

│       ├── 02_EDA.py

│       ├── 03_PCA.py

│       └── 04_Conclusiones.py

├── reports/

│   └── informe_final.pdf

└── logs/

└── pipeline_log.csv
----------------
## Preparación y calidad de datos

El dataset original presentaba los siguientes problemas detectados en la inspección
inicial: 753 valores faltantes, 126 registros duplicados, inconsistencias en
variables categóricas (mayúsculas/minúsculas, espacios) y valores imposibles
en variables numéricas (edades negativas, minutos negativos).

Las transformaciones aplicadas fueron:
- Eliminación de 126 duplicados
- Normalización de `subscription_plan`, `country` y `favorite_genre`
- Imputación de valores faltantes con mediana para variables numéricas y moda para categóricas
- Eliminación de registros con valores fuera del rango lógico

El registro completo de transformaciones está disponible en [`logs/pipeline_log.csv`](logs/pipeline_log.csv).
El dataset final retiene el 85.82% de los datos originales.

---

## Resumen del análisis exploratorio

El análisis exploratorio se desarrolló en [`notebooks/03_eda.ipynb`](notebooks/03_eda.ipynb)
respondiendo 7 preguntas definidas a partir de la inspección inicial.

Hallazgos principales:
- El 44.75% de los usuarios tiene plan Básico, el 35.36% Estándar y el 19.89% Premium.
- Los usuarios Premium consumen en mediana 1088.88 minutos mensuales, casi el doble
  que los usuarios Básico (551.90 minutos).
- La correlación entre edad y tiempo de visualización es 0.003, prácticamente nula.
- Los géneros favoritos se distribuyen de forma homogénea entre países, sin
  preferencias culturales marcadas.
- La media de edad es 33.4 años, con mayor concentración entre los 25 y 45 años.

El plan de suscripción es el factor más determinante en el comportamiento de consumo,
por encima de la edad, el país o el género favorito.

---

## Reducción de dimensionalidad

El análisis PCA se desarrolló en [`notebooks/04_pca.ipynb`](notebooks/04_pca.ipynb).
Se aplicó StandardScaler sobre 7 variables antes de ejecutar PCA.

Resultados:
- La PC1 explica el 21.83% de la varianza y está dominada por `monthly_watch_time_mins`
  y `subscription_plan_enc` (loadings de 0.71).
- Se necesitan 5 componentes para superar el 80% de varianza acumulada.
- La varianza se distribuye de forma pareja entre las 7 componentes, lo que indica
  baja correlación entre variables y confirma los hallazgos del EDA.

---

## Visualización interactiva

La aplicación pública desarrollada en Streamlit presenta los resultados del proyecto
en 5 páginas: Dataset, EDA (5 visualizaciones), PCA (2 visualizaciones) y Conclusiones.

🔗 [Ver aplicación en Streamlit](https://proyectointegrador-mineriadedatos1-itse.streamlit.app/)

---

## Cómo ejecutar localmente

```bash
# 1. Clonar el repositorio
git clone https://github.com/Danielafz/PI_Mineria_Datos_I.git

# 2. Crear y activar entorno virtual
python -m venv venv
venv\Scripts\Activate.ps1

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar la app
streamlit run app/Home.py
```

---

## Conclusiones

El plan de suscripción es el factor más determinante en el uso de la plataforma:
los usuarios Premium consumen casi el doble de contenido que los Básico,
independientemente de su edad o país de origen. Este resultado fue consistente
en el EDA y confirmado por el PCA.

La edad, los géneros favoritos y el país no mostraron influencia significativa
en el comportamiento de consumo, lo que sugiere una audiencia diversa con
gustos homogéneos.

El alcance de las conclusiones se encuentra condicionado por la información
disponible y por las decisiones documentadas durante el proceso.

🔗 [Repositorio GitHub](https://github.com/Danielafz/PI_Mineria_Datos_I)  
🔗 [Aplicación Streamlit](https://proyectointegrador-mineriadedatos1-itse.streamlit.app/)
