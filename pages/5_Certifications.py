import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="Certifications | Karan Kumar", layout="wide")

# Custom Glassmorphism for the certificate cards
st.markdown("""
<style>
    .cert-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        text-align: center;
    }
    .cert-title {
        font-weight: 600;
        color: #00d2ff;
        margin-bottom: 15px;
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>
""", unsafe_allow_html=True)

st.title("🏆 Professional Credentials")
st.write("A verified track record of my expertise in Data Analytics, Machine Learning, and Lean Process Optimization.")

CERT_PATH = Path("assets/certificates")
pdf_files = list(CERT_PATH.glob("*.pdf"))

def get_pdf_display(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
    return f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600px" style="border-radius:10px;"></iframe>'

if not pdf_files:
    st.warning("No certificates found. Please add PDF files to `assets/certificates/`.")
else:
    # Use columns for a grid layout
    cols = st.columns(3, gap="large")
    
    for idx, pdf in enumerate(pdf_files):
        with cols[idx % 3]:
            # Clean up the filename for the display title
            clean_title = pdf.stem.replace("_", " ").replace("-", " ").title()
            
            # Create a glass card container
            st.markdown(f'<div class="cert-card">', unsafe_allow_html=True)
            st.markdown(f'<div class="cert-title">📄 {clean_title}</div>', unsafe_allow_html=True)
            
            # Interaction: View via Expander (saves memory and space)
            with st.expander("👁️ Quick View"):
                st.markdown(get_pdf_display(pdf), unsafe_allow_html=True)
            
            # Interaction: Download
            with open(pdf, "rb") as f:
                st.download_button(
                    label="⬇️ Download PDF",
                    data=f,
                    file_name=pdf.name,
                    mime="application/pdf",
                    key=f"dl_{idx}",
                    use_container_width=True
                )
            st.markdown('</div>', unsafe_allow_html=True)

# --- VALUE ADDED CONTENT ---
st.write("---")
st.markdown("""
<div style="background: rgba(16, 185, 129, 0.1); padding: 20px; border-radius: 15px; border: 1px solid #10b981;">
    <h4 style="color: #10b981; margin-top:0;">🌟 Highlight: Lean 1 Star Certification</h4>
    <p style="margin-bottom:0;">This certification reflects my commitment to <b>Process Excellence</b>. 
    I apply Lean methodologies to my data workflows to ensure that automation is not just fast, 
    but eliminates waste and maximizes business value.</p>
</div>
""", unsafe_allow_html=True)