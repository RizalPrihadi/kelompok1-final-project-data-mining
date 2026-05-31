import streamlit as st

from utils.helper import section_title

from utils.helper import load_css

load_css()

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Evaluation",
    page_icon="📈",
    layout="wide"
)

# =====================================================
# HEADER
# =====================================================

st.title("📈 Evaluation")

st.markdown("""
Tahap **Evaluation** dilakukan untuk menilai kualitas
hasil clustering dan memastikan model yang dibangun
mampu memberikan insight yang relevan terhadap
analisis bencana di Indonesia.
""")

st.divider()

# =====================================================
# EVALUATION OBJECTIVES
# =====================================================

section_title(
    "Evaluation Objectives",
    "🎯"
)

st.info("""
Tujuan evaluasi:

✅ Mengukur kualitas cluster

✅ Menilai pemisahan antar cluster

✅ Memastikan cluster mudah diinterpretasikan

✅ Memberikan insight yang bermanfaat
untuk pengambilan keputusan
""")

# =====================================================
# EVALUATION METRICS
# =====================================================

section_title(
    "Evaluation Metrics",
    "📊"
)

st.image(
    "../reports/figures/13_evaluation_metrics.png",
    use_container_width=True
)

st.success("""
Metric evaluasi digunakan untuk mengukur
seberapa baik model K-Means mengelompokkan data.

Metrik yang digunakan:

• Silhouette Score

• Inertia

• Within Cluster Sum of Squares (WCSS)

Semakin tinggi nilai Silhouette Score,
semakin baik kualitas cluster yang terbentuk.
""")

# =====================================================
# CLUSTER DISTRIBUTION REVIEW
# =====================================================

section_title(
    "Cluster Distribution Review",
    "🔍"
)

st.image(
    "../reports/figures/14_cluster_distribution_review.png",
    use_container_width=True
)

st.info("""
Distribusi cluster dievaluasi untuk memastikan
tidak terdapat cluster yang terlalu dominan
atau terlalu sedikit anggotanya.

Distribusi yang seimbang menunjukkan bahwa
model mampu memanfaatkan informasi data
secara efektif.
""")

# =====================================================
# BUSINESS CLUSTER PROFILE
# =====================================================

section_title(
    "Business Cluster Profile",
    "💼"
)

st.image(
    "../reports/figures/15_business_cluster_profile.png",
    use_container_width=True
)

st.markdown("""
### 🟢 Cluster 0 — Low Impact Disaster

Karakteristik:

- Jumlah korban rendah
- Kerugian ekonomi rendah
- Dampak sosial relatif kecil

Rekomendasi:

- Monitoring rutin
- Edukasi masyarakat
- Pencegahan dasar

---

### 🟡 Cluster 1 — Medium Impact Disaster

Karakteristik:

- Korban menengah
- Kerugian ekonomi menengah
- Membutuhkan respons lebih cepat

Rekomendasi:

- Peningkatan kesiapsiagaan
- Penguatan infrastruktur
- Sistem peringatan dini

---

### 🔴 Cluster 2 — High Impact Disaster

Karakteristik:

- Korban tinggi
- Kerugian ekonomi besar
- Dampak luas terhadap masyarakat

Rekomendasi:

- Prioritas mitigasi nasional
- Alokasi sumber daya lebih besar
- Penguatan kebijakan kebencanaan
""")

# =====================================================
# EVALUATION SUMMARY
# =====================================================

section_title(
    "Evaluation Summary",
    "📋"
)

st.success("""
### Hasil Evaluasi

✅ Model berhasil membentuk cluster yang jelas

✅ Cluster memiliki karakteristik yang berbeda

✅ Silhouette Score menunjukkan kualitas clustering yang baik

✅ Hasil cluster mudah diinterpretasikan

✅ Cluster memberikan insight yang bermanfaat
untuk analisis risiko bencana Indonesia
""")

# =====================================================
# BUSINESS IMPACT
# =====================================================

section_title(
    "Business Impact",
    "🚀"
)

st.markdown("""
Hasil clustering dapat dimanfaatkan untuk:

### 🏛 Pemerintah

- Menentukan prioritas mitigasi bencana
- Menyusun kebijakan kebencanaan

### 🚑 BPBD dan BNPB

- Menentukan wilayah prioritas
- Menyiapkan strategi respons bencana

### 📊 Peneliti

- Mengidentifikasi pola dampak bencana
- Mendukung penelitian lanjutan

### 🌍 Masyarakat

- Meningkatkan kesiapsiagaan
- Mendukung edukasi kebencanaan
""")

# =====================================================
# KESIMPULAN AKHIR
# =====================================================

section_title(
    "Final Conclusion",
    "🏁"
)

st.balloons()

st.success("""
Model K-Means Clustering berhasil digunakan
untuk mengelompokkan data bencana Indonesia
berdasarkan tingkat dampaknya.

Model menghasilkan tiga kelompok utama:

🟢 Low Impact Disaster

🟡 Medium Impact Disaster

🔴 High Impact Disaster

Hasil clustering dapat digunakan sebagai
dasar pengambilan keputusan dalam mitigasi
dan manajemen risiko bencana.
""")