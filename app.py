import streamlit as st
from datetime import datetime, date, timedelta

# 1. SETTING HALAMAN WEB
st.set_page_config(page_title="Kalkulator Infus Pro", page_icon="💧", layout="centered")

# ==========================================
#      INJEKSI KODE DESAIN (CSS GLOW UP)
# ==========================================
st.markdown("""
<style>
    /* 1. Mengubah Gaya Judul Utama */
    .main h1 {
        color: #1E3A8A !important; /* Biru Gelap Medis */
        font-family: 'Inter', sans-serif;
        font-weight: 800 !important;
        text-align: center;
        margin-bottom: 5px;
    }
    
    /* 2. Menghias Semua Tombol Utama */
    div.stButton > button {
        background-color: #2563EB !important; /* Biru Cerah Medis */
        color: white !important;
        border-radius: 10px !important;
        border: none !important;
        padding: 10px 20px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease-in-out !important;
        box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.2) !important;
    }
    
    /* Efek Animasi Bergerak Saat Tombol Disentuh Kursor (Ala PPT) */
    div.stButton > button:hover {
        background-color: #1D4ED8 !important; /* Biru Lebih Gelap */
        transform: translateY(-2px) !important; /* Efek Melayang Naik */
        box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.4) !important;
    }
    
    /* 3. Mempercantik Kotak Kontainer (Container Border) */
    [data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 16px !important;
        border: 1px solid #E2E8F0 !important;
        background-color: #F8FAFC !important; /* Latar Belakang Kotak Soft Gray-Blue */
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.05) !important;
        padding: 20px !important;
    }

    /* 4. Merapikan Teks Petunjuk Informasi */
    .stAlert {
        border-radius: 12px !important;
    }
</style>
""", unsafe_allow_html=True)


# Inisialisasi State Navigasi Halaman
if 'halaman' not in st.session_state:
    st.session_state['halaman'] = 'home'

def kembali_ke_home():
    st.session_state['halaman'] = 'home'

# Buat daftar angka alarm Jam (00-23) dan Menit (00-59) untuk Menu 1
list_jam = [f"{i:02d}" for i in range(24)]
list_menit = [f"{i:02d}" for i in range(60)]

# ==========================================
#          HALAMAN UTAMA (HOME)
# ==========================================
if st.session_state['halaman'] == 'home':
    st.title("💧 Kalkulator Infus Profesional")
    st.write("<p style='text-align: center; color: #64748B;'>Silakan pilih mode perhitungan di bawah ini untuk memulai:</p>", unsafe_allow_html=True)
    st.write("")
    
    # Kotak Pilihan Menu 1
    with st.container(border=True):
        st.subheader("Menu 1: Hitung Waktu Habis & Laju Cairan")
        st.write("Gunakan ini jika kamu tahu **Kecepatan Infus (TPM)** dan ingin mencari tahu kapan infusnya habis serta berapa mL/jam lajunya.")
        if st.button("Buka Menu 1 ➔", use_container_width=True):
            st.session_state['halaman'] = 'menu1'
            st.rerun()

    st.write("") 

    # Kotak Pilihan Menu 2
    with st.container(border=True):
        st.subheader("Menu 2: Konversi mL/jam ke TPM")
        st.write("Gunakan ini jika instruksi dokter berupa target **mL/jam** dan kamu ingin tahu setelan TPM pada roller clamp dengan cepat.")
        if st.button("Buka Menu 2 ➔", use_container_width=True):
            st.session_state['halaman'] = 'menu2'
            st.rerun()

