import streamlit as st
from datetime import datetime, date, timedelta

# 1. SETTING HALAMAN WEB
st.set_page_config(page_title="Kalkulator Infus Pro", page_icon="💧", layout="centered")

# Inisialisasi State Navigasi Halaman
if 'halaman' not in st.session_state:
    st.session_state['halaman'] = 'home'

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
#       HALAMAN MENU 1 (INPUT MANUAL BERSIH)
# ==========================================
elif st.session_state['halaman'] == 'menu1':
    if st.button("← Kembali ke Menu Utama"):
        kembali_ke_home()
        st.rerun()
        
    st.title("📋 Menu 1: Hitung Waktu Habis")
    
    with st.form("form_infus_1"):
        st.write("### Isi Data Cairan")
        
        # value=None membuat kotak kosong secara bawaan saat pertama kali dibuka
        volume = st.number_input("Masukkan Volume Cairan Infus (mL)", min_value=0.0, value=None, placeholder="Contoh: 500")
        tpm = st.number_input("Masukkan Kecepatan Tetesan (TPM)", min_value=0.0, value=None, placeholder="Contoh: 20")
        
        st.info("💡 Petunjuk Faktor Tetes (gtt/mL) pada kemasan infus set yang umum:\n• 10 / 15 / 20 (Dewasa/Makro) \n• 60 (Anak/Mikro)")
        faktor_tetes = st.number_input("Masukkan Faktor Tetes Kemasan (gtt/mL)", min_value=0.0, value=None, placeholder="Contoh: 20")
        
        jam_mulai_time = st.time_input("Jam Berapa Infus Mulai Dipasang?", value=datetime.now().time())
        
        hitung = st.form_submit_button("Hitung Hasil Perhitungan ➔", use_container_width=True)

    if hitung:
        # Validasi wajib isi jika user belum mengetik apa pun
        if volume is None or tpm is None or faktor_tetes is None:
            st.error("⚠️ Semua kotak jawaban di atas wajib diisi terlebih dahulu!")
        elif volume <= 0 or tpm <= 0 or faktor_tetes <= 0:
            st.error("⚠️ Angka yang dimasukkan harus lebih besar dari 0!")
        else:
            # Hitung Data
            total_menit = (volume * faktor_tetes) / tpm
            ml_per_jam = (tpm * 60) / faktor_tetes
            
            waktu_mulai = datetime.combine(date.today(), jam_mulai_time)
            waktu_habis_presisi = waktu_mulai + timedelta(minutes=total_menit)
            waktu_habis_praktis = waktu_mulai + timedelta(minutes=round(total_menit))
            
            p_jam, p_menit = int(total_menit // 60), int(total_menit % 60)
            
            with st.container(border=True):
                st.success("### 📊 LEMBAR HASIL KALKULASI")
                st.write(f"**Laju Aktual Cairan:** {ml_per_jam:.2f} mL/jam")
                st.write(f"**Jam Pemasangan:** {waktu_mulai.strftime('%H:%M WIB')}")
                
                tab_mhs, tab_prk = st.tabs(["🔴 KHUSUS MAHASISWA (Presisi)", "🟢 KHUSUS PRAKTISI (Lapangan)"])
                with tab_mhs:
                    st.write(f"• **Durasi Tepat:** {p_jam} Jam {total_menit % 60:.2f} Menit")
                    st.write(f"• **Estimasi Selesai:** {waktu_habis_presisi.strftime('%H:%M:%S WIB')}")
                with tab_prk:
                    st.write(f"• **Durasi Bulat:** {p_jam} Jam {round(total_menit % 60)} Menit")
                    st.write(f"• **Perkiraan Selesai:** {waktu_habis_praktis.strftime('%H:%M WIB')}")

# ==========================================
#       HALAMAN MENU 2 (INPUT MANUAL BERSIH)
# ==========================================
elif st.session_state['halaman'] == 'menu2':
    if st.button("← Kembali ke Menu Utama"):
        kembali_ke_home()
        st.rerun()
        
    st.title("📋 Menu 2: Hitung Target TPM")
    
    with st.form("form_infus_2"):
        st.write("### Isi Data Cairan")
        
        volume = st.number_input("Masukkan Volume Cairan Infus (mL)", min_value=0.0, value=None, placeholder="Contoh: 500")
        laju_infus = st.number_input("Masukkan Target Laju Cairan (mL/jam)", min_value=0.0, value=None, placeholder="Contoh: 100")
        
        st.info("💡 Petunjuk Faktor Tetes (gtt/mL) pada kemasan infus set yang umum:\n• 10 / 15 / 20 (Dewasa/Makro) \n• 60 (Anak/Mikro)")
        faktor_tetes = st.number_input("Masukkan Faktor Tetes Kemasan (gtt/mL)", min_value=0.0, value=None, placeholder="Contoh: 20")
        
        jam_mulai_time = st.time_input("Jam Berapa Infus Mulai Dipasang?", value=datetime.now().time())
        
        hitung = st.form_submit_button("Hitung Hasil Perhitungan ➔", use_container_width=True)

    if hitung:
        # Validasi wajib isi jika user belum mengetik apa pun
        if volume is None or laju_infus is None or faktor_tetes is None:
            st.error("⚠️ Semua kotak jawaban di atas wajib diisi terlebih dahulu!")
        elif volume <= 0 or laju_infus <= 0 or faktor_tetes <= 0:
            st.error("⚠️ Angka yang dimasukkan harus lebih besar dari 0!")
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
