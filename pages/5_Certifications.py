import streamlit as st
import os

# Custom CSS for the "Glass" Certificate Cards
st.markdown("""
<style>
    .cert-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        transition: all 0.3s ease;
    }
    .cert-card:hover {
        background: rgba(255, 255, 255, 0.1);
        border-color: #38bdf8;
        transform: translateY(-5px);
    }
    .view-btn {
        color: #38bdf8 !important;
        text-decoration: none;
        font-weight: bold;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("📜 Professional Certifications")

# This matches the filenames in your uploaded image
certificates = [
    {"name": "Deloitte Strategic Analytics", "file": "Deloitte_certificate.pdf", "org": "Deloitte"},
    {"name": "KPMG Data Analytics Virtual Experience", "file": "KPMG_certificate.pdf", "org": "KPMG"},
    {"name": "R Programming (Johns Hopkins)", "file": "certificate R.pdf", "org": "Coursera / JHU"},
    {"name": "Numpy and Pandas Masterclass", "file": "Numpy and Pandas Masterclass Certificate.pdf", "org": "Udemy"},
    {"name": "Excel Fundamentals for Data Analysis", "file": "Excel Fundamentals for Data Analysis.pdf", "org": "Corporate Finance Institute"},
    {"name": "Programming Foundations (JS, HTML, CSS)", "file": "Programming Foundations with JavaScript HTML and CSS.pdf", "org": "Duke University"},
]

# GitHub raw link base (Replace KaranKumar004 with your username if different)
repo_url = "https://raw.githubusercontent.com/KaranKumar004/portfolio/main/assets/certificates/"

for cert in certificates:
    with st.container():
        st.markdown(f"""
        <div class="cert-card">
            <p style="color: #38bdf8; font-size: 0.8rem; margin-bottom: 5px; font-weight: bold;">{cert['org']}</p>
            <h3 style="margin-top: 0; color: white;">{cert['name']}</h3>
            <a href="{repo_url}{cert['file'].replace(' ', '%20')}" target="_blank" class="view-btn">View Official Document →</a>
        </div>
        """, unsafe_allow_html=True)