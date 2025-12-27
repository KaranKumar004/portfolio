import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# Note: Remove set_page_config if this is loaded via exec() in app.py
# st.set_page_config(page_title="Analytics Lab | Karan Kumar", layout="wide")

# Theme-aware accent
accent = "#38bdf8" 

# --- MASTER CSS FOR ZERO GREY ---
st.markdown(f"""
<style>
    /* Force all base text to white */
    html, body, [data-testid="stWidgetLabel"], .stText, p, span, label, li, ol, ul {{
        color: white !important;
        opacity: 1 !important;
    }}
    
    h1, h2, h3, h4, h5, h6 {{
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
    }}

    .algo-card {{
        background: rgba(0, 0, 0, 0.6);
        border-left: 5px solid {accent};
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 20px;
        color: white !important;
        border: 1px solid rgba(255,255,255,0.1);
    }}

    .logic-box {{
        background: rgba(56, 189, 248, 0.1);
        padding: 15px;
        border-radius: 10px;
        border: 1px dashed {accent};
        color: white !important;
    }}

    .glass-card {{
        background: rgba(0, 0, 0, 0.6);
        padding: 25px;
        border-radius: 15px;
        color: white !important;
        height: 100%;
        border: 1px solid rgba(255,255,255,0.1);
    }}
    
    /* Fix for slider labels */
    div[data-testid="stThumbValue"], div[data-testid="stTickBarMin"], div[data-testid="stTickBarMax"] {{
        color: white !important;
    }}
</style>
""", unsafe_allow_html=True)

st.title("🤖 The Analytics Lab")
st.markdown("<p style='font-size:1.2rem;'>Explaining the 'Why' behind the 'How'. This section explores the mathematical logic and statistical rigor I apply to data.</p>", unsafe_allow_html=True)

# --- SECTION 1: THE ML PHILOSOPHY ---
st.markdown(f"""
<div class="algo-card">
    <h3 style="margin-top:0;">🧠 My Methodology: The Three Pillars</h3>
    <p>I follow a disciplined approach to every data problem:</p>
    <ol style="line-height:1.8;">
        <li><b>Statistical Foundation:</b> Understanding distributions and outliers via R.</li>
        <li><b>Algorithm Selection:</b> Choosing models based on <i>Interpretability</i> vs. <i>Complexity</i>.</li>
        <li><b>Automated Pipeline:</b> Deploying the solution using Python for real-world business use.</li>
    </ol>
</div>
""", unsafe_allow_html=True)

# --- SECTION 2: INTERACTIVE ML DEMO ---
st.markdown("<hr style='border-color: rgba(255,255,255,0.2);'>", unsafe_allow_html=True)
st.markdown("<h2 style='color: white !important;'>🧪 Live Lab: Linear Regression Simulator</h2>", unsafe_allow_html=True)
st.markdown("<p>Adjust the parameters to see how a Regression model fits noisy data.</p>", unsafe_allow_html=True)

col_sim1, col_sim2 = st.columns([1, 2])

with col_sim1:
    st.markdown("<b style='font-size:1.1rem;'>Model Parameters</b>", unsafe_allow_html=True)
    noise = st.slider("Data Noise Level", 0, 50, 20)
    n_points = st.slider("Sample Size (N)", 50, 500, 100)
    
    st.markdown(f"""
    <div class="logic-box" style="margin-top:20px;">
        <b style="color:{accent};">Algorithm Insight:</b><br>
        Linear Regression is my go-to for <b>Price Prediction</b> because it provides clear feature coefficients (e.g., 'For every 1km increase in mileage, price drops by $X').
    </div>
    """, unsafe_allow_html=True)

with col_sim2:
    # Generate dummy data
    x = np.linspace(0, 10, n_points)
    y = 2.5 * x + np.random.normal(0, noise, n_points)
    df = pd.DataFrame({'X': x, 'Y': y})
    
    
    fig = px.scatter(df, x='X', y='Y', trendline="ols", 
                     title="Linear Fit Analysis",
                     template="plotly_dark",
                     color_discrete_sequence=[accent])
    
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

# --- SECTION 3: R VS PYTHON (THE DUALITY) ---
st.markdown("<hr style='border-color: rgba(255,255,255,0.2);'>", unsafe_allow_html=True)
st.markdown("<h2 style='color: white !important;'>📊 The Tech Duality: When I use what?</h2>", unsafe_allow_html=True)

r_col, py_col = st.columns(2)

with r_col:
    st.markdown(f"""
    <div class="glass-card" style="border-top: 4px solid #276BBE;">
        <h4 style="color:#276BBE !important;">📈 R for Statistical Deep-Dives</h4>
        <p>I utilize <b>R (Tidyverse, ggplot2, lm)</b> for exploratory research where precision matters more than speed.</p>
        <ul style="line-height:1.6;">
            <li><b>Hypothesis Testing:</b> Checking if process changes are statistically significant.</li>
            <li><b>Patent Analysis:</b> I used R to identify trends in Seattle University patent datasets, leveraging R's superior handling of complex data frames.</li>
            <li><b>Visualization:</b> Creating publication-quality graphs for executive reports.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with py_col:
    st.markdown(f"""
    <div class="glass-card" style="border-top: 4px solid #FFD43B;">
        <h4 style="color:#FFD43B !important;">🐍 Python for Production & Automation</h4>
        <p>I use <b>Python (Scikit-learn, Pandas)</b> when the goal is to build a tool that works independently.</p>
        <ul style="line-height:1.6;">
            <li><b>End-to-End Pipelines:</b> Automating QC from raw Excel to final SQL database.</li>
            <li><b>Random Forest:</b> My preference for <b>Telecom Churn</b> because it captures non-linear relationships.</li>
            <li><b>Scalability:</b> Integrating models into Streamlit apps or UNIFY platforms.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- FINAL SECTION: PATENT ANALYSIS HIGHLIGHT ---
st.markdown("<hr style='border-color: rgba(255,255,255,0.2);'>", unsafe_allow_html=True)
st.markdown(f"""
<div class="algo-card" style="text-align:center;">
    <h3 style="color:{accent} !important;">🔎 Case Study: Patent Dataset EDA</h3>
    <p style="max-width:800px; margin: 0 auto;">Using R, I performed a deep-dive into patent data to identify innovation clusters. By applying <b>K-Means Clustering</b>, 
    we were able to segment technological categories based on filing frequency and keyword density, uncovering hidden trends in IP growth.</p>
</div>
""", unsafe_allow_html=True)