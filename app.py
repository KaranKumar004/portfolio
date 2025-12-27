import streamlit as st
import base64

# 1. Page Config
st.set_page_config(page_title="Karan Kumar Portfolio", layout="wide", initial_sidebar_state="collapsed")

# 2. Define the background image variable
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        return base64.b64encode(f.read()).decode()

# Using your new background image name
try:
    bg_img = get_base64("assets/images/new1.jpg") 
except FileNotFoundError:
    # Fallback if the name is different
    bg_img = ""

# 3. CSS BLOCK (High-Contrast & Top Nav)
st.markdown(f"""
<style>
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                    url("data:image/png;base64,{bg_img}");
        background-size: cover;
        background-attachment: fixed;
    }}
    
    /* Center the Top Nav */
    .nav-container {{
        display: flex;
        justify-content: center;
        gap: 15px;
        padding: 15px;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 50px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 50px;
        position: sticky;
        top: 10px;
        z-index: 1000;
    }}
    
    .nav-link {{
        color: white !important;
        text-decoration: none !important;
        font-weight: 600;
        padding: 8px 15px;
        border-radius: 20px;
        transition: 0.3s;
        font-size: 0.9rem;
    }}
    
    .nav-link:hover {{
        background: rgba(255, 255, 255, 0.2);
        color: #38bdf8 !important;
    }}

    [data-testid="stSidebar"] {{ display: none; }}
</style>
""", unsafe_allow_html=True)


# 4. Top Navigation Bar (Updated with Certifications)
st.markdown(f"""
<div class="nav-container">
    <a class="nav-link" href="/?page=home" target="_self">Home</a>
    <a class="nav-link" href="/?page=about" target="_self">About</a>
    <a class="nav-link" href="/?page=skills" target="_self">Skills</a>
    <a class="nav-link" href="/?page=projects" target="_self">Projects</a>
    <a class="nav-link" href="/?page=analytics" target="_self">Analytics</a>
    <a class="nav-link" href="/?page=certs" target="_self">Certifications</a>
    <a class="nav-link" href="/?page=contact" target="_self">Contact</a>
</div>
""", unsafe_allow_html=True)

# 5. Routing Logic (Updated)
query_params = st.query_params
page = query_params.get("page", "home")

if page == "home":
    with open("pages/1_Home.py", encoding="utf-8") as f:
        exec(f.read())
elif page == "about":
    with open("pages/2_About_Me.py", encoding="utf-8") as f:
        exec(f.read())
elif page == "skills":
    with open("pages/3_Skills.py", encoding="utf-8") as f:
        exec(f.read())
elif page == "projects":
    with open("pages/4_Projects.py", encoding="utf-8") as f:
        exec(f.read())
elif page == "analytics":
    with open("pages/7_Analytics_Algorithms.py", encoding="utf-8") as f:
        exec(f.read())
elif page == "certs":
    # Link to the certification page we created
    with open("pages/5_Certifications.py", encoding="utf-8") as f:
        exec(f.read())
elif page == "contact":
    with open("pages/6_Contact.py", encoding="utf-8") as f:
        exec(f.read())