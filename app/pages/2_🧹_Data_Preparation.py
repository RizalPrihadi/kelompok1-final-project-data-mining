import streamlit as st

from utils.helper import section_title

from utils.helper import load_css

load_css()

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Data Preparation",
    page_icon="🧹",
    layout="wide"
)

# =====================================================
# HEADER
# =====================================================

st.title("🧹 Data Preparation")

st.markdown("""
Tahap **Data Preparation** dilakukan untuk membersihkan,
memilih, dan mentransformasi data sehingga siap digunakan
pada proses clustering menggunakan algoritma K-Means.
""")

st.divider()

# =====================================================
# RINGKASAN PROSES
# =====================================================

section_title(
    "Data Preparation Workflow",
    "📝"
)

st.markdown("""
Tahapan yang dilakukan:

1. 🚨 Missing Value Handling
2. 🔄 Duplicate Removal
3. 📦 Outlier Analysis
4. ⚖️ Feature Selection
5. 📏 Data Standardization
6. 📉 PCA (Principal Component Analysis)
""")

# =====================================================
# MISSING VALUE HANDLING
# =====================================================

section_title(
    "Missing Value Handling",
    "🚨"
)

st.success("""
Seluruh missing value diperiksa dan ditangani
menggunakan metode imputasi yang sesuai.

Tujuan:
- Menghindari error saat modeling
- Menjaga kualitas data
- Meningkatkan stabilitas clustering
""")

# =====================================================
# DUPLICATE REMOVAL
# =====================================================

section_title(
    "Duplicate Removal",
    "🔄"
)

st.info("""
Data duplikat diperiksa dan dihapus
agar setiap record merepresentasikan
kejadian bencana yang unik.
""")

# =====================================================
# OUTLIER ANALYSIS
# =====================================================

section_title(
    "Outlier Analysis",
    "📦"
)

st.warning("""
Outlier ditemukan pada beberapa variabel
seperti jumlah korban meninggal dan kerugian ekonomi.

Karena dataset EM-DAT merupakan data historis bencana,
outlier tetap dipertahankan karena memiliki nilai informasi
yang penting.
""")

# =====================================================
# FEATURE SELECTION
# =====================================================

section_title(
    "Feature Selection",
    "⚖️"
)

st.markdown("""
Fitur yang dipilih untuk proses clustering:

- Total Events
- Total Deaths
- Total Affected
- Total Damage (USD, original)

Fitur-fitur tersebut dianggap paling representatif
dalam menggambarkan tingkat dampak bencana.
""")

# =====================================================
# STANDARDIZATION
# =====================================================

section_title(
    "Data Standardization",
    "📏"
)

st.info("""
StandardScaler digunakan untuk menyamakan skala seluruh fitur.

Alasan:

- K-Means sensitif terhadap skala data
- Menghindari dominasi fitur dengan nilai besar
- Meningkatkan kualitas clustering
""")

# =====================================================
# PCA VISUALIZATION
# =====================================================

section_title(
    "PCA Visualization",
    "📉"
)

st.image(
    "../reports/figures/7_pca_visualization.png",
    use_container_width=True
)

st.success("""
PCA digunakan untuk mereduksi dimensi data
menjadi dua komponen utama.

Tujuan:

• Memudahkan visualisasi data

• Melihat pola penyebaran data

• Membantu interpretasi hasil clustering
""")

# =====================================================
# DATA PREPARATION SUMMARY
# =====================================================

section_title(
    "Data Preparation Summary",
    "📊"
)

st.markdown("""
### Hasil Tahap Data Preparation

✅ Missing value berhasil ditangani

✅ Data duplikat berhasil dihapus

✅ Outlier berhasil dianalisis

✅ Fitur penting berhasil dipilih

✅ Standardisasi berhasil dilakukan

✅ PCA berhasil diterapkan

Data siap digunakan pada tahap
**Modeling menggunakan K-Means Clustering**.
""")