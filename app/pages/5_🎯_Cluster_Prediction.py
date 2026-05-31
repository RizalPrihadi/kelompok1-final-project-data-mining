import streamlit as st
import pandas as pd
import joblib

from utils.helper import section_title

from utils.helper import load_css

load_css()

# =====================================================
# LOAD MODEL
# =====================================================

kmeans = joblib.load("../models/kmeans.pkl")
scaler = joblib.load("../models/scaler.pkl")

# =====================================================
# HEADER
# =====================================================

st.title("🤖 Disaster Cluster Prediction")

st.markdown("""
Masukkan karakteristik bencana untuk mengetahui
cluster dampak bencana berdasarkan model
K-Means Clustering yang telah dibuat.
""")

st.divider()

# =====================================================
# INPUT FORM
# =====================================================

section_title(
    "Input Disaster Information",
    "📝"
)

col1, col2 = st.columns(2)

with col1:

    total_events = st.number_input(
        "Total Events",
        min_value=0.0,
        value=1.0
    )

    total_deaths = st.number_input(
        "Total Deaths",
        min_value=0.0,
        value=0.0
    )

with col2:

    total_affected = st.number_input(
        "Total Affected",
        min_value=0.0,
        value=100.0
    )

    total_damage = st.number_input(
        "Total Damage (USD, original)",
        min_value=0.0,
        value=0.0
    )

# =====================================================
# PREDIKSI CLUSTER
# =====================================================

if st.button(
    "🚀 Determine Cluster",
    use_container_width=True
):

    input_df = pd.DataFrame({

        "Total Events":[total_events],

        "Total Deaths":[total_deaths],

        "Total Affected":[total_affected],

        "Total Damage (USD, original)":[total_damage]

    })

    scaled_data = scaler.transform(
        input_df
    )

    cluster = kmeans.predict(
        scaled_data
    )[0]

# =====================================================
# HASIL
# =====================================================

    st.divider()

    st.subheader(
        "🎯 Prediction Result"
    )

    st.success(
        f"Predicted Cluster : {cluster}"
    )

# =====================================================
# INTERPRETASI CLUSTER
# =====================================================

    if cluster == 0:

        st.markdown("""
        <div class='cluster-low'>
        🟢 Cluster 0 - Low Impact Disaster
        </div>
        """,
        unsafe_allow_html=True)

        st.info("""
        Karakteristik:

        • Korban relatif rendah

        • Dampak ekonomi rendah

        • Tingkat keparahan rendah
        """)

    elif cluster == 1:

        st.markdown("""
        <div class='cluster-medium'>
        🟡 Cluster 1 - Medium Impact Disaster
        </div>
        """,
        unsafe_allow_html=True)

        st.warning("""
        Karakteristik:

        • Dampak menengah

        • Korban menengah

        • Kerugian ekonomi menengah
        """)

    else:

        st.markdown("""
        <div class='cluster-high'>
        🔴 Cluster 2 - High Impact Disaster
        </div>
        """,
        unsafe_allow_html=True)

        st.error("""
        Karakteristik:

        • Korban tinggi

        • Kerusakan tinggi

        • Kerugian ekonomi besar
        """)

# =====================================================
# VISUALISASI INPUT VS CLUSTER CENTER
# =====================================================

centers = pd.DataFrame(
    kmeans.cluster_centers_,
    columns=[
        "Total Events",
        "Total Deaths",
        "Total Affected",
        "Total Damage (USD, original)"
    ]
)

st.subheader(
    "📊 Cluster Centers"
)

st.dataframe(
    centers,
    use_container_width=True
)