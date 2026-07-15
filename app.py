import streamlit as st
from datetime import datetime, date, timedelta

# 1. SETTING HALAMAN WEB
st.set_page_config(page_title="Kalkulator Infus Pro", page_icon="💧", layout="centered")

# Inisialisasi State Navigasi (Biar bisa bolak-balik Halaman Utama <-> Form)
if 'halaman' not in st.session_state:
    st.session_state['halaman'] = 'home'

# Fungsi pembantu untuk tombol kembali
def kembali_ke_home():
    st.session_state['halaman'] = 'home'

# ==========================================
#          HALAMAN UTAMA (HOME)
# ==========================================
if st.session_state['halaman'] == 'home':
    st.title("💧 Kalkulator Infus Profesional")
    st.write("Silakan pilih mode perhitungan di bawah ini untuk memulai:")
    
    # Kotak Pilihan Menu 1
    with st.container(border=True):
        st.subheader("Menu 1: Hitung Waktu Habis & Laju Cairan")
        st.write("Gunakan ini jika kamu tahu **TPM (Tetes Per Menit)** dan ingin mencari tahu kapan infusnya habis.")
        if st.button("Buka Menu 1 ➔", use_container_width=True):
            st.session_state['halaman'] = 'menu1'
            st.rerun()

    st.write("") # Spasi pembatas

    # Kotak Pilihan Menu 2
    with st.container(border=True):
        st.subheader("Menu 2: Hitung Target TPM (Tetes Per Menit)")
        st.write("Gunakan ini jika dokter memberi instruksi target **mL/jam** dan kamu ingin mencari tahu setelan TPM-nya.")
        if st.button("Buka Menu 2 ➔", use_container_width=True):
            st.session_state['halaman'] = 'menu2'
            st.rerun()

