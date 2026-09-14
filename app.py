import os
import streamlit as st
import pandas as pd
import base64

def get_base64_img(img_path):
    with open(img_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# 1. Konfigurasi Halaman Web
st.set_page_config(
    page_title="Portofolio - Muh Irham A Ilyas",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 3rem;
        padding-left: 4rem;
        padding-right: 4rem;
    }
    .stApp {
        background-color: #F8F9FD;
    }
    .nav-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-bottom: 15px;
        border-bottom: 1px solid #EEEEEE;
        margin-bottom: 20px;
    }
    .logo-box {
        width: 35px;
        height: 20px;
        background-color: #444444;
        border-radius: 2px;
    }
    .lang-switch {
        color: #888888;
        font-size: 11px;
        letter-spacing: 1px;
    }
    .hello-text {
        color: #888888;
        font-size: 12px;
        letter-spacing: 2px;
        font-weight: 600;
        margin-bottom: 10px;
    }
    .hero-title {
        font-size: 46px;
        font-weight: 800;
        color: #111111;
        line-height: 1.2;
        margin-bottom: 15px;
    }
    .hero-title span {
        color: #E63946;
    }
    .hero-desc {
        color: #666666;
        font-size: 14px;
        line-height: 1.6;
        max-width: 450px;
        margin-bottom: 25px;
    }
    .btn-red {
        background-color: #E63946;
        color: white !important;
        padding: 12px 28px;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 1px;
        border: none;
        border-radius: 2px;
        text-decoration: none;
        display: inline-block;
        box-shadow: 0px 4px 15px rgba(230, 57, 70, 0.3);
    }
    .social-icons {
        margin-top: 40px;
        color: #888888;
        font-size: 16px;
    }
    .social-icons span {
        margin-right: 15px;
        cursor: pointer;
    }
    .section-header {
        font-size: 24px;
        font-weight: 700;
        color: #111111;
        margin-top: 15px;
        margin-bottom: 20px;
        border-left: 4px solid #E63946;
        padding-left: 12px;
    }
    .custom-card {
        background: white;
        padding: 24px;
        border-radius: 8px;
        box-shadow: 0px 2px 10px rgba(0,0,0,0.03);
        margin-bottom: 20px;
    }
    .badge-ipk {
        background-color: #E63946;
        color: white;
        padding: 6px 14px;
        border-radius: 12px;
        font-weight: 700;
        font-size: 13px;
        display: inline-block;
        margin-top: 10px;
    }
    div[data-testid="stHorizontalBlock"] button {
        border: none !important;
        background: transparent !important;
        font-weight: 600 !important;
        color: #555555 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Bar Navigasi Header Atas
st.markdown("""
    <div class="nav-header">
        <div class="logo-box"></div>
        <div class="lang-switch">IND &nbsp; <b style="color:#111;">ENG</b></div>
    </div>
""", unsafe_allow_html=True)

# 4. Inisialisasi Session State Navigasi
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

# 5. Logika Halaman Berdasarkan Tombol Navigasi
page = st.session_state.current_page

if page == "HOME":
    col1, col2 = st.columns([1.1, 1])

    with col1:
        st.markdown("""
            <div style="padding-top: 20px;">
                <div class="hello-text">&mdash; HELLO</div>
                <div class="hero-title">I'm <span>Muh Irham A Ilyas</span></div>
                <div class="hero-desc">
                    Saya menghadirkan pendekatan <b>Analisis Data</b> yang terstruktur untuk menjawab tantangan operasional dan administrasi bisnis. Dengan keahlian di bidang <b>SQL (PostgreSQL/SQLite), Python</b>, dan <b>Power BI</b>, saya mengolah data kompleks menjadi dashboard visual yang intuitif. Latar belakang saya di sektor <b>Peternakan</b> (Polbangtan Gowa & Universitas Bosowa) memberikan perspektif mendalam dalam memecahkan masalah riil industri <b>Agribisnis</b> secara tepat sasaran.
                </div>
                <a href="#" class="btn-red">DOWNLOAD CV</a>
                <div class="social-icons">
                    <span>🌐</span> <span>💼</span> <span>✉️</span> <span>📷</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(BASE_DIR, "Irham1.png")
        
        if os.path.exists(img_path):
            img_b64 = get_base64_img(img_path)
            
            # Render foto menggunakan HTML & CSS tajam (crisp-edges)
            st.markdown(f"""
                <div style="text-align: center;">
                    <img src="data:image/png;base64,{img_b64}" 
                         style="width: 320px; 
                                max-width: 100%; 
                                height: auto; 
                                image-rendering: -webkit-optimize-contrast; 
                                image-rendering: crisp-edges;
                                filter: drop-shadow(0px 4px 10px rgba(0,0,0,0.15));">
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("File 'Irham1.png' tidak ditemukan di folder app.py!")

elif page == "ABOUT":
    st.markdown('<div class="section-header">Tentang Saya</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="custom-card">
            <h3 style="color:#111; margin-bottom:15px;">Profil Profesional</h3>
            <p style="color:#666; font-size:14px; line-height:1.6;">
                Lulusan D-III dan sedang menjalani S1 dengan dasar yang kuat dalam analis data, pembersihan data, dan visualisasi menggunakan Excel Tingkat Lanjut, SQL, Query dan Power BI. Memiliki pengalaman dalam membuat proyek mandiri dalam membangun dashboard interaktif dan bersemangat untuk berkontribusi dalam pengambilan Keputusan berbasis data di Perusahaan.
            </p>
            <br>
            <h4 style="color:#E63946;">Pengalaman & Keahlian Utama</h4>
            <ul style="color:#555; line-height:1.8;">
                <li>Analisis Data & Visualisasi</li>
                <li>Penyusunan Laporan & Dashboard Interaktif</li>
                <li>Pengelolaan Data & Pembersihan Data</li>
                <li>Penggunaan SQL, Excel, Power BI, dan Python</li>
                <li>Pengalaman dalam Proyek Mandiri & Kolaboratif</li>
                <li>Komunikasi Efektif & Pemecahan Masalah</li>
                <li>Pengolahan Administrasi Digital & Database</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

elif page == "SKILLS":
    st.markdown('<div class="section-header">Tingkat Keahlian & Tools</div>', unsafe_allow_html=True)
    col_about, col_skills = st.columns([1, 1])
    with col_skills:  
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.write("**Tingkat Penguasaan Tools & Skills**")
        st.text("SQL & Data Querying")
        st.progress(85)
        st.text("Python (Pandas & Streamlit)")
        st.progress(80)
        st.text("Power BI & Excel Analysis")
        st.progress(90)
        st.text("Graphic Design & Visuals")
        st.progress(90)
        st.text("Microsoft Office Suite")
        st.progress(90)
        st.markdown('</div>', unsafe_allow_html=True)

elif page == "PENDIDIKAN":
    st.markdown('<div class="section-header">Riwayat Pendidikan</div>', unsafe_allow_html=True)

    col_logo1, col_info1 = st.columns([1, 2.5])
    
    with col_logo1:
        st.image("https://assets.siakadcloud.com/uploads/universitasbosowa/logoaplikasi/1328.jpg", width=130)
        st.subheader("Universitas Bosowa")
        st.caption("2026 – Sekarang")
        st.markdown("**Status: Mahasiswa Aktif**")

    with col_info1:
        st.subheader("Sarjana (S1) - Peternakan")
        st.write("Mengembangkan keahlian dalam olah data tingkat lanjut, query database (SQL), serta visualisasi bisnis.")
        st.divider()

    st.markdown("<br>", unsafe_allow_html=True)

    col_logo, col_info = st.columns([1, 2.5])
    
    with col_logo:
        # Menampilkan Card Logo Kampus
        st.image("https://sidaeng.polbangtan-gowa.ac.id/gambar/Logo.FpCa9qQisW.png", width=140)
        st.subheader("Politeknik Pembangunan Pertanian")
        st.caption("Polbangtan Gowa (2020 – 2023)")
        st.markdown("**IPK: 3.74 / 4.00**")

    with col_info:
        # Menggunakan Elemen Bawaan Streamlit (Bebas Error Teks Kode)
        st.subheader("Diploma-III - Peternakan")
        st.write("**Program Studi:** Budidaya Ternak")
        st.divider()

        st.markdown("### 🎓 Penelitian")
        st.write('**Judul Penelitian:** *"Sistem Pengelolaan Semen di Balai Besar Inseminasi Buatan (BBIB) Singosari Jawa Timur"*')
        st.write("**Fokus:** Menguji dan Mengolah Data Pada Semen Cair dan Semen Beku Pada Ternak Ruminansia.")

        st.markdown("### 💼 Pengalaman Magang")
        st.write("• **Balai Besar Inseminasi Buatan (BBIB)** - Singosari, Jawa Timur (2023)")
        st.caption("  *Menguji dan Mengolah Data Pada Semen Cair dan Semen Beku Pada Ternak.*")
        st.write("• **Pt Berdikari United Livestock (BULS)** - Sidrap, Sulawesi Selatan (2022)")
        st.caption("  *Mengelola data recording pemeliharaan dan memelihara ternak secara profesional.*")

        st.markdown("### 👥 Pengalaman Organisasi")
        st.write("• **Anggota / Pengurus Badan Eksekutif Mahasiswa** — Divisi Penalaran & Keilmuan (2021-2022)")
        st.caption("  *Menyelenggarakan kegiatan kemahasiswaan dan kegiatan sosial.*")
        st.write("• **Anggota / Pengurus Badan Eksekutif Mahasiswa** — Divisi Media & Informasi (2021-2022)")
        st.caption("  *Menggantikan posisi kordinator media & informasi*")
        st.caption("  *Membuat desain(spanduk, sertifikat, banner) kebutuhan program kerja setiap divisi*")
        st.write("• **Anggota / Panitia Himpunan Mahasiswa Peternakan** — Divisi Media & Informasi (2021-2022)")
        st.caption("  *Panitia Pengkaderan Mahasiswa Baru*")

    col_icon, col_title = st.columns([0.6, 3])
    with col_icon:
        img_b64 = get_base64_image("i:\Dowload\certificate-free-sticker-02.png")
        st.markdown(
            f'### <img src="data:image/png;base64,{img_b64}" width="30" height="30"> Sertifikat Operator Kandang</h3>', unsafe_allow_html=True)
    with col_title:
        st.write('**Judul Sertifikat:** *"Operator Kandang (2023)"*')
        st.write("**Fokus:** Mampu mengoperasikan dan mengelola kandang ternak secara profesional.")

elif page == "PENGALAMAN":
    st.markdown('<div class="section-header">Pengalaman Kerja & Profesional</div>', unsafe_allow_html=True)

    # --- PENGALAMAN 1 ---
    col_logo1, col_info1 = st.columns([1, 2.5])
    with col_logo1:
        st.image("https://tirangroup.com/wp-content/uploads/2026/03/logo-tng-square.webp", width=120)
        st.markdown("""
            <h4 style="color:#111; margin-top:10px; margin-bottom:5px;">Pt Tiran Group Nusantara</h4>
            <p style="color:#888; font-size:13px; font-weight:600;">2023 &ndash; Sekarang</p>
        </div>
        """, unsafe_allow_html=True)
    with col_info1:
        st.markdown("""
            <div class="custom-card">
                <h3 style="color:#E63946; margin-bottom:5px;">Teknisi Peternakan</h3>
                <h5 style="color:#444; margin-bottom:10px;">Pt Tiran Group Nusantara &bull; <span style="color:#888; font-size:14px;">2023 &ndash; Sekarang</span></h5>
                <hr style="border: 0.5px solid #F0F0F0;">
            <ul style="color:#555; font-size:14px; line-height:1.7;">
                <li><b>Memabangun Divisi Peternakan di Unit </b>Tambak Pt Tiran Group Nusantara</b></li>
                <li><b>Melakukan evaluasi lapangan dengan data yang sudah ada</b></li>
                <li><b>Memperbaiki system manajemen perkandangan</b></li>
                <li><b>Melakukan input data (pemeliharaan, Produksi, Penjualan) dengan menggunakan excel.</b></li>
                <li><b>Membuat laporan harian, mingguan, dan bulanan untuk manajemen.</b></li>
                <li><b>Membuat visualisasi data untuk mempermudah pengambilan keputusan manajemen.</b></li>
                <li><b>Melakukan evaluasi pemeliharaan dengan menggunakan data pemeliharaan sebagai bahan evaluasi.</b></li>
                <li><b>Membuat laporan rutin (harian, Bulanan, Tahunan) yang berasal dari data mentah yang pada lapangan.</b></li>
                <li><b>Membuat Visualisasi & Dashboard Interaktif (Power BI):</b> Menghubungkan database hasil olahan dari DBeaver ke <b>Power BI</b> untuk membangun dashboard visual yang memantau KPI operasional dan tren penjualan secara <i>real-time</i>.</li>
                <li><b>Otomatisasi Laporan:</b> Memastikan alur data (<i>data pipeline</i>) dari database hingga visualisasi berjalan lancar guna mendukung pengambilan keputusan manajerial secara akurat.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

elif page == "PORTFOLIO":
    st.markdown('<div class="section-header">Showcase Proyek Analisis</div>', unsafe_allow_html=True)
    p_col1, p_col2 = st.columns(2)

    with p_col1:
        st.markdown("""
            <div class="custom-card">
                <h4 style="color:#E63946;">01. Proyek Analisis Dashboard</h4>
                <p style="color:#666; font-size:13px;">Analisis performa penjualan bulanan dan simulasi keuntungan menggunakan Python & Streamlit.</p>
            </div>
        """, unsafe_allow_html=True)
        data = pd.DataFrame({
            'Bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei'],
            'Penjualan (Juta)': [12, 19, 15, 25, 22]
        })
        st.line_chart(data.set_index('Bulan'))

    with p_col2:
        st.markdown("""
            <div class="custom-card">
                <h4 style="color:#E63946;">02. Proyek Tracking Keuangan & Inventaris</h4>
                <p style="color:#666; font-size:13px;">Sistem otomatisasi pencatatan inventaris dan pengeluaran operasional berbasis digital template.</p>
            </div>
        """, unsafe_allow_html=True)
        inv_data = pd.DataFrame({
            'Kategori': ['Elektronik', 'Furnitur', 'Peralatan'],
            'Jumlah Stok': [45, 28, 60]
        })
        st.bar_chart(inv_data.set_index('Kategori'))

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