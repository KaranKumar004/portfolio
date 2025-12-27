import streamlit as st

# Note: Remove st.set_page_config if this is called via exec() in app.py
# st.set_page_config(page_title="Projects | Karan Kumar", layout="wide")

# Theme-aware accent
accent = "#38bdf8" 

st.markdown(f"""
<style>
    /* Global Force: No Grey Fonts */
    html, body, [data-testid="stWidgetLabel"], p, span, h1, h2, h3, h4 {{
        color: white !important;
        opacity: 1 !important;
    }}
    
    .project-card {{
        background: rgba(0, 0, 0, 0.65); /* Darker for high contrast */
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 20px;
        padding: 30px;
        transition: all 0.3s ease;
        height: 100%;
        display: flex;
        flex-direction: column;
    }}
    .project-card:hover {{
        transform: translateY(-5px);
        border: 1px solid {accent};
        box-shadow: 0 10px 30px rgba(56, 189, 248, 0.2);
    }}
    .tech-pill {{
        display: inline-block;
        background: rgba(56, 189, 248, 0.15);
        color: {accent} !important;
        padding: 4px 12px;
        border-radius: 50px;
        font-size: 0.8rem;
        margin-right: 8px;
        margin-top: 15px;
        border: 1px solid {accent};
        font-weight: 600;
    }}
    .impact-text {{
        color: #00ff9d !important; /* Bright Neon Green for visibility */
        font-weight: 700;
        font-size: 0.95rem;
        margin-top: 10px;
        text-shadow: 0 0 10px rgba(0, 255, 157, 0.3);
    }}
    hr {{ border-color: rgba(255,255,255,0.2) !important; }}
</style>
""", unsafe_allow_html=True)

st.title("🚀 Strategic Projects")
st.markdown("<p style='font-size:1.2rem;'>A showcase of automation engines built for Genpact and analytical models developed for business intelligence.</p>", unsafe_allow_html=True)

# --- 1. ENTERPRISE AUTOMATION ---
st.markdown("<h2 style='margin-top:40px;'>🏢 Enterprise Automation (Genpact)</h2>", unsafe_allow_html=True)
c1, c2 = st.columns(2)

with c1:
    st.markdown(f"""
    <div class="project-card">
        <div>
            <h3 style="color:{accent} !important;">⚙️ Python QC Engine</h3>
            <p style="line-height:1.6;">Designed and deployed an end-to-end <b>Excel validation engine</b> that automates complex data auditing. 
            Previously, teams spent hours manually cross-referencing sheets; this engine performs logical checks, identifies anomalies, and generates 
            automated status reports in seconds.</p>
            <p class="impact-text">🏆 Result: 5k+ records/day | 80% Error Reduction | 60% Faster TAT</p>
        </div>
        <div>
            <span class="tech-pill">Python</span><span class="tech-pill">Pandas</span><span class="tech-pill">OpenPyXL</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="project-card">
        <div>
            <h3 style="color:{accent} !important;">🏢 UNIFY Reporting Suite</h3>
            <p style="line-height:1.6;">Developed a suite of automated checkout tools using <b>Genius Scripting</b> within the UNIFY platform. 
            The system validates report completeness and data integrity before final submission, ensuring high-stakes financial data meets 
            Genpact’s rigorous quality standards.</p>
            <p class="impact-text">⭐ Awarded: Genpact Cheers Recognition Award</p>
        </div>
        <div>
            <span class="tech-pill">UNIFY</span><span class="tech-pill">Genius Script</span><span class="tech-pill">Excel Automation</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- 2. MACHINE LEARNING ---
st.markdown("<h2>🤖 Machine Learning & Research</h2>", unsafe_allow_html=True)
c3, c4, c5 = st.columns(3)

with c3:
    st.markdown(f"""
    <div class="project-card">
        <div>
            <h4>📈 Price Prediction</h4>
            <p style="font-size:0.9rem; line-height:1.5;">Built a <b>Linear Regression</b> model to estimate market values. By cleaning 
            outliers and performing feature scaling on engine size and mileage, the model provides actionable valuation insights.</p>
        </div>
        <div>
            <span class="tech-pill">Scikit-Learn</span><span class="tech-pill">Regression</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="project-card">
        <div>
            <h4>📉 Telecom Churn Analysis</h4>
            <p style="font-size:0.9rem; line-height:1.5;">Utilized a <b>Random Forest Classifier</b> to predict customer attrition. I focused on 
            <i>Feature Importance</i> to identify exactly why customers leave, helping businesses prioritize retention strategies.</p>
        </div>
        <div>
            <span class="tech-pill">Random Forest</span><span class="tech-pill">Predictive Modeling</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with c5:
    st.markdown(f"""
    <div class="project-card">
        <div>
            <h4>🔁 VBA to Python Migration</h4>
            <p style="font-size:0.9rem; line-height:1.5;">Architected the migration of legacy <b>Excel VBA macros</b> into modern Python scripts. 
            This reduced file dependency and allowed for integration into cloud-based data pipelines.</p>
        </div>
        <div>
            <span class="tech-pill">Refactoring</span><span class="tech-pill">Architecture</span>
        </div>
    </div>
    """, unsafe_allow_html=True)