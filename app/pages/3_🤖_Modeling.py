import streamlit as st
import pandas as pd

from utils.helper import section_title

from utils.helper import load_css

load_css()

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Modeling",
    page_icon="🤖",
    layout="wide"
)

# =====================================================
# HEADER
# =====================================================

st.title("🤖 Modeling")

st.markdown("""
Tahap **Modeling** bertujuan untuk mengelompokkan data
bencana Indonesia menggunakan algoritma
**K-Means Clustering** berdasarkan karakteristik
dampak bencana.
""")

st.divider()

# =====================================================
# ALGORITMA YANG DIGUNAKAN
# =====================================================

section_title(
    "Model Selection",
    "📌"
)

st.info("""
Model yang digunakan adalah:

✅ K-Means Clustering

Alasan pemilihan:

• Cocok untuk data tanpa label

• Mudah diinterpretasikan

• Efektif untuk segmentasi data

• Banyak digunakan pada analisis clustering
""")

# =====================================================
# FITUR YANG DIGUNAKAN
# =====================================================

section_title(
    "Selected Features",
    "📊"
)

st.markdown("""
Fitur yang digunakan dalam proses clustering:

- Total Events
- Total Deaths
- Total Affected
- Total Damage (USD, original)

Keempat fitur tersebut merepresentasikan
tingkat dampak suatu bencana.
""")

# =====================================================
# ELBOW METHOD
# =====================================================

section_title(
    "Elbow Method",
    "📈"
)

st.image(
    "../reports/figures/8_elbow_method.png",
    use_container_width=True
)

st.success("""
Elbow Method digunakan untuk menentukan
jumlah cluster optimal.

Titik siku (elbow point) menunjukkan jumlah
cluster yang memberikan keseimbangan terbaik
antara kompleksitas model dan variasi data.

Berdasarkan grafik, dipilih K = 3 cluster.
""")

# =====================================================
# SILHOUETTE ANALYSIS
# =====================================================

section_title(
    "Silhouette Analysis",
    "🎯"
)

st.image(
    "../reports/figures/9_silhouette_analysis.png",
    use_container_width=True
)

st.info("""
Silhouette Score digunakan untuk mengukur
kualitas hasil clustering.

Interpretasi:

• Mendekati 1 → Cluster sangat baik

• Mendekati 0 → Cluster saling tumpang tindih

• Mendekati -1 → Cluster buruk

Semakin tinggi nilai silhouette score,
semakin baik kualitas cluster yang terbentuk.
""")

# =====================================================
# DISTRIBUSI CLUSTER
# =====================================================

section_title(
    "Cluster Distribution",
    "📊"
)

st.image(
    "../reports/figures/10_cluster_distribution.png",
    use_container_width=True
)

st.success("""
Visualisasi ini menunjukkan jumlah data
yang masuk ke masing-masing cluster.

Distribusi cluster membantu memahami
komposisi data hasil segmentasi.
""")

# =====================================================
# CLUSTER VISUALIZATION
# =====================================================

section_title(
    "Cluster Visualization",
    "🌍"
)

st.image(
    "../reports/figures/11_cluster_visualization.png",
    use_container_width=True
)

st.info("""
Visualisasi cluster menunjukkan pemisahan
antar kelompok data setelah proses clustering.

Semakin jelas pemisahan antar cluster,
semakin baik performa model K-Means.
""")

# =====================================================
# CLUSTER PROFILE
# =====================================================

section_title(
    "Cluster Profile",
    "📋"
)

st.image(
    "../reports/figures/12_cluster_profile.png",
    use_container_width=True
)

st.markdown("""
### Karakteristik Cluster

🟢 **Cluster 0**

- Dampak rendah
- Korban relatif sedikit
- Kerugian ekonomi rendah

---

🟡 **Cluster 1**

- Dampak sedang
- Korban dan kerugian menengah

---

🔴 **Cluster 2**

- Dampak tinggi
- Korban tinggi
- Kerugian ekonomi besar
""")

# =====================================================
# MODELING SUMMARY
# =====================================================

section_title(
    "Modeling Summary",
    "💡"
)

st.success("""
### Hasil Modeling

✅ Algoritma K-Means berhasil diterapkan

✅ Jumlah cluster optimal berhasil ditentukan

✅ Data berhasil dikelompokkan menjadi 3 cluster

✅ Cluster memiliki karakteristik yang berbeda

### Output Modeling

1. Low Impact Disaster
2. Medium Impact Disaster
3. High Impact Disaster

Hasil clustering akan dievaluasi lebih lanjut
pada tahap Evaluation.
""")