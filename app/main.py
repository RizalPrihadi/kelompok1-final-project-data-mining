import streamlit as st
import pandas as pd
import plotly.express as px

from utils.helper import load_css

load_css()

# =====================================================
# CONFIG
# =====================================================

st.set_page_config(
    page_title="Dashboard",
    page_icon="🌋",
    layout="wide"
)

# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_data():
    return pd.read_csv(
        "../dataset/processed/disaster_clustered.csv"
    )

df = load_data()

# =====================================================
# HERO SECTION
# =====================================================

st.title("🌋 Indonesia Disaster Clustering Dashboard")

st.markdown("""
### CRISP-DM Based Disaster Analysis

Dashboard ini digunakan untuk menganalisis
profil bencana di Indonesia menggunakan
algoritma K-Means Clustering.

Silakan pilih menu di sidebar.
""")

# =====================================================
# KPI
# =====================================================

cluster_count = df["Cluster"].nunique()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📄 Total Data",
        f"{len(df):,}"
    )

with col2:
    st.metric(
        "📊 Total Fitur",
        df.shape[1]-1
    )

with col3:
    st.metric(
        "🤖 Total Cluster",
        cluster_count
    )

with col4:
    st.metric(
        "📈 Data Siap Analisis",
        "100%"
    )

st.divider()

# =====================================================
# PROJECT OVERVIEW
# =====================================================

st.subheader("📌 Project Overview")

overview_col1, overview_col2 = st.columns([2,1])

with overview_col1:

    st.markdown("""
### Tujuan Project

Mengelompokkan data bencana Indonesia berdasarkan:

- Total Events
- Total Deaths
- Total Affected
- Total Damage

Menggunakan algoritma K-Means Clustering untuk menemukan
pola bencana berdasarkan tingkat dampaknya.
""")

with overview_col2:

    st.info("""
### Metodologi

✅ Business Understanding

✅ Data Understanding

✅ Data Preparation

✅ Modeling

✅ Evaluation

✅ Deployment
""")

st.divider()

# =====================================================
# CLUSTER DISTRIBUTION
# =====================================================

st.subheader("📊 Distribusi Cluster")

cluster_distribution = (
    df["Cluster"]
    .value_counts()
    .sort_index()
    .reset_index()
)

cluster_distribution.columns = [
    "Cluster",
    "Jumlah Data"
]

fig_cluster = px.bar(
    cluster_distribution,
    x="Cluster",
    y="Jumlah Data",
    text="Jumlah Data",
    title="Jumlah Data pada Setiap Cluster"
)

fig_cluster.update_traces(
    textposition="outside"
)

st.plotly_chart(
    fig_cluster,
    use_container_width=True
)

# =====================================================
# PIE CHART
# =====================================================

col1, col2 = st.columns(2)

with col1:

    fig_pie = px.pie(
        cluster_distribution,
        names="Cluster",
        values="Jumlah Data",
        hole=0.5,
        title="Persentase Cluster"
    )

    st.plotly_chart(
        fig_pie,
        use_container_width=True
    )

with col2:

    st.markdown("""
### 💡 Interpretasi Cluster

Cluster digunakan untuk mengelompokkan
karakteristik bencana berdasarkan:

- Jumlah kejadian
- Jumlah korban
- Jumlah terdampak
- Kerugian ekonomi

Semakin tinggi nilai rata-rata pada suatu
cluster maka semakin besar dampak bencana
yang direpresentasikan.
""")

# =====================================================
# CLUSTER PROFILE
# =====================================================

st.divider()

st.subheader("📈 Profil Cluster")

cluster_profile = (
    df.groupby("Cluster")
    .mean(numeric_only=True)
    .round(2)
)

st.dataframe(
    cluster_profile,
    use_container_width=True
)

# =====================================================
# KEY INSIGHTS
# =====================================================

st.divider()

st.subheader("💡 Key Insights")

highest_cluster = (
    cluster_profile[
        "Total Damage (USD, original)"
    ].idxmax()
)

highest_damage = (
    cluster_profile[
        "Total Damage (USD, original)"
    ].max()
)

st.success(
    f"""
    🚨 Cluster {highest_cluster}
    memiliki rata-rata kerugian ekonomi tertinggi
    sebesar {highest_damage:,.2f}.
    """
)

st.info(
    """
    📌 Hasil clustering dapat digunakan sebagai
    dasar untuk mengidentifikasi kelompok
    bencana dengan tingkat dampak yang berbeda.
    """
)

st.info("""
🎯 Coba fitur Cluster Prediction untuk
menentukan kategori dampak suatu bencana
berdasarkan model K-Means yang telah dibuat.
""")

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
    "Indonesia Disaster Clustering Dashboard | CRISP-DM | K-Means Clustering"
)