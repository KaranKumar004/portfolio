import streamlit as st

# Note: Remove st.set_page_config if this is called via exec() in app.py
# st.set_page_config(page_title="Skills | Karan Kumar", layout="wide")

accent_color = "#38bdf8" 

st.markdown(f"""
<style>
    /* Global Force White */
    html, body, [data-testid="stWidgetLabel"], p, span, li, label, h1, h2, h3 {{
        color: white !important;
        opacity: 1 !important;
    }}

    .skill-card {{
        background: rgba(0, 0, 0, 0.7); /* Darker for better white text contrast */
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 20px;
        padding: 30px;
        height: 100%;
        transition: all 0.3s ease;
    }}
    .skill-card:hover {{
        transform: translateY(-5px);
        border: 1px solid {accent_color};
        box-shadow: 0 10px 30px rgba(56, 189, 248, 0.2);
    }}
    .skill-header {{
        color: {accent_color} !important;
        font-size: 1.6rem;
        font-weight: 700;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 10px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }}
    .skill-tag {{
        display: inline-block;
        background: rgba(56, 189, 248, 0.1);
        padding: 6px 14px;
        border-radius: 10px;
        margin: 5px;
        font-size: 0.85rem;
        border: 1px solid {accent_color};
        color: white !important;
        font-weight: 500;
    }}
    .description-text {{
        font-size: 0.9rem;
        line-height: 1.5;
        margin-top: 15px;
        color: #e0e0e0 !important;
    }}
</style>
""", unsafe_allow_html=True)

st.title("🧠 Technical Toolkit")
st.markdown("<p style='font-size:1.2rem;'>A comprehensive breakdown of my engineering and analytical capabilities, from low-level automation to high-level statistical research.</p>", unsafe_allow_html=True)

# --- 3 COLUMN LAYOUT ---
col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown(f"""
    <div class="skill-card">
        <div class="skill-header">🐍 Programming</div>
        <div class="skill-tag">Python (Pandas/NumPy)</div>
        <div class="skill-tag">R (Tidyverse)</div>
        <div class="skill-tag">SQL (PostgreSQL)</div>
        <div class="skill-tag">Streamlit UI</div>
        <div class="skill-tag">OpenPyXL</div>
        <div class="description-text">
            <b>Key Expertise:</b><br>
            • Migrating <b>VBA/Excel</b> logic into <b>Pythonic frameworks</b>.<br>
            • Building <b>Automated Data Pipelines</b> that clean and validate 5,000+ records daily.<br>
            • Developing <b>Interactive Dashboards</b> for real-time KPI tracking.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="skill-card">
        <div class="skill-header">📊 Analytics & ML</div>
        <div class="skill-tag">Scikit-Learn</div>
        <div class="skill-tag">Random Forest</div>
        <div class="skill-tag">K-Means</div>
        <div class="skill-tag">EDA</div>
        <div class="skill-tag">Hypothesis Testing</div>
        <div class="description-text">
            <b>Key Expertise:</b><br>
            • <b>Predictive Modeling:</b> Applying Regression to forecast business metrics.<br>
            • <b>Classification:</b> Predicting churn using ensemble methods like Random Forest.<br>
            • <b>Statistical Rigor:</b> Using R for deep-dive Patent Analysis and Trend Discovery.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="skill-card">
        <div class="skill-header">🛠️ Tools & Ops</div>
        <div class="skill-tag">Power BI / Tableau</div>
        <div class="skill-tag">Git / GitHub</div>
        <div class="skill-tag">UNIFY / Genius</div>
        <div class="skill-tag">Advanced Excel</div>
        <div class="skill-tag">Jupyter</div>
        <div class="description-text">
            <b>Key Expertise:</b><br>
            • <b>Business Intelligence:</b> Creating executive-level visuals in Power BI.<br>
            • <b>Version Control:</b> Managing collaborative codebases via Git.<br>
            • <b>Enterprise Platforms:</b> Deep experience in <b>Genpact UNIFY</b> ecosystem.
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- THE "WHY" SECTION ---
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f"""
<div class="skill-card" style="text-align:center; background: rgba(0,0,0,0.8); border: 2px solid {accent_color};">
    <h3 style="color:{accent_color} !important; margin-bottom:15px;">💡 My Core Value Proposition</h3>
    <p style="max-width: 900px; margin: 0 auto; font-size: 1.15rem; line-height: 1.8; color: white !important;">
        "I specialize in <b>Process Digitization</b>. While many analysts only report on data, I build the 
        <b>Automation Engines</b> that generate it. My unique advantage is taking a messy, manual 
        workflow and re-engineering it into a scalable Python framework that ensures 
        <b>100% Data Integrity</b> before it ever reaches a dashboard."
    </p>
</div>
""", unsafe_allow_html=True)