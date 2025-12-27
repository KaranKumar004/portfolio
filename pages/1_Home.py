import streamlit as st

# Use the accent color defined in your app.py
h_color = "#38bdf8" 

# Global CSS to force ALL Streamlit labels and text to white
st.markdown("""
<style>
    /* Force all standard Streamlit text, labels, and headers to white */
    html, body, [data-testid="stWidgetLabel"], .stText, p, span, label {
        color: white !important;
    }
    h1, h2, h3, h4, h5, h6 {
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    hr {
        border-color: rgba(255,255,255,0.2) !important;
    }
</style>
""", unsafe_allow_html=True)

# ---------- HERO SECTION ----------
st.markdown(f"""
    <div style="text-align:center; padding: 60px 0;">
        <h1 style="font-size: 4.5rem; background: linear-gradient(to right, {h_color}, #FFFFFF); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom:0;">
            Karan Kumar S
        </h1>
        <p style="font-size:1.8rem; color: white !important; font-weight:400;">Data Analyst & Automation Architect</p>
        <div style="margin-top:25px; display: flex; justify-content: center; gap: 10px;">
            <span style="background:rgba(56, 189, 248, 0.1); padding:8px 20px; border-radius:50px; font-size:0.9rem; border:1px solid {h_color}; color:{h_color} !important; font-weight:bold;">🐍 Python Expert</span>
            <span style="background:rgba(147, 51, 234, 0.1); padding:8px 20px; border-radius:50px; font-size:0.9rem; border:1px solid #9333ea; color:#9333ea !important; font-weight:bold;">📊 R Statistician</span>
            <span style="background:rgba(255, 255, 255, 0.05); padding:8px 20px; border-radius:50px; font-size:0.9rem; border:1px solid white; color: white !important; font-weight:bold;">🤖 ML Engineer</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# ---------- IMPACT METRICS ----------
# We use markdown for the header to avoid the default grey st.write color
st.markdown("<h3 style='color: white !important;'>⚡ Business ROI & Impact</h3>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

def glass_metric(label, value, icon, description):
    return f"""
    <div class="glass-card" style="text-align:center; height:180px; display:flex; flex-direction:column; justify-content:center; color: white !important; background: rgba(0,0,0,0.3); border-radius: 15px; border: 1px solid rgba(255,255,255,0.1);">
        <div style="font-size:1.8rem; margin-bottom:5px;">{icon}</div>
        <div style="font-size:2.2rem; font-weight:800; color:{h_color} !important;">{value}</div>
        <div style="font-size:0.8rem; font-weight:700; text-transform:uppercase; letter-spacing:1px; margin-bottom:5px; color: white !important;">{label}</div>
        <div style="font-size:0.75rem; color: white !important; opacity: 1 !important;">{description}</div>
    </div>
    """

col1.markdown(glass_metric("Throughput", "5K+", "📂", "Daily records processed"), unsafe_allow_html=True)
col2.markdown(glass_metric("Precision", "80%", "❌", "Reduction in human error"), unsafe_allow_html=True)
col3.markdown(glass_metric("Efficiency", "60%", "⏱", "Time saved via automation"), unsafe_allow_html=True)
col4.markdown(glass_metric("Deployment", "4+", "🤖", "Live ML Algorithms"), unsafe_allow_html=True)

st.markdown("---")

# ---------- LIVE TERMINAL ----------
st.markdown("<h3 style='color: white !important;'>💻 Current Environment</h3>", unsafe_allow_html=True)

terminal_html = f"""
<div style="background: #1e1e1e; border-radius: 15px; padding: 25px; font-family: 'Courier New', Courier, monospace; border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 20px 50px rgba(0,0,0,0.5);">
    <div style="display: flex; gap: 8px; margin-bottom: 15px;">
        <div style="width:12px; height:12px; background:#ff5f56; border-radius:50%;"></div>
        <div style="width:12px; height:12px; background:#ffbd2e; border-radius:50%;"></div>
        <div style="width:12px; height:12px; background:#27c93f; border-radius:50%;"></div>
    </div>
    <div style="color: white !important; font-size: 0.95rem; line-height: 1.6;">
        <span style="color: #569cd6;">import</span> karan_kumar <span style="color: #569cd6;">as</span> dev<br><br>
        <span style="color: #6a9955;"># Initializing Genpact workflow automation...</span><br>
        >>> dev.status()<br>
        <span style="color: #ce9178;">"Active: Transforming manual data into automated intelligence."</span><br><br>
        <span style="color: #6a9955;"># Core Competencies</span><br>
        >>> dev.get_skills()<br>
        [<span style="color: #ce9178;">'PredictiveModeling'</span>, <span style="color: #ce9178;">'RuleBasedQC'</span>, <span style="color: #ce9178;">'StatisticalInference'</span>]<br><br>
        <span style="color: #6a9955;"># Current Focus</span><br>
        >>> dev.current_goal()<br>
        <span style="color: #ce9178;">"Optimizing R/Python pipelines for 100% data integrity."</span>
    </div>
</div>
"""
st.markdown(terminal_html, unsafe_allow_html=True)

st.markdown("---")

# ---------- STRATEGIC EXPERTISE ----------
st.markdown("<h3 style='color: white !important;'>🧠 Strategic Expertise</h3>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)

def expertise_card(title, text, icon):
    return f"""
    <div style="height:250px; color: white !important; background: rgba(0,0,0,0.4); padding: 25px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1);">
        <h4 style="color:{h_color} !important; margin-bottom:15px;">{icon} {title}</h4>
        <p style="font-size:0.95rem; color: white !important; opacity: 1 !important; line-height: 1.5;">{text}</p>
    </div>
    """

with c1:
    st.markdown(expertise_card("Automation", "Migrating legacy VBA Macros to scalable Python frameworks. I build robust scripts that handle multi-sheet validations.", "🐍"), unsafe_allow_html=True)

with c2:
    st.markdown(expertise_card("Statistics (R)", "Deep-dive EDA using R Stats. My focus is on Hypothesis Testing and Patent Analysis to uncover trends.", "📈"), unsafe_allow_html=True)

with c3:
    st.markdown(expertise_card("Machine Learning", "Deploying Random Forest and Linear Regression models. I optimize them for business interpretability.", "🤖"), unsafe_allow_html=True)

# ---------- CALL TO ACTION ----------
st.markdown(f"""
<div style="text-align:center; padding: 40px; background: rgba(56, 189, 248, 0.05); border-radius: 24px; border: 1px dashed {h_color}; margin-top: 40px;">
    <h3 style="margin:0; color: white !important;">Ready to transform your data workflows?</h3>
    <p style="color: white !important; opacity: 1 !important; margin-top: 10px;">Explore my technical documentation or reach out for a collaboration.</p>
</div>
""", unsafe_allow_html=True)