# ==========================================
#       HALAMAN MENU 1 (INPUT SEKALIGUS)
# ==========================================
elif st.session_state['halaman'] == 'menu1':
    if st.button("← Kembali ke Menu Utama"):
        kembali_ke_home()
        st.rerun()
        
    st.title("📋 Menu 1: Hitung Waktu Habis")
    
    # Semua pertanyaan ditampilkan dalam satu box Form sekaligus
    with st.form("form_infus_1"):
        st.write("### Isi Data Cairan")
        
        volume = st.number_input("Masukkan Volume Cairan Infus (mL)", min_value=0.0, value=500.0, step=50.0)
        tpm = st.number_input("Masukkan Kecepatan Tetesan (TPM)", min_value=0.0, value=20.0, step=1.0)
        
        faktor_opsi = st.selectbox("Pilih Faktor Tetes Kemasan (gtt/mL)", ["20 (Standar Dewasa)", "60 (Standar Anak)", "10", "15", "Kustom"])
        
        faktor_tetes = 20.0
        if "20" in faktor_opsi: faktor_tetes = 20.0
        elif "60" in faktor_opsi: faktor_tetes = 60.0
        elif "10" in faktor_opsi: faktor_tetes = 10.0
        elif "15" in faktor_opsi: faktor_tetes = 15.0
        else:
            faktor_tetes = st.number_input("Masukkan Faktor Tetes Kustom", min_value=0.1, value=20.0)
            
        jam_mulai_time = st.time_input("Jam Berapa Infus Mulai Dipasang?", value=datetime.now().time())
        
        # Tombol submit di dalam form
        hitung = st.form_submit_button("Hitung Hasil Perhitungan ➔", use_container_width=True)

    if hitung:
        if volume <= 0 or tpm <= 0:
            st.error("Volume dan TPM harus lebih besar dari 0!")
        else:
            # Hitung Data
            total_menit = (volume * faktor_tetes) / tpm
            ml_per_jam = (tpm * 60) / faktor_tetes
            
            waktu_mulai = datetime.combine(date.today(), jam_mulai_time)
            waktu_habis_presisi = waktu_mulai + timedelta(minutes=total_menit)
            waktu_habis_praktis = waktu_mulai + timedelta(minutes=round(total_menit))
            
            # Format durasi teks
            p_jam, p_menit = int(total_menit // 60), int(total_menit % 60)
            
            # TAMPILAN LEMBAR HASIL DALAM KOTAK
            with st.container(border=True):
                st.success("### 📊 LEMBAR HASIL KALKULASI")
                st.write(f"**Laju Aktual Cairan:** {ml_per_jam:.2f} mL/jam")
                st.write(f"**Jam Pemasangan:** {waktu_mulai.strftime('%H:%M WIB')}")
                
                # Split hasil via Tabs agar rapi
                tab_mhs, tab_prk = st.tabs(["🔴 KHUSUS MAHASISWA (Presisi)", "🟢 KHUSUS PRAKTISI (Lapangan)"])
                with tab_mhs:
                    st.write(f"• **Durasi Tepat:** {p_jam} Jam {total_menit % 60:.2f} Menit")
                    st.write(f"• **Estimasi Selesai:** {waktu_habis_presisi.strftime('%H:%M:%S WIB')}")
                with tab_prk:
                    st.write(f"• **Durasi Bulat:** {p_jam} Jam {round(total_menit % 60)} Menit")
                    st.write(f"• **Perkiraan Selesai:** {waktu_habis_praktis.strftime('%H:%M WIB')}")

# ==========================================
#       HALAMAN MENU 2 (INPUT SEKALIGUS)
# ==========================================
elif st.session_state['halaman'] == 'menu2':
    if st.button("← Kembali ke Menu Utama"):
        kembali_ke_home()
        st.rerun()
        
    st.title("📋 Menu 2: Hitung Target TPM")
    
    with st.form("form_infus_2"):
        st.write("### Isi Data Cairan")
        
        volume = st.number_input("Masukkan Volume Cairan Infus (mL)", min_value=0.0, value=500.0, step=50.0)
        laju_infus = st.number_input("Masukkan Target Laju Cairan (mL/jam)", min_value=0.0, value=100.0, step=10.0)
        
        faktor_opsi = st.selectbox("Pilih Faktor Tetes Kemasan (gtt/mL)", ["20 (Standar Dewasa)", "60 (Standar Anak)", "10", "15", "Kustom"])
        
        faktor_tetes = 20.0
        if "20" in faktor_opsi: faktor_tetes = 20.0
        elif "60" in faktor_opsi: faktor_tetes = 60.0
        elif "10" in faktor_opsi: faktor_tetes = 10.0
        elif "15" in faktor_opsi: faktor_tetes = 15.0
        else:
            faktor_tetes = st.number_input("Masukkan Faktor Tetes Kustom", min_value=0.1, value=20.0)
            
        jam_mulai_time = st.time_input("Jam Berapa Infus Mulai Dipasang?", value=datetime.now().time())
        
        hitung = st.form_submit_button("Hitung Hasil Perhitungan ➔", use_container_width=True)

    if hitung:
        if volume <= 0 or laju_infus <= 0:
            st.error("Volume dan Laju Cairan harus lebih besar dari 0!")
        else:
            tpm_teoretis = (laju_infus * faktor_tetes) / 60
            total_menit = (volume / laju_infus) * 60
            
            waktu_mulai = datetime.combine(date.today(), jam_mulai_time)
            waktu_habis_presisi = waktu_mulai + timedelta(minutes=total_menit)
            waktu_habis_praktis = waktu_mulai + timedelta(minutes=round(total_menit))
            
            p_jam, p_menit = int(total_menit // 60), int(total_menit % 60)
            
            with st.container(border=True):
                st.success("### 📊 LEMBAR HASIL KALKULASI")
                st.write(f"**Target Kecepatan:** {laju_infus} mL/jam")
                st.write(f"**Jam Pemasangan:** {waktu_mulai.strftime('%H:%M WIB')}")
                
                tab_mhs, tab_prk = st.tabs(["🔴 KHUSUS MAHASISWA (Presisi)", "🟢 KHUSUS PRAKTISI (Lapangan)"])
                with tab_mhs:
                    st.write(f"• **Kebutuhan Tetesan:** {tpm_teoretis:.2f} TPM")
                    st.write(f"• **Estimasi Selesai:** {waktu_habis_presisi.strftime('%H:%M:%S WIB')}")
                with tab_prk:
                    st.write(f"• **Setelan Roller Clamp:** {round(tpm_teoretis)} TPM (Tetes/Menit)")
                    st.write(f"• **Perkiraan Selesai:** {waktu_habis_praktis.strftime('%H:%M WIB')}")