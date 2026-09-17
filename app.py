import os
import base64
from io import BytesIO
from textwrap import wrap

import streamlit as st
import pandas as pd
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# ==========================================
# 1. KONFIGURASI HALAMAN WEB
# ==========================================
st.set_page_config(
    page_title="Muh Irham A Ilyas | Data Analyst Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. CACHING FUNGSI PEMBACA GAMBAR (ANTI-LAG)
# ==========================================
@st.cache_data
def get_base64_img(img_path):
    if os.path.exists(img_path):
        with open(img_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@st.cache_data
def build_project_pdf(title, category, description, tools):
    pdf_buffer = BytesIO()
    document = canvas.Canvas(pdf_buffer, pagesize=A4)
    page_width, page_height = A4

    document.setFillColor(HexColor("#1f1915"))
    document.rect(0, page_height - 120, page_width, 120, fill=1, stroke=0)
    document.setFillColor(HexColor("#f8f2ea"))
    document.setFont("Helvetica-Bold", 22)
    document.drawString(48, page_height - 62, "Project Portfolio")
    document.setFont("Helvetica", 10)
    document.drawString(48, page_height - 84, "Muh Irham A Ilyas | Data Analyst")

    document.setFillColor(HexColor("#1f1915"))
    document.setFont("Helvetica-Bold", 18)
    title_lines = wrap(title, width=46)
    y_position = page_height - 170
    for line in title_lines:
        document.drawString(48, y_position, line)
        y_position -= 24

    document.setFillColor(HexColor("#7f5a45"))
    document.setFont("Helvetica-Bold", 10)
    document.drawString(48, y_position - 4, category.upper())
    y_position -= 40

    document.setFillColor(HexColor("#3d2f28"))
    document.setFont("Helvetica-Bold", 11)
    document.drawString(48, y_position, "Project overview")
    y_position -= 22
    document.setFont("Helvetica", 10.5)
    for line in wrap(description, width=88):
        document.drawString(48, y_position, line)
        y_position -= 17

    y_position -= 18
    document.setFont("Helvetica-Bold", 11)
    document.drawString(48, y_position, "Tools and skills")
    y_position -= 22
    document.setFont("Helvetica", 10.5)
    for line in wrap(tools, width=88):
        document.drawString(48, y_position, line)
        y_position -= 17

    document.setStrokeColor(HexColor("#c9ab8d"))
    document.line(48, 72, page_width - 48, 72)
    document.setFillColor(HexColor("#5f5048"))
    document.setFont("Helvetica", 9)
    document.drawString(48, 52, "Contact: muhirham.ilyas@gmail.com")
    document.drawRightString(page_width - 48, 52, "linkedin.com/in/muh-irham-a-ilyas-372651307")

    document.save()
    return pdf_buffer.getvalue()

# ==========================================
# 3. CSS GLOBAL TERPUSAT (HANYA 1X DI SINI)
# ==========================================
st.markdown("""
    <style>
    :root {
        --bg-cream-1: #f5efe7;
        --bg-cream-2: #efe5d8;
        --panel-cream: rgba(255,255,255,0.52);
        --panel-cream-strong: #f8f2ea;
        --brown-900: #1f1915;
        --brown-700: #3d2f28;
        --brown-600: #5c4335;
        --brown-500: #7f5a45;
        --brown-300: #c9ab8d;
        --gold-300: #d8b98a;
        --gold-500: #b99154;
        --sage-700: #566153;
        --sage-400: #87927b;
        --terracotta-500: #b86f52;
        --terracotta-300: #d39a7d;
        --gray-900: #34312e;
        --gray-700: #6f6b64;
        --gray-500: #a9a39a;
        --gray-200: #e4dfd7;
        --text-main: #2a211c;
        --text-soft: #625d56;
        --line-soft: rgba(111,107,100,0.25);
        --shadow-soft: rgba(31,25,21,0.12);
    }

    html, body, [class*="css"], .stApp {
        font-family: "Segoe UI", "Inter", -apple-system, sans-serif !important;
        background: linear-gradient(180deg, var(--bg-cream-1) 0%, var(--bg-cream-2) 100%) !important;
        color: var(--text-main) !important;
    }

    .stApp {
        background-image:
            radial-gradient(circle at top left, rgba(135,146,123,0.16), transparent 26%),
            radial-gradient(circle at 92% 22%, rgba(184,111,82,0.10), transparent 24%),
            radial-gradient(circle at 8% 88%, rgba(169,163,154,0.13), transparent 22%),
            radial-gradient(circle at bottom right, rgba(31,25,21,0.06), transparent 35%),
            linear-gradient(180deg, var(--bg-cream-1) 0%, var(--bg-cream-2) 100%);
        animation: fadeInPage 0.45s ease-out;
    }

    html { scroll-behavior: smooth; }

    @keyframes fadeInPage {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes fadeUp {
        from {
            opacity: 0;
            transform: translateY(18px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes floatSoft {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-6px); }
    }

    @media (prefers-reduced-motion: reduce) {
        *, *::before, *::after {
            animation-duration: 0.01ms !important;
            animation-iteration-count: 1 !important;
            transition-duration: 0.01ms !important;
            scroll-behavior: auto !important;
        }
    }

    h1, h2, h3, h4, h5, h6,
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: var(--brown-900) !important;
        font-weight: 800 !important;
        letter-spacing: -0.05em !important;
        margin-top: 12px !important;
        margin-bottom: 12px !important;
    }

    h1, .stMarkdown h1 { font-size: 2.7rem !important; line-height: 1.08 !important; }
    h2, .stMarkdown h2 { font-size: 1.9rem !important; border-bottom: 2px solid rgba(92,67,53,0.55); padding-bottom: 8px; }
    h3, .stMarkdown h3 { font-size: 1.4rem !important; }

    p, li, div, label {
        color: var(--text-soft) !important;
        font-size: 1rem !important;
        line-height: 1.72 !important;
    }

    .section-header {
        font-size: 1.9rem;
        font-weight: 800;
        color: var(--brown-900);
        border-bottom: 2px solid var(--terracotta-500);
        padding-bottom: 10px;
        margin: 28px 0 24px 0;
        letter-spacing: -0.04em;
        animation: fadeUp 0.7s ease both;
    }

    .nav-shell {
        background: rgba(255,255,255,0.5);
        border: 1px solid var(--line-soft);
        border-radius: 10px;
        padding: 10px 12px;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        box-shadow: 0 14px 32px rgba(31,25,21,0.05);
        margin-bottom: 20px;
        position: sticky;
        top: 12px;
        z-index: 50;
    }

    .hello-text {
        display: inline-block;
        background: rgba(135,146,123,0.16);
        border: 1px solid rgba(86,97,83,0.25);
        color: var(--sage-700);
        font-weight: 800;
        letter-spacing: 0.14em;
        font-size: 0.72rem;
        padding: 8px 14px;
        border-radius: 999px;
        margin-bottom: 16px;
        text-transform: uppercase;
    }

    .hero-title {
        font-size: clamp(2.4rem, 5vw, 4.2rem);
        font-weight: 900;
        line-height: 1.02;
        margin-bottom: 18px;
        letter-spacing: -0.07em;
    }
    .hero-title span {
        color: var(--terracotta-500);
        text-shadow: 0 4px 18px rgba(184,111,82,0.16);
    }

    .hero-desc {
        color: var(--text-soft);
        font-size: 1.08rem;
        line-height: 1.8;
        margin-bottom: 26px;
        max-width: 720px;
    }

    .hero-card {
        background: linear-gradient(135deg, rgba(86,97,83,0.98), rgba(61,47,40,0.98));
        border-radius: 26px;
        padding: 28px 26px;
        box-shadow: 0 18px 40px rgba(31,25,21,0.12);
        margin-top: 18px;
        margin-bottom: 22px;
        position: relative;
        overflow: hidden;
        animation: fadeUp 0.8s ease both;
    }
    .hero-card::before {
        content: "";
        position: absolute;
        inset: -20% auto auto -10%;
        width: 200px;
        height: 200px;
        background: rgba(255,255,255,0.08);
        border-radius: 50%;
        filter: blur(12px);
    }
    .hero-card h3 {
        color: #f7efe6 !important;
        margin-top: 0 !important;
        margin-bottom: 10px !important;
    }
    .hero-card p {
        color: #eee3d6 !important;
        margin: 0 !important;
    }

    .stat-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 16px;
        margin-top: 18px;
    }

    .stat-pill {
        background: rgba(228,223,215,0.44);
        border: 1px solid var(--line-soft);
        border-radius: 18px;
        padding: 18px 16px;
        box-shadow: 0 8px 28px rgba(31,25,21,0.04);
        animation: fadeUp 0.75s ease both;
    }
    .stat-pill:nth-child(2) { border-top: 3px solid var(--terracotta-500); }
    .stat-pill:nth-child(3) { border-top: 3px solid var(--sage-400); }
    .stat-pill strong {
        display: block;
        font-size: 1.7rem;
        color: var(--brown-900);
        margin-bottom: 6px;
        letter-spacing: -0.06em;
    }
    .stat-pill span {
        color: var(--brown-600);
        font-size: 0.78rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.09em;
    }

    .olive-card {
        background: linear-gradient(135deg, var(--terracotta-500) 0%, var(--brown-700) 100%);
        color: #fff !important;
        padding: 30px 32px;
        border-radius: 12px;
        margin: 24px 0;
        box-shadow: 0 18px 36px rgba(61,47,40,0.18);
        animation: fadeUp 0.8s ease both;
    }
    .olive-card h3 { color: #fff !important; border: none !important; margin-top: 0 !important; }
    .olive-card p { color: #f1e5dc !important; margin: 0 !important; }

    .custom-card {
        background: rgba(255,255,255,0.58);
        border: 1px solid var(--line-soft);
        padding: 22px 20px;
        border-radius: 10px;
        margin-bottom: 18px;
        box-shadow: 0 10px 25px rgba(31,25,21,0.03);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        animation: fadeUp 0.8s ease both;
        position: relative;
        overflow: hidden;
    }
    .custom-card::before {
        content: "";
        position: absolute;
        inset: 0 auto 0 0;
        width: 3px;
        background: var(--sage-400);
        opacity: 0.65;
    }
    .custom-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 16px 28px rgba(31,25,21,0.06);
    }

    .card-list {
        color: var(--gray-700) !important;
        font-size: 0.96rem !important;
        line-height: 1.6;
        margin: 0;
    }

    .custom-card h3,
    .custom-card h4 {
        color: var(--gray-900) !important;
    }

    .custom-card p,
    .custom-card li {
        color: var(--gray-700) !important;
    }

    .stat-pill strong {
        color: var(--gray-900) !important;
    }

    .stat-pill span,
    .skill-tag {
        color: var(--brown-700) !important;
    }

    [data-testid="stCaptionContainer"] p {
        color: var(--gray-700) !important;
    }

    .featured-card {
        border-left: 5px solid var(--terracotta-500) !important;
        background: rgba(255,255,255,0.64);
    }

    .company-logo-card {
        background: rgba(228,223,215,0.48);
        border: 1px solid var(--line-soft);
        border-radius: 10px;
        padding: 16px;
        text-align: center;
        margin-bottom: 15px;
        box-shadow: 0 10px 25px rgba(31,25,21,0.03);
    }

    .badge-featured {
        background: linear-gradient(135deg, var(--terracotta-500), var(--brown-700));
        color: #fff !important;
        padding: 5px 12px;
        border-radius: 999px;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.04em;
        text-transform: uppercase;
    }

    .badge-category {
        background: var(--gray-900);
        color: #f8f2ea !important;
        padding: 5px 12px;
        border-radius: 999px;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.04em;
        text-transform: uppercase;
    }

    .skill-tag-group {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 14px;
    }
    .skill-tag {
        background: rgba(127,90,69,0.08);
        border: 1px solid rgba(127,90,69,0.16);
        color: var(--brown-900);
        padding: 6px 12px;
        border-radius: 999px;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.02em;
    }

    .card-header-flex {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 12px;
        gap: 12px;
    }
    .card-header-flex h3 {
        color: var(--brown-900) !important;
        margin: 0 !important;
        border: none !important;
    }
    .icons-group {
        display: flex;
        gap: 8px;
        align-items: center;
        flex-wrap: wrap;
    }

    .skill-progress-bg {
        background: rgba(92,67,53,0.12);
        border-radius: 999px;
        height: 9px;
        margin: 12px 0 12px 0;
        overflow: hidden;
    }
    .skill-progress {
        background: linear-gradient(90deg, var(--sage-700) 0%, var(--gold-500) 100%);
        height: 9px;
        border-radius: 999px;
        box-shadow: 0 6px 16px rgba(127,90,69,0.22);
    }

    .profile-frame {
        width: 280px;
        max-width: 100%;
        height: auto;
        border-radius: 30% 30% 18% 18%;
        border: 3px solid rgba(127,90,69,0.2);
        box-shadow: 0 18px 30px rgba(31,25,21,0.12);
        animation: floatSoft 4s ease-in-out infinite;
    }

    div[data-testid="stButton"] > button,
    div[data-testid="stDownloadButton"] > button {
        background: linear-gradient(135deg, var(--brown-900) 0%, var(--terracotta-500) 100%) !important;
        color: var(--panel-cream-strong) !important;
        border-radius: 999px !important;
        font-weight: 700 !important;
        padding: 12px 18px !important;
        font-size: 0.88rem !important;
        border: none !important;
        transition: transform 0.2s ease, box-shadow 0.2s ease !important;
        width: 100% !important;
        box-shadow: 0 10px 20px rgba(31,25,21,0.12) !important;
    }

    div[data-testid="stButton"] > button p,
    div[data-testid="stButton"] > button span,
    div[data-testid="stDownloadButton"] > button p,
    div[data-testid="stDownloadButton"] > button span {
        color: var(--panel-cream-strong) !important;
    }

    div[data-testid="stButton"] > button:hover,
    div[data-testid="stDownloadButton"] > button:hover {
        background: linear-gradient(135deg, var(--sage-700) 0%, var(--brown-700) 100%) !important;
        color: #fff !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 16px 24px rgba(92,67,53,0.18) !important;
    }

    div[data-testid="stButton"] > button:hover p,
    div[data-testid="stButton"] > button:hover span,
    div[data-testid="stDownloadButton"] > button:hover p,
    div[data-testid="stDownloadButton"] > button:hover span {
        color: #fff !important;
    }

    .btn-primary-link {
        display: inline-block;`
        background: linear-gradient(135deg, var(--brown-900) 0%, var(--brown-700) 100%);
        color: #f8f2ea !important;
        padding: 12px 24px;
        border-radius: 999px;
        font-weight: 700;
        text-decoration: none;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        box-shadow: 0 10px 18px rgba(31,25,21,0.12);
    }
    .btn-primary-link:hover {
        background: linear-gradient(135deg, #7f5a45 0%, var(--brown-700) 100%);
        color: #fff !important;
        transform: translateY(-2px);
    }

    .dark-footer {
        background: linear-gradient(135deg, #3d2f28 0%, #1d2a24 100%);
        color: #f8f2ea !important;
        padding: 42px 28px;
        border-radius: 12px 12px 0 0;
        margin-top: 46px;
        text-align: center;
        box-shadow: 0 -8px 26px rgba(0,0,0,0.08);
        position: relative;
        overflow: hidden;
    }
    .dark-footer::before {
        content: "";
        position: absolute;
        inset: auto auto -40px -40px;
        width: 180px;
        height: 180px;
        background: rgba(255,255,255,0.04);
        border-radius: 50%;
    }
    .dark-footer h2 { color: #f8f2ea !important; border: none !important; }
    .dark-footer p { color: #d0bba8 !important; }

    .social-row {
        display: flex;
        gap: 12px;
        flex-wrap: wrap;
        justify-content: center;
        margin-top: 18px;
    }

    .social-pill {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
        color: var(--panel-cream-strong) !important;
        background: var(--brown-700);
        border: 1px solid rgba(248,242,234,0.24);
        border-radius: 999px;
        padding: 10px 18px;
        font-size: 0.82rem;
        font-weight: 700;
        box-shadow: 0 8px 18px rgba(31,25,21,0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .social-pill:hover {
        transform: translateY(-2px);
        color: #fff !important;
        background: var(--terracotta-500);
        border-color: var(--sage-400);
        box-shadow: 0 12px 22px rgba(31,25,21,0.08);
    }

    .contact-shell {
        background: rgba(228,223,215,0.42);
        border: 1px solid var(--line-soft);
        border-radius: 10px;
        padding: 24px;
        box-shadow: 0 16px 34px rgba(31,25,21,0.04);
    }

    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: rgba(255,255,255,0.78) !important;
        border: 1px solid var(--gray-500) !important;
        border-radius: 14px !important;
        color: var(--brown-900) !important;
    }

    .stTextInput > label,
    .stTextArea > label {
        color: var(--brown-900) !important;
        font-weight: 700 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 4. LOGIKA & TOMBOL NAVIGASI INSTAN (ANTI-GLITCH)
# ==========================================
if 'current_page' not in st.session_state:
    st.session_state.current_page = "HOME"

def set_page(page_name):
    st.session_state.current_page = page_name

st.markdown('<div class="nav-shell">', unsafe_allow_html=True)
nav1, nav2, nav3, nav4, nav5, nav6, nav7 = st.columns(7)

with nav1:
    st.button("HOME", use_container_width=True, on_click=set_page, args=("HOME",))
with nav2:
    st.button("ABOUT", use_container_width=True, on_click=set_page, args=("ABOUT",))
with nav3:
    st.button("PORTFOLIO", use_container_width=True, on_click=set_page, args=("PORTFOLIO",))
with nav4:
    st.button("SKILLS", use_container_width=True, on_click=set_page, args=("SKILLS",))
with nav5:
    st.button("PENDIDIKAN", use_container_width=True, on_click=set_page, args=("PENDIDIKAN",))
with nav6:
    st.button("PENGALAMAN", use_container_width=True, on_click=set_page, args=("PENGALAMAN",))
with nav7:
    st.button("CONTACT", use_container_width=True, on_click=set_page, args=("CONTACT",))
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ==========================================
# 5. RENDERING KONTEN UTAMA (WADAH TUNGGAL BERSISIH)
# ==========================================
main_area = st.empty()
page = st.session_state.current_page

with main_area.container():
    # --- HALAMAN HOME ---
    if page == "HOME":
        col1, col2 = st.columns([1.35, 0.65])

        with col1:
            st.markdown("""
                <div>
                    <div class="hello-text">HELLO • WELCOME</div>
                    <div class="hero-title">I'm <span>Muh Irham A Ilyas</span></div>
                    <div class="hero-desc">
                        Saya adalah <b>Data Analyst</b> yang membantu bisnis mengambil keputusan lebih cepat melalui data yang terstruktur, dashboard yang jelas, dan sistem yang mudah dipahami. Saya fokus pada <b>SQL</b>, <b>Python</b>, <b>Power BI</b>, serta <b>Streamlit</b> untuk membangun solusi analisis berbasis kebutuhan operasional.
                    </div>
                    <a href="#" class="btn-primary-link">DOWNLOAD CV</a>
                </div>
            """, unsafe_allow_html=True)

            st.markdown("""
                <div class="stat-grid">
                    <div class="stat-pill">
                        <strong>3+</strong>
                        <span>Years Experience</span>
                    </div>
                    <div class="stat-pill">
                        <strong>15+</strong>
                        <span>Projects</span>
                    </div>
                    <div class="stat-pill">
                        <strong>90%</strong>
                        <span>Data Accuracy</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        with col2:
            img_path = os.path.join(BASE_DIR, "Irham1.png")
            if os.path.exists(img_path):
                st.markdown('<div style="display:flex; justify-content:center;">', unsafe_allow_html=True)
                st.image(img_path, use_container_width=True, output_format="PNG")
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.markdown("""
                    <div class="custom-card" style="text-align:center; padding: 30px; border: 1px dashed rgba(110,107,90,0.45);">
                        <strong>📸 Foto Profil</strong><br>
                        <span>Tambahkan file <b>Irham1.png</b> ke folder project untuk menampilkan foto.</span>
                    </div>
                """, unsafe_allow_html=True)

        st.markdown("""
            <div class="hero-card">
                <h3>Data-driven decisions. Better business outcomes.</h3>
                <p>Berfokus pada pengolahan database relasional, pembersihan data (data wrangling), visualisasi KPI, serta otomatisasi laporan agar keputusan bisnis lebih cepat, relevan, dan terukur.</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="social-row">
                <a class="social-pill" href="https://www.linkedin.com/in/muh-irham-a-ilyas-372651307/" target="_blank" rel="noreferrer">LinkedIn</a>
                <a class="social-pill" href="https://github.com/okyarmadani09-ops/profil-muh-irham-a-ilyas" target="_blank" rel="noreferrer">GitHub</a>
                <a class="social-pill" href="mailto:muhirham.ilyas@gmail.com">Email</a>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<div class='section-header'>Tailored Strategies. Real Results.</div>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("""
                <div class='custom-card'>
                    <h4>🗄️ Database & Query</h4>
                    <p class='card-list'>
                        • SQL (PostgreSQL, MySQL)<br>
                        • DBeaver Management<br>
                        • Data Wrangling & Cleaning<br>
                        • Query Optimization
                    </p>
                </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown("""
                <div class='custom-card'>
                    <h4>⚡ Python Automation</h4>
                    <p class='card-list'>
                        • Python (Pandas, NumPy)<br>
                        • Streamlit Web Apps<br>
                        • Data Pipeline Automation<br>
                        • VS Code Workflow
                    </p>
                </div>
            """, unsafe_allow_html=True)
        with c3:
            st.markdown("""
                <div class='custom-card'>
                    <h4>📊 Business Intelligence</h4>
                    <p class='card-list'>
                        • Power BI Dashboards<br>
                        • Interactive Data Viz<br>
                        • Executive KPI Reporting<br>
                        • Agribusiness Analytics
                    </p>
                </div>
            """, unsafe_allow_html=True)

    # --- HALAMAN ABOUT ---
    elif page == "ABOUT":
        st.markdown('<div class="section-header">Tentang Saya</div>', unsafe_allow_html=True)
        
        st.markdown("""
            <div class="olive-card">
                <h3>Hello! Saya Muh Irham A Ilyas 👋</h3>
                <p>Data Analyst dengan latar belakang spesifik di sektor agribisnis dan peternakan. Saya menjembatani data mentah lapangan dengan pengambilan keputusan strategis melalui query SQL, otomatisasi Python, serta dashboard bisnis interaktif.</p>
            </div>
        """, unsafe_allow_html=True)

        col_ab1, col_ab2 = st.columns(2)

        with col_ab1:
            st.subheader("📌 Fokus & Spesialisasi Utama")
            st.write("• **Database Management & Cleaning:** Mengolah data mentah dari Excel menjadi struktur database relasional menggunakan **SQL (SQLite/PostgreSQL)** dan **DBeaver**.")
            st.write("• **Scripting & Otomatisasi:** Efisiensi alur pemrosesan data (*data pipeline*) berbasis **Python (Pandas)**.")
            st.write("• **Executive Business Intelligence:** Merancang visualisasi KPI dan tren bisnis menggunakan **Power BI** dan **Streamlit**.")
            st.write("• **Domain Expertise:** Pemahaman mendalam terkait operasional peternakan, perikanan, serta recording data industri agribisnis.")

        with col_ab2:
            st.subheader("💡 Pendekatan Kerja")
            st.markdown("**1. Terstruktur & Presisi**")
            st.caption("Setiap data diolah dengan standar pembersihan data (*data wrangling*) yang ketat untuk menjamin akurasi laporan.")
            st.markdown("**2. Berorientasi Solusi Bisnis**")
            st.caption("Fokus tidak hanya pada data visual, tetapi pada rekomendasi konkret yang mempercepat pengambilan keputusan manajerial.")
            st.markdown("**3. Adaptif & Pembelajar Cepat**")
            st.caption("Aktif meningkatkan kapabilitas analitis baik dari studi akademik S1 Peternakan Universitas Bosowa maupun praktik proyek industri.")

        st.divider()
        st.write("**Domain & Technical Highlights:** `SQL / DBeaver` • `Python / Pandas` • `Power BI` • `Excel Query` • `Livestock & Aquaculture Analytics` • `Digital Administration` caps")

    # --- HALAMAN SKILLS ---
    elif page == "SKILLS":
        st.markdown('<div class="section-header">Tingkat Keahlian & Tools</div>', unsafe_allow_html=True)
        
        col_s1, col_s2 = st.columns(2)
        
        with col_s1:
            st.markdown("""
                <div class="custom-card">
                    <div class="card-header-flex">
                        <h3>🗄️ SQLite & Query</h3>
                        <div class="icons-group">
                            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" width="28" height="28" title="SQLite">
                            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" width="28" height="28" title="PostgreSQL">
                        </div>
                    </div>
                    <p class="card-list">
                        Penguasaan manipulasi database relasional, pembersihan data mentah, serta ekstraksi informasi presisi.
                    </p>
                    <div style="margin: 10px 0 6px 0;"><b>Tingkat Penguasaan</b> &bull; 85%</div>
                    <div class="skill-progress-bg">
                        <div class="skill-progress" style="width: 85%;"></div>
                    </div>
                    <div class="skill-tag-group">
                        <span class="skill-tag">SQLite</span>
                        <span class="skill-tag">DBeaver</span>
                        <span class="skill-tag">Data Cleaning</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        with col_s2:
            st.markdown("""
                <div class="custom-card">
                    <div class="card-header-flex">
                        <h3>⚡ Python, Pandas & Streamlit</h3>
                        <div class="icons-group">
                            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="28" height="28" title="Python">
                            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width="28" height="28" title="Pandas">
                            <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/streamlit.svg" width="26" height="26" class="icon-olive" title="Streamlit">
                        </div>
                    </div>
                    <p class="card-list">
                        Pengembangan skrip otomatisasi olah data, manipulasi dataset berukuran besar, dan aplikasi web interaktif.
                    </p>
                    <div style="margin: 10px 0 6px 0;"><b>Tingkat Penguasaan</b> &bull; 80%</div>
                    <div class="skill-progress-bg">
                        <div class="skill-progress" style="width: 80%;"></div>
                    </div>
                    <div class="skill-tag-group">
                        <span class="skill-tag">Python</span>
                        <span class="skill-tag">Pandas</span>
                        <span class="skill-tag">Streamlit</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        col_s3, col_s4 = st.columns(2)

        with col_s3:
            st.markdown("""
                <div class="custom-card">
                    <div class="card-header-flex">
                        <h3>📊 Power BI & Excel</h3>
                        <div class="icons-group">
                            <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/powerbi.svg" width="25" height="25" class="icon-gold" title="Power BI">
                            <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/microsoftexcel.svg" width="25" height="25" class="icon-green" title="Microsoft Excel">
                        </div>
                    </div>
                    <p class="card-list">
                        Penyusunan dashboard visual interaktif berbasis Power BI dan analisis data mendalam menggunakan rumus Advanced Excel.
                    </p>
                    <div style="margin: 10px 0 6px 0;"><b>Tingkat Penguasaan</b> &bull; 90%</div>
                    <div class="skill-progress-bg">
                        <div class="skill-progress" style="width: 90%;"></div>
                    </div>
                    <div class="skill-tag-group">
                        <span class="skill-tag">Power BI</span>
                        <span class="skill-tag">Pivot Table</span>
                        <span class="skill-tag">Dashboard KPI</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        with col_s4:
            st.markdown("""
                <div class="custom-card">
                    <div class="card-header-flex">
                        <h3>🎨 Graphic Designer</h3>
                        <div class="icons-group">
                            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/canva/canva-original.svg" width="28" height="28" title="Canva">
                            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/photoshop/photoshop-plain.svg" width="28" height="28" title="Photoshop">
                        </div>
                    </div>
                    <p class="card-list">
                        Pembuatan media visual, desain spanduk, banner program kerja, sertifikat, serta kebutuhan konten media informasi.
                    </p>
                    <div style="margin: 10px 0 6px 0;"><b>Tingkat Penguasaan</b> &bull; 90%</div>
                    <div class="skill-progress-bg">
                        <div class="skill-progress" style="width: 90%;"></div>
                    </div>
                    <div class="skill-tag-group">
                        <span class="skill-tag">Canva</span>
                        <span class="skill-tag">Visual Content</span>
                        <span class="skill-tag">Banner & Certificate</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("""
            <div class="custom-card">
                <div class="card-header-flex">
                    <h3>💼 Microsoft Office Suite</h3>
                    <div class="icons-group">
                        <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/microsoftword.svg" width="25" height="25" style="filter: invert(30%) sepia(80%) saturate(2000%) hue-rotate(200deg);" title="MS Word">
                        <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/microsoftpowerpoint.svg" width="25" height="25" style="filter: invert(35%) sepia(85%) saturate(2500%) hue-rotate(5deg);" title="MS PowerPoint">
                        <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/microsoftexcel.svg" width="25" height="25" class="icon-green" title="MS Excel">
                    </div>
                </div>
                <p class="card-list">
                    Pengelolaan administrasi perkantoran digital, penyusunan laporan ilmiah/kerja terstruktur, dan pembuatan slide presentasi bisnis profesional.
                </p>
                <div style="margin: 10px 0 6px 0;"><b>Tingkat Penguasaan</b> &bull; 90%</div>
                <div class="skill-progress-bg">
                    <div class="skill-progress" style="width: 90%;"></div>
                </div>
                <div class="skill-tag-group">
                    <span class="skill-tag">MS Word</span>
                    <span class="skill-tag">MS PowerPoint</span>
                    <span class="skill-tag">MS Excel</span>
                    <span class="skill-tag">Administrasi Digital</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # --- HALAMAN PENDIDIKAN ---
    elif page == "PENDIDIKAN":
        st.markdown('<div class="section-header">Riwayat Pendidikan & Akademik</div>', unsafe_allow_html=True)
        
        col_logo1, col_info1 = st.columns([1, 3])
        with col_logo1:
            st.image("https://assets.siakadcloud.com/uploads/universitasbosowa/logoaplikasi/1328.jpg", width=110)
            st.caption("Universitas Bosowa")
            
        with col_info1:
            st.subheader("Sarjana (S1) - Peternakan")
            st.write("**Status:** Mahasiswa Aktif (2026 – Sekarang)")
            st.write("Fokus pada pendalaman **Sistem Agribisnis & Pengolahan Data Lanjut**, integrasi database (SQL), serta analisis data bisnis untuk efisiensi industri peternakan.")
            st.divider()

        col_logo2, col_info2 = st.columns([1, 3])
        with col_logo2:
            st.image("https://sidaeng.polbangtan-gowa.ac.id/gambar/Logo.FpCa9qQisW.png", width=120)
            st.caption("Polbangtan Gowa")
            
        with col_info2:
            st.subheader("Diploma-III (D3) - Budidaya Ternak")
            st.write("**Periode:** 2020 – 2023 | **IPK:** 3.74 / 4.00")
            st.write("Mempelajari manajemen pemeliharaan ternak terstandar, pencatatan data operasional (*recording*), serta pengolahan data laboratorium.")
            st.divider()

        col_edu1, col_edu2 = st.columns(2)
        with col_edu1:
            st.subheader("🎓 Penelitian & Magang")
            st.markdown("**Penelitian Tugas Akhir**")
            st.write('*"Sistem Pengelolaan Semen di Balai Besar Inseminasi Buatan (BBIB) Singosari Jawa Timur"*')
            st.caption("• Menguji dan mengolah data kualitatif/kuantitatif sampel semen ternak ruminansia.")
            
            st.markdown("**Pengalaman Magang**")
            st.write("• **BBIB Singosari (2023):** Pengujian laboratorium & pencatatan data sampel semen.")
            st.write("• **PT Berdikari United Livestock / BULS (2022):** Pengelolaan data recording pemeliharaan ternak.")

        with col_edu2:
            st.subheader("👥 Organisasi & Sertifikasi")
            st.markdown("**Badan Eksekutif Mahasiswa (BEM)**")
            st.write("• **Divisi Penalaran & Keilmuan (2021–2022):** Menyelenggarakan kegiatan keilmuan dan sosial kemahasiswaan.")
            st.write("• **Divisi Media & Informasi (2021–2022):** Pembuatan desain visual (spanduk, sertifikat, banner) untuk kebutuhan program kerja.")
            
            st.markdown("**📜 Sertifikasi Profesi**")
            st.write("• **Operator Kandang Ternak (2023)** — Standardisasi kompetensi tata kelola manajemen kandang.")

    # --- HALAMAN PENGALAMAN ---
    elif page == "PENGALAMAN":
        st.markdown('<div class="section-header">Pengalaman Kerja & Profesional</div>', unsafe_allow_html=True)

        col_logo_tiran, col_info_tiran = st.columns([1, 2.5])

        with col_logo_tiran:
            st.markdown("""
                <div class="company-logo-card">
                    <img src="https://tirangroup.com/wp-content/uploads/2026/03/logo-tng-square.webp" style="width: 100%; max-width: 180px; height: auto; border-radius: 8px;">
                </div>
            """, unsafe_allow_html=True)
            st.subheader("PT Tiran Group Nusantara")
            st.caption("2023 – Sekarang")

        with col_info_tiran:
            st.subheader("Teknisi Peternakan & Data Analyst")
            st.markdown("**Unit Tambak — PT Tiran Group Nusantara** *(Full-Time)*")
            st.divider()
            
            st.markdown("### 🎯 Peran & Tanggung Jawab Utama:")
            st.write("• **Pengembangan Divisi:** Membangun dan merancang sistem tata kelola Divisi Peternakan di Unit Tambak PT Tiran Group Nusantara dari awal.")
            st.write("• **Evaluasi Lapangan & Input Data:** Analisis kondisi pemeliharaan serta merekapitulasi data operasional (pemeliharaan, produksi, dan penjualan) menggunakan Microsoft Excel & SQL.")
            st.write("• **Sistem Pelaporan Periodik:** Menyusun laporan harian, mingguan, dan bulanan berbasis data mentah lapangan untuk bahan evaluasi manajerial.")
            st.write("• **Visualisasi & Dashboard KPI (Power BI):** Menghubungkan database olahan dari DBeaver ke Power BI untuk membangun dashboard visual interaktif guna memantau KPI operasional dan tren penjualan secara *real-time*.")
            st.write("• **Otomatisasi Data Pipeline:** Merancang alur data terintegrasi dari lapangan hingga ke visualisasi dashboard untuk mempercepat pengambilan keputusan manajerial.")

            st.markdown("---")
            st.write("**Tools & Skills Digunakan:** `Power BI` • `SQL` • `DBeaver` • `Advanced Excel` • `Data Analytics` • `Operational Recording` caps")

    # --- HALAMAN PORTFOLIO ---
    elif page == "PORTFOLIO":
        st.markdown('<div class="section-header">Showcase Proyek Analisis & Manajemen</div>', unsafe_allow_html=True)
        
        st.markdown("""
            <div class="custom-card featured-card">
                <div class="card-header-flex">
                    <h3>📊 System Database & Analytics Peternakan - Perikanan</h3>
                    <span class="badge-featured">Featured Project</span>
                </div>
                <p class="card-list" style="font-size: 1rem !important; margin-bottom: 12px;">
                    Pengembangan sistem pengelolaan data terintegrasi untuk memantau operasional peternakan dan unit perikanan. Data mentah bersumber dari <b>Microsoft Excel</b> yang diolah dan distrukturkan ke dalam database relasional menggunakan <b>DBeaver</b>, kemudian dihubungkan ke <b>Power BI</b> untuk membangun dashboard visual monitoring KPI secara <i>real-time</i>.
                </p>
                <div class="skill-tag-group">
                    <span class="skill-tag">Power BI</span>
                    <span class="skill-tag">DBeaver / SQL</span>
                    <span class="skill-tag">Advanced Excel</span>
                    <span class="skill-tag">Data Pipeline</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.download_button(
            "Download project PDF",
            data=build_project_pdf(
                "System Database & Analytics Peternakan - Perikanan",
                "Featured project",
                "Pengembangan sistem pengelolaan data terintegrasi untuk memantau operasional peternakan dan unit perikanan. Data mentah dari Microsoft Excel distrukturkan ke database relasional menggunakan DBeaver dan dihubungkan ke Power BI untuk monitoring KPI.",
                "Power BI, DBeaver, SQL, Advanced Excel, Data Pipeline",
            ),
            file_name="system-database-analytics-peternakan-perikanan.pdf",
            mime="application/pdf",
            icon=":material/download:",
            width="stretch",
        )

        st.markdown("""
            <div class="custom-card">
                <div class="card-header-flex">
                    <h3>🗄️ Relational Database Management (DBeaver)</h3>
                    <span class="badge-category">SQL Project</span>
                </div>
                <p class="card-list" style="font-size: 1rem !important; margin-bottom: 12px;">
                    Perancangan skema database, pembersihan data mentah (data wrangling), serta optimasi query SQL untuk pencatatan inventaris dan operasional.
                </p>
                <div class="skill-tag-group">
                    <span class="skill-tag">DBeaver</span>
                    <span class="skill-tag">PostgreSQL / SQLite</span>
                    <span class="skill-tag">Data Cleaning</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.download_button(
            "Download project PDF",
            data=build_project_pdf(
                "Relational Database Management (DBeaver)",
                "SQL project",
                "Perancangan skema database, pembersihan data mentah, dan optimasi query SQL untuk pencatatan inventaris serta operasional.",
                "DBeaver, PostgreSQL, SQLite, Data Cleaning",
            ),
            file_name="relational-database-management-dbeaver.pdf",
            mime="application/pdf",
            icon=":material/download:",
            width="stretch",
        )

        st.markdown("""
            <div class="custom-card">
                <div class="card-header-flex">
                    <h3>🏗️ Evaluasi & Estimasi Renovasi Bangunan Kandang</h3>
                    <span class="badge-category">Operations & Infra</span>
                </div>
                <p class="card-list" style="font-size: 1rem !important; margin-bottom: 12px;">
                    Analisis kelayakan operasional, kalkulasi estimasi kebutuhan material, serta evaluasi alur biaya perbaikan fasilitas penunjang peternakan.
                </p>
                <div class="skill-tag-group">
                    <span class="skill-tag">Livestock Infrastructure</span>
                    <span class="skill-tag">Cost Estimation</span>
                    <span class="skill-tag">Project Evaluation</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.download_button(
            "Download project PDF",
            data=build_project_pdf(
                "Evaluasi & Estimasi Renovasi Bangunan Kandang",
                "Operations & infrastructure",
                "Analisis kelayakan operasional, kalkulasi estimasi kebutuhan material, dan evaluasi alur biaya perbaikan fasilitas penunjang peternakan.",
                "Livestock Infrastructure, Cost Estimation, Project Evaluation",
            ),
            file_name="evaluasi-estimasi-renovasi-kandang.pdf",
            mime="application/pdf",
            icon=":material/download:",
            width="stretch",
        )

        st.markdown("""
            <div class="custom-card">
                <div class="card-header-flex">
                    <h3>🎨 Visual Design & Branding Media (Canva)</h3>
                    <span class="badge-category">Creative Project</span>
                </div>
                <p class="card-list" style="font-size: 1rem !important; margin-bottom: 12px;">
                    Perancangan aset media visual, banner program kerja, sertifikat digital, serta materi presentasi interaktif untuk kebutuhan publikasi.
                </p>
                <div class="skill-tag-group">
                    <span class="skill-tag">Canva</span>
                    <span class="skill-tag">Visual Content</span>
                    <span class="skill-tag">Media Publication</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.download_button(
            "Download project PDF",
            data=build_project_pdf(
                "Visual Design & Branding Media (Canva)",
                "Creative project",
                "Perancangan aset media visual, banner program kerja, sertifikat digital, dan materi presentasi interaktif untuk kebutuhan publikasi.",
                "Canva, Visual Content, Media Publication",
            ),
            file_name="visual-design-branding-media-canva.pdf",
            mime="application/pdf",
            icon=":material/download:",
            width="stretch",
        )

    # --- HALAMAN CONTACT ---
    elif page == "CONTACT":
        st.markdown('<div class="section-header">Hubungi Saya</div>', unsafe_allow_html=True)
        st.markdown('<div class="contact-shell">', unsafe_allow_html=True)
        with st.form("contact_form"):
            c1, c2 = st.columns(2)
            with c1:
                name = st.text_input("Nama Anda")
            with c2:
                email = st.text_input("Alamat Email")
            message = st.text_area("Pesan")
            submit = st.form_submit_button("Kirim Pesan")
            if submit:
                st.success("Terima kasih! Pesan Anda telah terkirim.")
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 6. FOOTER PENUTUP GLOBAL
# ==========================================
st.markdown("""
<div class='dark-footer'>
    <h2>Let's Build Something Meaningful Together.</h2>
    <p>Siap membantu tim Anda membuat keputusan berbasis data secara terukur dan efisien.</p>
    <div class='social-row'>
        <a class='social-pill' href='https://www.linkedin.com/in/muh-irham-a-ilyas-372651307/' target='_blank' rel='noreferrer'>LinkedIn</a>
        <a class='social-pill' href='https://github.com/okyarmadani09-ops/profil-muh-irham-a-ilyas' target='_blank' rel='noreferrer'>GitHub</a>
        <a class='social-pill' href='mailto:muhirham.ilyas@gmail.com'>Email</a>
    </div>
</div>
""", unsafe_allow_html=True)