import os
import streamlit as st
import pandas as pd
import base64

def get_base64_img(img_path):
    if os.path.exists(img_path):
        with open(img_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

# 1. Konfigurasi Halaman Web
st.set_page_config(
    page_title="Muh Irham A Ilyas | Data Analyst Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS (Warm Minimalist & Earthy Aesthetic - High Performance)
st.markdown("""
    <style>
    /* Reset & Native System Font */
    html, body, [class*="css"] {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Background Utama (#F5F2EB) */
    .stApp {
        background-color: #F5F2EB;
        color: #22201F;
    }
    
    /* Typografi Header */
    h1, h2, h3, h4, h5 {
        color: #22201F !important;
        font-weight: 700 !important;
        letter-spacing: -0.5px;
    }

    /* Section Header Decorator */
    .section-header {
        font-size: 1.8rem;
        font-weight: 700;
        color: #22201F;
        border-bottom: 2px solid #6E6B5A;
        padding-bottom: 8px;
        margin-bottom: 25px;
    }
    
    /* Hero Typography */
    .hello-text {
        color: #6E6B5A;
        font-weight: 700;
        letter-spacing: 2px;
        font-size: 0.9rem;
        margin-bottom: 5px;
        text-transform: uppercase;
    }
    
    .hero-title {
        font-size: 2.5rem;
        font-weight: 800;
        color: #22201F;
        margin-bottom: 15px;
        line-height: 1.2;
    }
    .hero-title span {
        color: #6E6B5A;
    }

    .hero-desc {
        color: #555248;
        font-size: 1.05rem;
        line-height: 1.7;
        margin-bottom: 25px;
    }

    /* Olive Banner Component (#6E6B5A) */
    .olive-card {
        background-color: #6E6B5A;
        color: #FFFFFF;
        padding: 35px 40px;
        border-radius: 20px;
        margin: 25px 0px 35px 0px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
    }
    .olive-card h3 {
        color: #FFFFFF !important;
        font-size: 1.5rem !important;
        margin-bottom: 10px;
    }
    .olive-card p {
        color: #ECE8E1;
        font-size: 1.05rem;
        line-height: 1.6;
        margin: 0;
    }

    /* Cards Component (#E8E4DC) */
    .custom-card {
        background-color: #E8E4DC;
        border: 1px solid #DCD7CC;
        padding: 24px;
        border-radius: 16px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.02);
    }

    /* Native Streamlit Metric Styling */
    div[data-testid="stMetric"] {
        background-color: #E8E4DC !important;
        border: 1px solid #DCD7CC !important;
        padding: 20px !important;
        border-radius: 14px !important;
    }
    [data-testid="stMetricValue"] {
        color: #22201F !important;
        font-weight: 700 !important;
    }
    [data-testid="stMetricLabel"] {
        color: #636054 !important;
    }

    /* Dark Footer (#1E1D1A) */
    .dark-footer {
        background-color: #1E1D1A;
        color: #E8E4DC;
        padding: 45px 40px;
        border-radius: 24px 24px 0px 0px;
        margin-top: 50px;
        text-align: center;
    }
    .dark-footer h2 {
        color: #F5F2EB !important;
        font-size: 1.8rem !important;
        margin-bottom: 10px;
    }
    .dark-footer p {
        color: #B5B0A3;
        font-size: 1rem;
        margin-bottom: 15px;
    }

    /* Button Styling */
    .btn-primary-link {
        display: inline-block;
        background-color: #22201F;
        color: #F5F2EB !important;
        padding: 10px 24px;
        border-radius: 30px;
        font-weight: 600;
        text-decoration: none;
        transition: all 0.3s ease;
    }
    .btn-primary-link:hover {
        background-color: #6E6B5A;
        color: #FFFFFF !important;
    }

    .stButton>button {
        background-color: #22201F !important;
        color: #F5F2EB !important;
        border-radius: 25px !important;
        font-weight: 600 !important;
        border: none !important;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover {
        background-color: #6E6B5A !important;
        color: #FFFFFF !important;
    }

    /* Tab Styling */
    button[data-baseweb="tab"] {
        color: #636054 !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
    }
    button[aria-selected="true"] {
        color: #22201F !important;
        border-bottom-color: #6E6B5A !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Navigasi Halaman Utama
if 'current_page' not in st.session_state:
    st.session_state.current_page = "HOME"

nav1, nav2, nav3, nav4, nav5, nav6, nav7 = st.columns(7)

with nav1:
    if st.button("HOME", use_container_width=True):
        st.session_state.current_page = "HOME"
with nav2:
    if st.button("ABOUT", use_container_width=True):
        st.session_state.current_page = "ABOUT"
with nav3:
    if st.button("PORTFOLIO", use_container_width=True):
        st.session_state.current_page = "PORTFOLIO"
with nav4:
    if st.button("SKILLS", use_container_width=True):
        st.session_state.current_page = "SKILLS"
with nav5:
    if st.button("PENDIDIKAN", use_container_width=True):
        st.session_state.current_page = "PENDIDIKAN"
with nav6:
    if st.button("PENGALAMAN", use_container_width=True):
        st.session_state.current_page = "PENGALAMAN"
with nav7:
    if st.button("CONTACT", use_container_width=True):
        st.session_state.current_page = "CONTACT"

st.markdown("<br>", unsafe_allow_html=True)

# 4. Routing Halaman
page = st.session_state.current_page
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if page == "HOME":
    col1, col2 = st.columns([1.2, 0.8])

    with col1:
        st.markdown("""
            <div style="padding-top: 10px;">
                <div class="hello-text">— HELLO & WELCOME</div>
                <div class="hero-title">I'm <span>Muh Irham A Ilyas</span></div>
                <div class="hero-desc">
                    Saya menghadirkan pendekatan <b>Analisis Data</b> yang terstruktur untuk menjawab tantangan operasional dan administrasi bisnis. Memiliki spesialisasi dalam mengolah database relasional <b>SQL (PostgreSQL/SQLite)</b>, membuat skrip otomatisasi <b>Python</b>, serta menyajikan dashboard visual interaktif berbasis <b>Power BI & Streamlit</b>.
                </div>
                <a href="#" class="btn-primary-link">DOWNLOAD CV</a>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        img_path = os.path.join(BASE_DIR, "Irham1.png")
        img_b64 = get_base64_img(img_path)
        
        if img_b64:
            st.markdown(f"""
                <div style="text-align: center;">
                    <img src="data:image/png;base64,{img_b64}" 
                         style="width: 280px; 
                                max-width: 100%; 
                                height: auto; 
                                border-radius: 120px 120px 20px 20px;
                                border: 3px solid #DCD7CC;
                                filter: drop-shadow(0px 8px 20px rgba(0,0,0,0.08));">
                </div>
            """, unsafe_allow_html=True)
        else:
            st.info("💡 File foto profil 'Irham1.png' siap ditampilkan setelah ditempatkan di folder proyek.")

    # Olive Banner Highlight
    st.markdown("""
    <div class='olive-card'>
        <h3>I'm Irham — your partner in data & analytics.</h3>
        <p>Berfokus pada pengolahan database relasional, pembersihan data (Data Wrangling), riset visualisasi data interaktif, serta otomatisasi skrip pengolahan data untuk efisiensi keputusan bisnis.</p>
    </div>
    """, unsafe_allow_html=True)

    # Core Expertise Grid
    st.markdown("<div class='section-header'>Tailored Strategies. Real Results.</div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class='custom-card'>
            <h4>🗄️ Database & Query</h4>
            <p style='color:#555248; font-size:14px;'>• SQL (PostgreSQL, MySQL)<br>• DBeaver Management<br>• Data Wrangling & Cleaning<br>• Query Optimization</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class='custom-card'>
            <h4>⚡ Python Automation</h4>
            <p style='color:#555248; font-size:14px;'>• Python (Pandas, NumPy)<br>• Streamlit Web Apps<br>• Data Pipeline Automation<br>• VS Code Workflow</p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class='custom-card'>
            <h4>📊 Business Intelligence</h4>
            <p style='color:#555248; font-size:14px;'>• Power BI Dashboards<br>• Interactive Data Viz<br>• Executive KPI Reporting<br>• Agribusiness Analytics</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "ABOUT":
    st.markdown('<div class="section-header">Tentang Saya</div>', unsafe_allow_html=True)
    
    # --- PROFIL RINGKAS (BANNER ATAS) ---
    st.markdown("""
        <div class="olive-card" style="margin-top:0px; margin-bottom:25px;">
            <h3 style="margin-bottom:8px;">Hello! Saya Muh Irham A Ilyas 👋</h3>
            <p>Data Analyst dengan latar belakang spesifik di sektor agribisnis dan peternakan. Saya menjembatani data mentah lapangan dengan pengambilan keputusan strategis melalui query SQL, otomatisasi Python, serta dashboard bisnis interaktif.</p>
        </div>
    """, unsafe_allow_html=True)

    # --- TATA LETAK 2 KOLOM MINIMALIS ---
    col_ab1, col_ab2 = st.columns(2)

    with col_ab1:
        st.subheader("📌 Fokus & Spesialisasi Utama")
        st.write("• **Database Management & Cleaning:** Mengolah data mentah dari Excel menjadi struktur database relasional menggunakan **SQL (SQLite/PostgreSQL)** dan **DBeaver**.")
        st.write("• **Scripting & Otomatisasi:** Efisiensi alur pemrosesan data (data pipeline) berbasis **Python (Pandas)**.")
        st.write("• **Executive Business Intelligence:** Merancang visualisasi KPI dan tren bisnis menggunakan **Power BI** dan **Streamlit**.")
        st.write("• **Domain Expertise:** Pemahaman mendalam terkait operasional peternakan, perikanan, serta recording data industri agribisnis.")

    with col_ab2:
        st.subheader("💡 Pendekatan Kerja")
        
        st.markdown("**1. Terstruktur & Presisi**")
        st.caption("Setiap data diolah dengan standar pembersihan data (data wrangling) yang ketat untuk menjamin akurasi laporan.")
        
        st.markdown("**2. Beriorientasi Solusi Bisnis**")
        st.caption("Fokus tidak hanya pada data visual, tetapi pada rekomendasi konkret yang mempercepat pengambilan keputusan manajerial.")
        
        st.markdown("**3. Adaptif & Pembelajar Cepat**")
        st.caption("Aktif meningkatkan kapabilitas analitis baik dari studi akademik S1 Peternakan Universitas Bosowa maupun praktik proyek industri.")

    st.divider()

    # --- RINGKASAN TAGAR TOOLS & DOMAIN ---
    st.write("**Domain & Technical Highlights:** `SQL / DBeaver` • `Python / Pandas` • `Power BI` • `Excel Query` • `Livestock & Aquaculture Analytics` • `Digital Administration`")

elif page == "SKILLS":
    st.markdown('<div class="section-header">Tingkat Keahlian & Tools</div>', unsafe_allow_html=True)
    
    # --- BARIS 1: SQLITE & PYTHON ---
    col_s1, col_s2 = st.columns(2)
    
    with col_s1:
        st.markdown("""
            <div class="custom-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                    <h3 style="color:#6E6B5A; margin:0;">🗄️ SQLite & Query</h3>
                    <div style="display: flex; gap: 8px;">
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" width="28" height="28" title="SQLite">
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" width="28" height="28" title="PostgreSQL">
                    </div>
                </div>
                <p style="color:#555248; font-size:14px; margin-bottom:15px;">
                    Penguasaan manipulasi database relasional, pembersihan data mentah, serta ekstraksi informasi presisi.
                </p>
                <div style="margin-bottom:8px;"><b>Tingkat Penguasaan</b> &bull; 85%</div>
                <div style="background:#DCD7CC; border-radius:10px; height:8px; margin-bottom:15px;">
                    <div style="background:#6E6B5A; width:85%; height:8px; border-radius:10px;"></div>
                </div>
                <div>
                    <span style="background:#F5F2EB; border:1px solid #DCD7CC; padding:4px 10px; border-radius:12px; font-size:12px; font-weight:600;">SQLite</span>
                    <span style="background:#F5F2EB; border:1px solid #DCD7CC; padding:4px 10px; border-radius:12px; font-size:12px; font-weight:600;">DBeaver</span>
                    <span style="background:#F5F2EB; border:1px solid #DCD7CC; padding:4px 10px; border-radius:12px; font-size:12px; font-weight:600;">Data Cleaning</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col_s2:
        st.markdown("""
            <div class="custom-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                    <h3 style="color:#6E6B5A; margin:0;">⚡ Python, Pandas & Streamlit</h3>
                    <div style="display: flex; gap: 8px;">
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="28" height="28" title="Python">
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width="28" height="28" title="Pandas">
                        <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/streamlit.svg" width="26" height="26" style="filter: invert(41%) sepia(18%) saturate(452%) hue-rotate(14deg) brightness(94%) contrast(89%);" title="Streamlit">
                    </div>
                </div>
                <p style="color:#555248; font-size:14px; margin-bottom:15px;">
                    Pengembangan skrip otomatisasi olah data, manipulasi dataset berukuran besar, dan aplikasi web interaktif.
                </p>
                <div style="margin-bottom:8px;"><b>Tingkat Penguasaan</b> &bull; 80%</div>
                <div style="background:#DCD7CC; border-radius:10px; height:8px; margin-bottom:15px;">
                    <div style="background:#6E6B5A; width:80%; height:8px; border-radius:10px;"></div>
                </div>
                <div>
                    <span style="background:#F5F2EB; border:1px solid #DCD7CC; padding:4px 10px; border-radius:12px; font-size:12px; font-weight:600;">Python</span>
                    <span style="background:#F5F2EB; border:1px solid #DCD7CC; padding:4px 10px; border-radius:12px; font-size:12px; font-weight:600;">Pandas</span>
                    <span style="background:#F5F2EB; border:1px solid #DCD7CC; padding:4px 10px; border-radius:12px; font-size:12px; font-weight:600;">Streamlit</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # --- BARIS 2: POWER BI & GRAPHIC DESIGNER ---
    col_s3, col_s4 = st.columns(2)

    with col_s3:
        st.markdown("""
            <div class="custom-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                    <h3 style="color:#6E6B5A; margin:0;">📊 Power BI & Excel</h3>
                    <div style="display: flex; gap: 8px; align-items: center;">
                        <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/powerbi.svg" width="25" height="25" style="filter: invert(72%) sepia(85%) saturate(700%) hue-rotate(355deg) brightness(95%) contrast(92%);" title="Power BI">
                        <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/microsoftexcel.svg" width="25" height="25" style="filter: invert(32%) sepia(80%) saturate(600%) hue-rotate(100deg) brightness(90%);" title="Microsoft Excel">
                    </div>
                </div>
                <p style="color:#555248; font-size:14px; margin-bottom:15px;">
                    Penyusunan dashboard visual interaktif berbasis Power BI dan analisis data mendalam menggunakan rumus Advanced Excel.
                </p>
                <div style="margin-bottom:8px;"><b>Tingkat Penguasaan</b> &bull; 90%</div>
                <div style="background:#DCD7CC; border-radius:10px; height:8px; margin-bottom:15px;">
                    <div style="background:#6E6B5A; width:90%; height:8px; border-radius:10px;"></div>
                </div>
                <div>
                    <span style="background:#F5F2EB; border:1px solid #DCD7CC; padding:4px 10px; border-radius:12px; font-size:12px; font-weight:600;">Power BI</span>
                    <span style="background:#F5F2EB; border:1px solid #DCD7CC; padding:4px 10px; border-radius:12px; font-size:12px; font-weight:600;">Pivot Table</span>
                    <span style="background:#F5F2EB; border:1px solid #DCD7CC; padding:4px 10px; border-radius:12px; font-size:12px; font-weight:600;">Dashboard KPI</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col_s4:
        st.markdown("""
            <div class="custom-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                    <h3 style="color:#6E6B5A; margin:0;">🎨 Graphic Designer</h3>
                    <div style="display: flex; gap: 8px;">
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/canva/canva-original.svg" width="28" height="28" title="Canva">
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/photoshop/photoshop-plain.svg" width="28" height="28" title="Photoshop">
                    </div>
                </div>
                <p style="color:#555248; font-size:14px; margin-bottom:15px;">
                    Pembuatan media visual, desain spanduk, banner program kerja, sertifikat, serta kebutuhan konten media informasi.
                </p>
                <div style="margin-bottom:8px;"><b>Tingkat Penguasaan</b> &bull; 90%</div>
                <div style="background:#DCD7CC; border-radius:10px; height:8px; margin-bottom:15px;">
                    <div style="background:#6E6B5A; width:90%; height:8px; border-radius:10px;"></div>
                </div>
                <div>
                    <span style="background:#F5F2EB; border:1px solid #DCD7CC; padding:4px 10px; border-radius:12px; font-size:12px; font-weight:600;">Canva</span>
                    <span style="background:#F5F2EB; border:1px solid #DCD7CC; padding:4px 10px; border-radius:12px; font-size:12px; font-weight:600;">Visual Content</span>
                    <span style="background:#F5F2EB; border:1px solid #DCD7CC; padding:4px 10px; border-radius:12px; font-size:12px; font-weight:600;">Banner & Certificate</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # --- BARIS 3: MICROSOFT OFFICE ---
    st.markdown("""
        <div class="custom-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <h3 style="color:#6E6B5A; margin:0;">💼 Microsoft Office Suite</h3>
                <div style="display: flex; gap: 10px; align-items: center;">
                    <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/microsoftword.svg" width="25" height="25" style="filter: invert(30%) sepia(80%) saturate(2000%) hue-rotate(200deg);" title="MS Word">
                    <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/microsoftpowerpoint.svg" width="25" height="25" style="filter: invert(35%) sepia(85%) saturate(2500%) hue-rotate(5deg);" title="MS PowerPoint">
                    <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/microsoftexcel.svg" width="25" height="25" style="filter: invert(32%) sepia(80%) saturate(600%) hue-rotate(100deg) brightness(90%);" title="MS Excel">
                </div>
            </div>
            <p style="color:#555248; font-size:14px; margin-bottom:15px;">
                Pengelolaan administrasi perkantoran digital, penyusunan laporan ilmiah/kerja terstruktur, dan pembuatan slide presentasi bisnis profesional.
            </p>
            <div style="margin-bottom:8px;"><b>Tingkat Penguasaan</b> &bull; 90%</div>
            <div style="background:#DCD7CC; border-radius:10px; height:8px; margin-bottom:15px;">
                <div style="background:#6E6B5A; width:90%; height:8px; border-radius:10px;"></div>
            </div>
            <div>
                <span style="background:#F5F2EB; border:1px solid #DCD7CC; padding:4px 10px; border-radius:12px; font-size:12px; font-weight:600;">MS Word</span>
                <span style="background:#F5F2EB; border:1px solid #DCD7CC; padding:4px 10px; border-radius:12px; font-size:12px; font-weight:600;">MS PowerPoint</span>
                <span style="background:#F5F2EB; border:1px solid #DCD7CC; padding:4px 10px; border-radius:12px; font-size:12px; font-weight:600;">MS Excel</span>
                <span style="background:#F5F2EB; border:1px solid #DCD7CC; padding:4px 10px; border-radius:12px; font-size:12px; font-weight:600;">Administrasi Digital</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

elif page == "PENDIDIKAN":
    st.markdown('<div class="section-header">Riwayat Pendidikan & Akademik</div>', unsafe_allow_html=True)
    
    # --- PENDIDIKAN 1: UNIVERSITAS BOSOWA ---
    col_logo1, col_info1 = st.columns([1, 3])
    
    with col_logo1:
        st.image("https://assets.siakadcloud.com/uploads/universitasbosowa/logoaplikasi/1328.jpg", width=110)
        st.caption("Universitas Bosowa")
        
    with col_info1:
        st.subheader("Sarjana (S1) - Peternakan")
        st.write("**Status:** Mahasiswa Aktif (2026 – Sekarang)")
        st.write("Fokus pada pendalaman **Sistem Agribisnis & Pengolahan Data Lanjut**, integrasi database (SQL), serta analisis data bisnis untuk efisiensi industri peternakan.")
        st.divider()

    st.markdown("<br>", unsafe_allow_html=True)

    # --- PENDIDIKAN 2: POLBANGTAN GOWA ---
    col_logo2, col_info2 = st.columns([1, 3])
    
    with col_logo2:
        st.image("https://sidaeng.polbangtan-gowa.ac.id/gambar/Logo.FpCa9qQisW.png", width=120)
        st.caption("Polbangtan Gowa")
        
    with col_info2:
        st.subheader("Diploma-III (D3) - Budidaya Ternak")
        st.write("**Periode:** 2020 – 2023 | **IPK:** 3.74 / 4.00")
        st.write("Mempelajari manajemen pemeliharaan ternak terstandar, pencatatan data operasional (recording), serta pengolahan data laboratorium.")
        st.divider()

    st.markdown("<br>", unsafe_allow_html=True)

    # --- PENELITIAN, MAGANG & ORGANISASI ---
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

elif page == "PENGALAMAN":
    st.markdown('<div class="section-header">Pengalaman Kerja & Profesional</div>', unsafe_allow_html=True)

    col_logo_tiran, col_info_tiran = st.columns([1, 3])

    with col_logo_tiran:
        st.image("https://tirangroup.com/wp-content/uploads/2026/03/logo-tng-square.webp", width=330)
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

        st.markdown("<br>", unsafe_allow_html=True)
        st.write("**Tools & Skills Digunakan:** `Power BI` • `SQL` • `DBeaver` • `Advanced Excel` • `Data Analytics` • `Operational Recording`")

elif page == "PORTFOLIO":
    st.markdown('<div class="section-header">Showcase Proyek Analisis</div>', unsafe_allow_html=True)
    
    # --- PROYEK UTAMA: DATABASE PETERNAKAN & PERIKANAN ---
    st.markdown("""
        <div class="custom-card" style="border-left: 5px solid #6E6B5A;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <h3 style="color:#6E6B5A; margin:0;">📊 System Database & Analytics Peternakan - Perikanan</h3>
                <span style="background:#6E6B5A; color:#FFF; padding:4px 12px; border-radius:15px; font-size:12px; font-weight:600;">Featured Project</span>
            </div>
            <p style="color:#555248; font-size:14.5px; line-height:1.6;">
                Pengembangan sistem pengelolaan data terintegrasi untuk memantau operasional peternakan dan unit perikanan. Data mentah bersumber dari <b>Microsoft Excel</b> yang diolah dan distrukturkan ke dalam database relasional menggunakan <b>DBeaver</b>, kemudian dihubungkan ke <b>Power BI</b> untuk membangun dashboard visual monitoring KPI secara <i>real-time</i>.
            </p>
            <div style="margin-top:12px; margin-bottom:15px;">
                <span style="background:#F5F2EB; border:1px solid #DCD7CC; padding:4px 10px; border-radius:12px; font-size:12px; font-weight:600;">Power BI</span>
                <span style="background:#F5F2EB; border:1px solid #DCD7CC; padding:4px 10px; border-radius:12px; font-size:12px; font-weight:600;">DBeaver / SQL</span>
                <span style="background:#F5F2EB; border:1px solid #DCD7CC; padding:4px 10px; border-radius:12px; font-size:12px; font-weight:600;">Advanced Excel</span>
                <span style="background:#F5F2EB; border:1px solid #DCD7CC; padding:4px 10px; border-radius:12px; font-size:12px; font-weight:600;">Data Pipeline</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # --- METRICS & SIMULASI DASHBOARD ---
    st.subheader("💡 Ringkasan Indikator Performance (KPI)")
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric(label="Total Rekap Data Operasional", value="10,000+ Baris", delta="Excel to SQL")
    with m2:
        st.metric(label="Efisiensi Waktu Pelaporan", value="85% Lebih Cepat", delta="Automated Pipeline")
    with m3:
        st.metric(label="Akurasi Monitoring Stok/Produksi", value="99.2%", delta="Real-time Power BI")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- TAB DETAIL PROYEK & SIMULASI GRAFIK ---
    st.subheader("📈 Simulasi Analytics & Visualisasi Data")
    tab_livestock, tab_fishery = st.tabs(["🐄 Monitoring Unit Peternakan", "🐟 Analytics Unit Perikanan"])

    with tab_livestock:
        st.write("#### Monitoring Tren Produksi & Pemeliharaan Ternak")
        st.write("Visualisasi pergerakan volume produksi dan rekapitulasi data pemeliharaan harian yang telah diolah dari DBeaver.")
        
        # Dataset Simulasi Peternakan
        data_peternakan = pd.DataFrame({
            'Bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun'],
            'Volume Produksi (Kg)': [450, 520, 610, 580, 690, 750],
            'Efisiensi Pakan (%)': [82, 85, 87, 86, 89, 91]
        })
        
        col_g1, col_g2 = st.columns(2)
        with col_g1:
            st.write("**Tren Volume Produksi**")
            st.line_chart(data_peternakan.set_index('Bulan')['Volume Produksi (Kg)'])
        with col_g2:
            st.write("**Tingkat Efisiensi Operasional Pakan**")
            st.bar_chart(data_peternakan.set_index('Bulan')['Efisiensi Pakan (%)'])

    with tab_fishery:
        st.write("#### Analytics Distribusi & Inventaris Unit Perikanan")
        st.write("Monitoring pencatatan stok, distribusi hasil perikanan, dan evaluasi hasil panen periodik.")
        
        # Dataset Simulasi Perikanan
        data_perikanan = pd.DataFrame({
            'Kategori Komoditas': ['Ikan Air Tawar', 'Udang & Crustacea', 'Pakan & Nutrisi', 'Peralatan Tambak'],
            'Total Volume (Ton)': [18, 25, 40, 12]
        })
        
        st.write("**Distribusi Stok & Komoditas Perikanan**")
        st.bar_chart(data_perikanan.set_index('Kategori Komoditas'))

    st.markdown("<br>", unsafe_allow_html=True)

    # --- PROYEK TAMBAHAN (AUTOMATION & TRACKING) ---
    st.subheader("🛠️ Proyek Analisis & Otomatisasi Lainnya")
    p_col1, p_col2 = st.columns(2)

    with p_col1:
        st.markdown("""
            <div class="custom-card">
                <h4 style="color:#6E6B5A;">02. Automatic Data Pipeline & Cleaning</h4>
                <p style="color:#555248; font-size:13.5px; line-height:1.5;">
                    Pembuatan skrip Python otomatis untuk membersihkan data mentah (data cleaning) sebelum diunggah ke database relasional SQLite/PostgreSQL.
                </p>
                <span style="background:#F5F2EB; border:1px solid #DCD7CC; padding:3px 8px; border-radius:10px; font-size:11px; font-weight:600;">Python</span>
                <span style="background:#F5F2EB; border:1px solid #DCD7CC; padding:3px 8px; border-radius:10px; font-size:11px; font-weight:600;">Pandas</span>
            </div>
        """, unsafe_allow_html=True)

    with p_col2:
        st.markdown("""
            <div class="custom-card">
                <h4 style="color:#6E6B5A;">03. Executive KPI Dashboard App</h4>
                <p style="color:#555248; font-size:13.5px; line-height:1.5;">
                    Aplikasi web portofolio dan dashboard interaktif ringkas berbasis Streamlit untuk menyajikan indikator performa utama bisnis secara intuitif.
                </p>
                <span style="background:#F5F2EB; border:1px solid #DCD7CC; padding:3px 8px; border-radius:10px; font-size:11px; font-weight:600;">Streamlit</span>
                <span style="background:#F5F2EB; border:1px solid #DCD7CC; padding:3px 8px; border-radius:10px; font-size:11px; font-weight:600;">Plotly</span>
            </div>
        """, unsafe_allow_html=True)

elif page == "CONTACT":
    st.markdown('<div class="section-header">Hubungi Saya</div>', unsafe_allow_html=True)
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

# 5. Footer Penutup
st.markdown("""
<div class='dark-footer'>
    <h2>Let's Build Something Meaningful Together.</h2>
    <p>Siap membantu tim Anda membuat keputusan berbasis data secara terukur dan efisien.</p>
</div>
""", unsafe_allow_html=True)
