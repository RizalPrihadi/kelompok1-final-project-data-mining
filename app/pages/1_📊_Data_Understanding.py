import streamlit as st
import pandas as pd
from utils.helper import section_title

from utils.helper import load_css

load_css()

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Data Understanding",
    page_icon="📊",
    layout="wide"
)

# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_data():
    return pd.read_excel(
        "../dataset/raw/emdat-country-profiles_idn_2026_05_23.xlsx"
    )

df = load_data()

# =====================================================
# HEADER
# =====================================================

st.title("📊 Data Understanding")

st.markdown("""
Tahap **Data Understanding** bertujuan untuk memahami karakteristik dataset,
mengevaluasi kualitas data, serta mengidentifikasi pola awal yang dapat digunakan
pada proses clustering.
""")

st.divider()

# =====================================================
# DATASET OVERVIEW
# =====================================================

section_title(
    "Dataset Overview",
    "📋"
)

st.image(
    "../reports/figures/2_distribution.png",
    use_container_width=True
)

st.info("""
Visualisasi distribusi data digunakan untuk memahami
karakteristik awal dataset bencana Indonesia.
""")

# =====================================================
# MISSING VALUE ANALYSIS
# =====================================================

section_title(
    "Missing Value Analysis",
    "🚨"
)

st.image(
    "../reports/figures/1_missing_value.png",
    use_container_width=True
)

st.success("""
Analisis missing value dilakukan untuk mengetahui
kelengkapan data sebelum proses preprocessing.
""")

# =====================================================
# OUTLIER DETECTION
# =====================================================

section_title(
    "Outlier Detection",
    "📦"
)

st.image(
    "../reports/figures/3_boxplot_outlier.png",
    use_container_width=True
)

st.warning("""
Beberapa variabel memiliki nilai ekstrem.
Karena dataset bencana bersifat historis,
outlier tetap dipertahankan.
""")

# =====================================================
# CATEGORICAL ANALYSIS
# =====================================================

section_title(
    "Categorical Analysis",
    "📊"
)

st.image(
    "../reports/figures/4_categorical_analysis.png",
    use_container_width=True
)

# =====================================================
# CORRELATION ANALYSIS
# =====================================================

section_title(
    "Correlation Analysis",
    "🔗"
)

st.image(
    "../reports/figures/5_correlation_matrix.png",
    use_container_width=True
)

st.info("""
Heatmap korelasi digunakan untuk melihat hubungan
antar variabel numerik dalam dataset.
""")

# =====================================================
# TOTAL DEATHS BY DISASTER TYPE
# =====================================================

section_title(
    "Total Deaths by Disaster Type",
    "☠️"
)

st.image(
    "../reports/figures/6_total_deaths_by_disaster_type.png",
    use_container_width=True
)

st.info("""
Visualisasi ini menunjukkan jenis bencana dengan
jumlah korban meninggal tertinggi di Indonesia.
""")