# ==========================================
#       HALAMAN MENU 1 (HITUNG WAKTU HABIS)
# ==========================================
elif st.session_state['halaman'] == 'menu1':
    if st.button("← Kembali ke Menu Utama"):
        kembali_ke_home()
        st.rerun()
        
    st.title("📋 Menu 1: Hitung Waktu Habis & Laju")
    
    with st.form("form_infus_1"):
        st.write("### Isi Data Cairan")
        
        volume = st.number_input("Masukkan Volume Infus (mL)", min_value=0.0, value=None, placeholder="Contoh: 500")
        tpm = st.number_input("Masukkan Kecepatan Infus (TPM)", min_value=0.0, value=None, placeholder="Contoh: 20")
        
        st.info("💡 Contoh faktor tetes yang umum pada kemasan:\n• 10 gtt/mL\n• 15 gtt/mL\n• 20 gtt/mL\n• 60 gtt/mL\n\n*Gunakan angka sesuai yang tertera pada kemasan infus set yang digunakan.*")
        faktor_tetes = st.number_input("Masukkan Faktor Tetes Kemasan (gtt/mL)", min_value=0.0, value=None, placeholder="Contoh: 20")
        
        st.write("⏱️ **Waktu Mulai Dipasang:**")
        col_jam, col_menit = st.columns(2)
        with col_jam:
            jam_terpilih = st.selectbox("Jam", list_jam, index=datetime.now().hour)
        with col_menit:
            menit_terpilih = st.selectbox("Menit", list_menit, index=datetime.now().minute)
        
        hitung = st.form_submit_button("Hitung Hasil Perhitungan ➔", use_container_width=True)

    if hitung:
        if volume is None or tpm is None or faktor_tetes is None:
            st.error("⚠️ Semua kotak jawaban di atas wajib diisi terlebih dahulu!")
        elif volume <= 0 or tpm <= 0 or faktor_tetes <= 0:
            st.error("⚠️ Angka yang dimasukkan harus lebih besar dari 0!")
        else:
            total_menit = (volume * faktor_tetes) / tpm
            ml_per_jam = (tpm * 60) / faktor_tetes
            
            waktu_mulai = datetime.now().replace(hour=int(jam_terpilih), minute=int(menit_terpilih), second=0, microsecond=0)
            
            # Presisi (Mahasiswa)
            total_detik = total_menit * 60
            p_jam = int(total_detik // 3600)
            p_menit = int((total_detik % 3600) // 60)
            p_detik = int(total_detik % 60)
            waktu_habis_presisi = waktu_mulai + timedelta(minutes=total_menit)
            
            # Praktis (Praktisi)
            menit_bulat = round(total_menit)
            pr_jam = menit_bulat // 60
            pr_menit = menit_bulat % 60
            waktu_habis_praktis = waktu_mulai + timedelta(minutes=menit_bulat)
            
            with st.container(border=True):
                st.success("### 📊 LEMBAR HASIL KALKULASI")
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

# ==========================================
#       HALAMAN MENU 2 (MURNI CONVERSI)
# ==========================================
elif st.session_state['halaman'] == 'menu2':
    if st.button("← Kembali ke Menu Utama"):
        kembali_ke_home()
        st.rerun()
        
    st.title("📋 Menu 2: Konversi mL/jam ke TPM")
    
    with st.form("form_infus_2"):
        st.write("### Isi Data Laju Aliran")
        
        laju_infus = st.number_input("Masukkan Laju yang Diinginkan (mL/jam)", min_value=0.0, value=None, placeholder="Contoh: 100")
        
        st.info("💡 Contoh faktor tetes yang umum pada kemasan:\n• 10 gtt/mL\n• 15 gtt/mL\n• 20 gtt/mL\n• 60 gtt/mL\n\n*Gunakan angka sesuai yang tertera pada kemasan infus set yang digunakan.*")
        faktor_tetes = st.number_input("Masukkan Faktor Tetes Kemasan (gtt/mL)", min_value=0.0, value=None, placeholder="Contoh: 20")
        
        hitung = st.form_submit_button("Hitung Kebutuhan Tetesan ➔", use_container_width=True)

    if hitung:
        if laju_infus is None or faktor_tetes is None:
            st.error("⚠️ Semua kotak jawaban di atas wajib diisi terlebih dahulu!")
        elif laju_infus <= 0 or faktor_tetes <= 0:
            st.error("⚠️ Angka yang dimasukkan harus lebih besar dari 0!")
        else:
            tpm_teoretis = (laju_infus * faktor_tetes) / 60
            
            with st.container(border=True):
                st.success("### 📊 LEMBAR HASIL KALKULASI TPM")
                st.write(f"**Laju yang Diinginkan:** {laju_infus} mL/jam")
                st.write(f"**Faktor Tetes Set:** {faktor_tetes} gtt/mL")
                
                tab_mhs, tab_prk = st.tabs(["🔴 KHUSUS MAHASISWA (Presisi)", "🟢 KHUSUS PRAKTISI (Lapangan)"])
                with tab_mhs:
                    st.write(f"• **TPM Teoretis:** {tpm_teoretis:.2f} TPM")
                with tab_prk:
                    st.write(f"• **TPM (Dibulatkan ke Bilangan Terdekat):** {round(tpm_teoretis)} TPM (Tetes/Menit)")
