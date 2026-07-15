import streamlit as st
from datetime import datetime, date, timedelta

# 1. SETTING HALAMAN WEB
st.set_page_config(page_title="Kalkulator Infus Pro", page_icon="💧", layout="centered")

# ==========================================
#      INJEKSI KODE DESAIN (CSS PREMIUM & ANIMASI)
# ==========================================
st.markdown("""
<style>
    /* 1. Efek Animasi Meluncur Masuk ala PPT (Fade In Slide Up) */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Menerapkan animasi ke seluruh blok utama web */
    .stMainBlockContainer, [data-testid="stVerticalBlock"] {
        animation: fadeInUp 0.5s ease-out forwards;
    }

    /* 2. Efek Judul Gradasi Premium (Gradient Text) */
    .gradient-title {
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 50%, #1E3A8A 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Inter', sans-serif;
        font-weight: 800 !important;
        text-align: center;
        font-size: 40px !important;
        margin-bottom: 10px;
    }
    
    /* 3. Menghias Semua Tombol Utama */
    div.stButton > button {
        background: linear-gradient(135deg, #3B82F6 0%, #2563EB 100%) !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
        transition: all 0.2s ease-in-out !important;
        box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.2) !important;
    }
    
    /* Efek Hover Tombol */
    div.stButton > button:hover {
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.3) !important;
    }
    
    /* Tombol Navigasi Sekunder (Kembali) agar warnanya beda dan elegan */
    div.stButton > button[key^="btn_back"], div.stButton > button:contains("←") {
        background: #F1F5F9 !important;
        color: #475569 !important;
        border: 1px solid #CBD5E1 !important;
        box-shadow: none !important;
    }
    div.stButton > button[key^="btn_back"]:hover {
        background: #E2E8F0 !important;
        color: #1E293B !important;
        transform: translateY(-2px) !important;
    }
    
    /* 4. Mempercantik Kotak Kontainer Card */
    [data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 20px !important;
        border: 1px solid #E2E8F0 !important;
        background-color: #F8FAFC !important;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.05), 0 10px 10px -5px rgba(0, 0, 0, 0.04) !important;
        padding: 25px !important;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
#     INISIALISASI STATE MULTI-LAYER
# ==========================================
# Halaman awal diset ke 'welcome'
if 'layer' not in st.session_state:
    st.session_state['layer'] = 'welcome'

# Buat menyimpan data input sementara agar tidak hilang saat bolak-balik halaman
if 'input_data' not in st.session_state:
    st.session_state['input_data'] = {}

# Daftar angka alarm jam & menit
list_jam = [f"{i:02d}" for i in range(24)]
list_menit = [f"{i:02d}" for i in range(60)]


# ==========================================
#      LAYER 1: KATA SAMBUTAN (WELCOME)
# ==========================================
if st.session_state['layer'] == 'welcome':
    st.markdown("<h1 class='gradient-title'>💧 INFUSION CALC PRO</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: #475569; font-weight: 500;'>Selamat Datang di Ruang Presisi Digital Pejuang Klinis!</p>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.write("<div style='text-align: center; padding: 10px 0;'>"
                 "Aplikasi ini dirancang khusus untuk membantu para praktisi kesehatan, bidan, perawat, hingga mahasiswa "
                 "dalam melakukan konversi dan kalkulasi laju cairan infus secara akurat, cepat, dan aman demi keselamatan pasien."
                 "<br><br><i>Telah disesuaikan dengan standar rumus perhitungan klinis terpercaya.</i>"
                 "</div>", unsafe_allow_html=True)
        
        st.write("")
        if st.button("🚀 MASUK APLIKASI UNTUK MEMULAI MENCARI ➔", use_container_width=True):
            st.session_state['layer'] = 'opsi'
            st.rerun()

# ==========================================
#      LAYER 2: PILIH OPSI MENU
# ==========================================
elif st.session_state['layer'] == 'opsi':
    st.markdown("<h2 style='text-align: center; color: #1E3A8A;'>Silakan Pilih Opsi yang Anda Butuhkan</h2>", unsafe_allow_html=True)
    st.write("")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### 📋 OPSI 1")
            st.write("**Hitung Waktu Habis & Laju Cairan**")
            st.caption("Gunakan jika Anda tahu kecepatan tetesan (TPM) dan ingin mencari tahu jam berapa kantong infus kosong.")
            if st.button("Buka Opsi 1 ➔", use_container_width=True, key="go_menu1"):
                st.session_state['layer'] = 'menu1_input'
                st.rerun()
                
    with col2:
        with st.container(border=True):
            st.markdown("### 📋 OPSI 2")
            st.write("**Konversi mL/jam ke TPM**")
            st.caption("Gunakan jika ada instruksi target volume per jam (mL/jam) dan ingin tahu setelan fisik roller clamp-nya.")
            if st.button("Buka Opsi 2 ➔", use_container_width=True, key="go_menu2"):
                st.session_state['layer'] = 'menu2_input'
                st.rerun()
                
    st.write("---")
    if st.button("🏠 Kembali ke Halaman Utama (Sambutan)", use_container_width=True, key="btn_back_welcome"):
        st.session_state['layer'] = 'welcome'
        st.rerun()

# ==========================================
#      LAYER 3A: INPUT FORM MENU 1
# ==========================================
elif st.session_state['layer'] == 'menu1_input':
    st.markdown("<h2 style='text-align: center; color: #1E3A8A;'>📋 Menu 1: Hitung Waktu Habis & Laju</h2>", unsafe_allow_html=True)
    
    with st.form("form_layer_1"):
        volume = st.number_input("Masukkan Volume Infus (mL)", min_value=0.0, value=st.session_state['input_data'].get('m1_vol', None), placeholder="Contoh: 500")
        tpm = st.number_input("Masukkan Kecepatan Infus (TPM)", min_value=0.0, value=st.session_state['input_data'].get('m1_tpm', None), placeholder="Contoh: 20")
        
        st.info("""
        💡 **PANDUAN FAKTOR TETES (gtt/mL):**
        Ukuran selang dari pabrik kemasan (BERBEDA dengan Kecepatan TPM). Nilai umumnya:
        • 10 / 15 / 20 gtt/mL (Umumnya makroset)  |  • 60 gtt/mL (Umumnya mikroset)
        """)
        faktor_tetes = st.number_input("Masukkan Faktor Tetes Kemasan (gtt/mL)", min_value=0.0, value=st.session_state['input_data'].get('m1_fakt', None), placeholder="Contoh: 20")
        
        st.write("⏱️ **Waktu Mulai Dipasang:**")
        c1, c2 = st.columns(2)
        with c1:
            jam_terpilih = st.selectbox("Jam", list_jam, index=st.session_state['input_data'].get('m1_jam', datetime.now().hour))
        with c2:
            menit_terpilih = st.selectbox("Menit", list_menit, index=st.session_state['input_data'].get('m1_men', datetime.now().minute))
            
        hitung = st.form_submit_button("🔮 HITUNG & TAMPILKAN HASIL ➔", use_container_width=True)
        
    if hitung:
        if volume is None or tpm is None or faktor_tetes is None:
            st.error("⚠️ Semua kotak di atas wajib diisi!")
        elif volume <= 0 or tpm <= 0 or faktor_tetes <= 0:
            st.error("⚠️ Angka harus lebih besar dari 0!")
        else:
            # Simpan data ke session state agar bisa dilempar ke layer hasil
            st.session_state['input_data']['m1_vol'] = volume
            st.session_state['input_data']['m1_tpm'] = tpm
            st.session_state['input_data']['m1_fakt'] = faktor_tetes
            st.session_state['input_data']['m1_jam'] = list_jam.index(jam_terpilih)
            st.session_state['input_data']['m1_men'] = list_menit.index(menit_terpilih)
            st.session_state['layer'] = 'menu1_hasil'
            st.rerun()
            
    st.write("---")
    nav1, nav2 = st.columns(2)
    with nav1:
        if st.button("← Kembali ke Pilihan Opsi", use_container_width=True):
            st.session_state['layer'] = 'opsi'
            st.rerun()
    with nav2:
        if st.button("🏠 Halaman Utama (Sambutan)", use_container_width=True, key="h1"):
            st.session_state['layer'] = 'welcome'
            st.rerun()

# ==========================================
#      LAYER 4A: LEMBAR HASIL MENU 1
# ==========================================
elif st.session_state['layer'] == 'menu1_hasil':
    st.markdown("<h2 style='text-align: center; color: #1E3A8A;'>📊 Lembar Hasil Perhitungan (Menu 1)</h2>", unsafe_allow_html=True)
    
    # Ambil data dari penyimpanan session
    volume = st.session_state['input_data']['m1_vol']
    tpm = st.session_state['input_data']['m1_tpm']
    faktor_tetes = st.session_state['input_data']['m1_fakt']
    j_idx = st.session_state['input_data']['m1_jam']
    m_idx = st.session_state['input_data']['m1_men']
    
    total_menit = (volume * faktor_tetes) / tpm
    ml_per_jam = (tpm * 60) / faktor_tetes
    waktu_mulai = datetime.now().replace(hour=int(list_jam[j_idx]), minute=int(list_menit[m_idx]), second=0, microsecond=0)
    
    # Perhitungan Durasi Aman (Bebas Bug 60 Menit)
    total_detik = total_menit * 60
    p_jam = int(total_detik // 3600)
    p_menit = int((total_detik % 3600) // 60)
    p_detik = int(total_detik % 60)
    waktu_habis_presisi = waktu_mulai + timedelta(minutes=total_menit)
    
    menit_bulat = round(total_menit)
    pr_jam = menit_bulat // 60
    pr_menit = menit_bulat % 60
    waktu_habis_praktis = waktu_mulai + timedelta(minutes=menit_bulat)
    
    with st.container(border=True):
        st.success("### DATA HASIL KALKULASI CAIRAN")
        st.write(f"**Volume Infus:** {volume} mL")
        st.write(f"**Laju Infus (Hasil Perhitungan):** {ml_per_jam:.2f} mL/jam")
        st.write(f"**Jam Pemasangan:** {waktu_mulai.strftime('%H:%M WIB')}")
        
        tab_mhs, tab_prk = st.tabs(["🔴 KHUSUS MAHASISWA (Presisi)", "🟢 KHUSUS PRAKTISI (Lapangan)"])
        with tab_mhs:
            st.write(f"• **Durasi Tepat:** {p_jam} Jam {p_menit} Menit {p_detik} Detik")
            st.write(f"• **Estimasi Selesai:** {waktu_habis_presisi.strftime('%H:%M:%S WIB')}")
        with tab_prk:
            st.write(f"• **Durasi Bulat:** {pr_jam} Jam {pr_menit} Menit")
            st.write(f"• **Perkiraan Selesai:** {waktu_habis_praktis.strftime('%H:%M WIB')}")
            
    st.write("---")
    nav1, nav2, nav3 = st.columns(3)
    with nav1:
        if st.button("← Ubah Data Input", use_container_width=True):
            st.session_state['layer'] = 'menu1_input'
            st.rerun()
    with nav2:
        if st.button("📋 Pilihan Opsi", use_container_width=True, key="o1"):
            st.session_state['layer'] = 'opsi'
            st.rerun()
    with nav3:
        if st.button("🏠 Halaman Utama", use_container_width=True, key="h2"):
            st.session_state['layer'] = 'welcome'
            st.rerun()

# ==========================================
#      LAYER 3B: INPUT FORM MENU 2
# ==========================================
elif st.session_state['layer'] == 'menu2_input':
    st.markdown("<h2 style='text-align: center; color: #1E3A8A;'>📋 Menu 2: Konversi mL/jam ke TPM</h2>", unsafe_allow_html=True)
    
    with st.form("form_layer_2"):
        laju_infus = st.number_input("Masukkan Laju yang Diinginkan (mL/jam)", min_value=0.0, value=st.session_state['input_data'].get('m2_laju', None), placeholder="Contoh: 100")
        
        st.info("""
        💡 **PANDUAN FAKTOR TETES (gtt/mL):**
        Ukuran selang dari pabrik kemasan (BERBEDA dengan Kecepatan TPM). Nilai umumnya:
        • 10 / 15 / 20 gtt/mL (Umumnya makroset)  |  • 60 gtt/mL (Umumnya mikroset)
        """)
        faktor_tetes = st.number_input("Masukkan Faktor Tetes Kemasan (gtt/mL)", min_value=0.0, value=st.session_state['input_data'].get('m2_fakt', None), placeholder="Contoh: 20")
        
        hitung = st.form_submit_button("🔮 HITUNG KEBUTUHAN TETESAN ➔", use_container_width=True)
        
    if hitung:
        if laju_infus is None or faktor_tetes is None:
            st.error("⚠️ Semua kotak di atas wajib diisi!")
        elif laju_infus <= 0 or faktor_tetes <= 0:
            st.error("⚠️ Angka harus lebih besar dari 0!")
        else:
            st.session_state['input_data']['m2_laju'] = laju_infus
            st.session_state['input_data']['m2_fakt'] = faktor_tetes
            st.session_state['layer'] = 'menu2_hasil'
            st.rerun()
            
    st.write("---")
    nav1, nav2 = st.columns(2)
    with nav1:
        if st.button("← Kembali ke Pilihan Opsi", use_container_width=True):
            st.session_state['layer'] = 'opsi'
            st.rerun()
    with nav2:
        if st.button("🏠 Halaman Utama (Sambutan)", use_container_width=True, key="h3"):
            st.session_state['layer'] = 'welcome'
            st.rerun()

# ==========================================
#      LAYER 4B: LEMBAR HASIL MENU 2
# ==========================================
elif st.session_state['layer'] == 'menu2_hasil':
    st.markdown("<h2 style='text-align: center; color: #1E3A8A;'>📊 Lembar Hasil Konversi TPM (Menu 2)</h2>", unsafe_allow_html=True)
    
    laju_infus = st.session_state['input_data']['m2_laju']
    faktor_tetes = st.session_state['input_data']['m2_fakt']
    
    tpm_teoretis = (laju_infus * faktor_tetes) / 60
    
    with st.container(border=True):
        st.success("### DATA HASIL KONVERSI KECEPATAN TETES")
        st.write(f"**Laju yang Diinginkan:** {laju_infus} mL/jam")
        st.write(f"**Faktor Tetes Set:** {faktor_tetes} gtt/mL")
        
        tab_mhs, tab_prk = st.tabs(["🔴 KHUSUS MAHASISWA (Presisi)", "🟢 KHUSUS PRAKTISI (Lapangan)"])
        with tab_mhs:
            st.write(f"• **TPM Teoretis:** {tpm_teoretis:.2f} TPM")
        with tab_prk:
            st.write(f"• **TPM (Dibulatkan ke Bilangan Terdekat):** {round(tpm_teoretis)} TPM (Tetes/Menit)")
            
    st.write("---")
    nav1, nav2, nav3 = st.columns(3)
    with nav1:
        if st.button("← Ubah Data Input", use_container_width=True):
            st.session_state['layer'] = 'menu2_input'
            st.rerun()
    with nav2:
        if st.button("📋 Pilihan Opsi", use_container_width=True, key="o2"):
            st.session_state['layer'] = 'opsi'
            st.rerun()
    with nav3:
        if st.button("🏠 Halaman Utama", use_container_width=True, key="h4"):
            st.session_state['layer'] = 'welcome'
            st.rerun()
