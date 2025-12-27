import streamlit as st

# Use session state theme for dynamic highlighting
# We use bright cyan for dark backgrounds to ensure it cuts through the noise
h_color = "#00f2ff" 

st.markdown(f"""
<style>
    /* Global Text Shadow for readability against busy backgrounds */
    .stApp {{
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
    }}

    .fade-in {{
        animation: fadeIn 1.5s ease-in-out;
    }}
    
    @keyframes fadeIn {{
        from {{opacity:0; transform: translateY(20px);}}
        to {{opacity:1; transform: translateY(0);}}
    }}

    .highlight {{
        color: {h_color};
        font-weight: 700;
        text-shadow: 0 0 10px rgba(0, 242, 255, 0.5);
    }}

    /* Increased opacity for glass panels to act as a solid backdrop for text */
    .glass-panel {{
        background: rgba(0, 0, 0, 0.6); /* Darker backdrop for better contrast */
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 24px;
        padding: 40px;
        box-shadow: 0 12px 40px rgba(0,0,0,0.5);
        margin-bottom: 25px;
    }}

    .tag {{
        display: inline-block;
        background: rgba(0, 242, 255, 0.15);
        border: 1px solid {h_color};
        color: {h_color};
        padding: 6px 15px;
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 5px;
        text-shadow: none; /* Tags don't need shadows */
    }}
    
    h1, h2, h3, h4 {{
        color: white !important;
        letter-spacing: 1px;
    }}
</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown(f"""
<div class="fade-in" style="text-align:center; padding: 40px 0;">
    <h1 style="font-size: 4rem; margin-bottom:0;"> About Me</h1>
    <h2 style="font-weight:300;">Decoding Complexity through <span class="highlight">Data & Automation</span></h2>
</div>
""", unsafe_allow_html=True)

# ---------- THE JOURNEY ----------
st.markdown(f"""
<div class="glass-panel fade-in">
    <h3 style="text-align:center; color:{h_color}; margin-top:0;">🚀 My Journey: From Manual to Machine</h3>
    <p style="text-align:center; font-size:1.15rem; max-width:900px; margin: 0 auto; color: #e0e0e0;">
    I am a <b>Data Analyst at Genpact</b> with a mission to eliminate manual bottlenecks. 
    My career took a pivotal turn when I realized that data isn't just for reporting—it's for <b>optimization</b>.
    </p>
    <br>
    <p style="text-align:center; font-size:1.15rem; max-width:900px; margin: 0 auto; color: #e0e0e0;">
    By bridging the gap between <span class="highlight">Statistical Research (R)</span> and 
    <span class="highlight">Production Engineering (Python)</span>, I've helped teams move from 
    reactive firefighting to proactive, automated decision-making.
    </p>
    <br>
    <p style="text-align:center; font-style:italic; opacity:0.9; color: #00f2ff;">"I don't just find the needle in the haystack; I build a magnet to find it automatically."</p>
</div>
""", unsafe_allow_html=True)

# ---------- WHAT I WORK ON ----------
st.write("### 🛠️ Strategic Focus")
pill_col1, pill_col2, pill_col3 = st.columns(3)

def pillar_card(title, desc, icon):
    return f"""
    <div class="glass-panel" style="text-align:center; height:240px; padding: 25px;">
        <div style="font-size:2rem; margin-bottom:10px;">{icon}</div>
        <h4 style="color:{h_color}; margin-bottom:15px;">{title}</h4>
        <p style="font-size:0.95rem; line-height:1.5; color: #d1d1d1;">{desc}</p>
    </div>
    """

pill_col1.markdown(pillar_card("Automation", "Building Python pipelines that replace hours of manual QC with seconds of code.", "🐍"), unsafe_allow_html=True)
pill_col2.markdown(pillar_card("Intelligence", "Applying Regression and Random Forest to turn historical noise into future predictions.", "🤖"), unsafe_allow_html=True)
pill_col3.markdown(pillar_card("Statistics", "Leveraging R for deep EDA and hypothesis testing to ensure data integrity.", "📊"), unsafe_allow_html=True)

# ---------- INTEREST TAGS ----------
tags = ["Data Analytics", "Machine Learning", "Predictive Modeling", "Python", "R Language", "VBA Migration", "QC Automation", "SQL", "Feature Engineering"]
tag_html = "".join([f'<span class="tag">{t}</span>' for t in tags])

st.markdown(f"""
<div class="fade-in" style="text-align:center; padding: 30px 0;">
    {tag_html}
</div>
""", unsafe_allow_html=True)