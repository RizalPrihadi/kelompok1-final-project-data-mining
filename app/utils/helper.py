import streamlit as st

def load_css():

    with open(
        "assets/style.css"
    ) as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

def section_title(title, icon="📌"):
    st.markdown(
        f"""
        <div class='section-title'>
            <h3>{icon} {title}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )