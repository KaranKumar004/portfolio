import streamlit as st

st.set_page_config(page_title="Contact | Karan Kumar", layout="wide")

# Theme-aware accent color
accent = "#38bdf8" if st.session_state.get("theme") == "dark" else "#6366f1"

st.markdown(f"""
<style>
    .contact-card {{
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        transition: all 0.3s ease;
        text-decoration: none;
        display: block;
        height: 100%;
    }}
    .contact-card:hover {{
        transform: translateY(-10px);
        border: 1px solid {accent};
        background: rgba(255, 255, 255, 0.1);
    }}
    .contact-icon {{
        font-size: 2.5rem;
        margin-bottom: 15px;
    }}
    .contact-text {{
        font-size: 1.1rem;
        font-weight: 600;
        color: {accent};
    }}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown(f"""
<div style="
    background: rgba(0, 0, 0, 0.6); 
    padding: 60px; 
    border-radius: 30px; 
    text-align: center; 
    color: white !important; 
    margin-bottom: 40px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(15px);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
">
    <h1 style="
        color: white !important; 
        margin-bottom: 15px; 
        text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.8);
        background: linear-gradient(to right, {accent}, #9333ea);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline-block;
        font-size: 3.5rem;
    ">
         Let's Connect
    </h1>
    <p style="
        font-size: 1.3rem; 
        color: white !important; 
        opacity: 1 !important; 
        font-weight: 400;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
    ">
        Currently open to <b style="color: {accent};">Data Analyst</b> & <b style="color: #9333ea;">Junior Data Scientist</b> opportunities in Bangalore.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------- CONTACT GRID ----------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <a href="mailto:karankumarsk14@gmail.com" class="contact-card">
        <div class="contact-icon">📧</div>
        <div class="contact-text">Email</div>
        <p style="font-size:0.8rem; opacity:0.7;">Click to send mail</p>
    </a>
    """, unsafe_allow_html=True) 

with col2:
    st.markdown(f"""
    <a href="https://www.linkedin.com/public-profile/settings?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_self_edit_contact-info%3B8Bk3YPQ7TWikBarnS9WLpg%3D%3D" target="_blank" class="contact-card">
        <div class="contact-icon">💼</div>
        <div class="contact-text">LinkedIn</div>
        <p style="font-size:0.8rem; opacity:0.7;">Professional Network</p>
    </a>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <a href="https://github.com/KaranKumar004" target="_blank" class="contact-card">
        <div class="contact-icon">💻</div>
        <div class="contact-text">GitHub</div>
        <p style="font-size:0.8rem; opacity:0.7;">View My Code</p>
    </a>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="contact-card">
        <div class="contact-icon">📍</div>
        <div class="contact-text">Location</div>
        <p style="font-size:0.8rem; opacity:0.7;">Bangalore, India</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------- FINAL PITCH ----------
st.markdown("<hr style='border-color: rgba(255,255,255,0.2);'>", unsafe_allow_html=True)

st.markdown(f"""
<div style="
    text-align:center; 
    max-width:800px; 
    margin: 20px auto; 
    padding: 30px;
    background: rgba(0, 0, 0, 0.5); 
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    color: #FFFFFF !important; 
    opacity: 1 !important;
">
    <h3 style="color: #FFFFFF !important; text-shadow: 2px 2px 4px rgba(0,0,0,0.8); margin-top:0;">
        Why work with me?
    </h3>
    <p style="
        color: #FFFFFF !important; 
        opacity: 1 !important; 
        font-size: 1.15rem; 
        line-height: 1.8;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    ">
        I combine <b>technical rigor</b> (Python/R) with <b>operational experience</b> (Genpact). 
        I don't just provide data; I provide the automated frameworks that keep data accurate and teams efficient.
    </p>
</div>
""", unsafe_allow_html=True)