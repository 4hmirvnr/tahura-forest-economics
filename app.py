import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Konfigurasi Halaman
st.set_page_config(page_title="Valuasi Ekonomi Tahura Djuanda", page_icon="🌲", layout="wide")

# ==========================================
# STATE MANAGEMENT
# ==========================================
if 'luas' not in st.session_state: st.session_state.luas = 590
if 'kerapatan' not in st.session_state: st.session_state.kerapatan = 80

# Sidebar Navigasi
st.sidebar.title("🌲 Menu Navigasi")
menu = st.sidebar.radio("Pilih Modul:", [
    "1. Beranda", "2. Profil Tahura", "3. Kalkulator TEV", 
    "4. Trade-off Lahan", "5. Kebijakan PES", "6. Kasus Interaktif", "7. Visualisasi TEV"
])

# ==========================================
# LOGIKA MENU
# ==========================================
if menu == "1. Beranda":
    st.title("PBL 6  ̶  Ekonomi Sumber Daya Alam dan Lingkungan 🌍")
    st.markdown("---")
    st.subheader("Identitas Kelompok 3")
    st.info("• Ahmad Irvan Nur Varizki (10090224011)\n• Freya Helga Pebrian (10090224017)\n• Muhammad Yaasin As-Suhaimi (10090224028)")
    st.markdown("**Dosen Pengampu:** Yuhka Sundaya, S.E., M.S.i")

elif menu == "2. Profil Tahura":
    st.title("Profil Taman Hutan Raya Ir. H. Juanda 🏞️")
    st.write("Tahura pertama di Indonesia, diresmikan 1985. Luas ±590 Ha, elevasi 770-1.330 mdpl.")
    st.write("Fungsi: Daerah tangkapan air utama Sungai Cikapundung & destinasi wisata (Gua Belanda/Jepang).")
    st.write("Biodiversitas: 2.500 jenis flora, habitat monyet kra, burung kepodang, dan tupai.")

elif menu == "3. Kalkulator TEV":
    st.header("Kalkulator TEV 🧮")
    st.session_state.luas = st.number_input("Luas Lahan (Ha)", value=st.session_state.luas)
    st.session_state.kerapatan = st.slider("Kerapatan Vegetasi (%)", 10, 100, st.session_state.kerapatan)
    
    factor = st.session_state.luas * (st.session_state.kerapatan / 100)
    # Kalkulasi sesuai komponen permintaan
    guna_langsung = factor * 25  # wisata & hasil hutan
    jasa_ling = factor * 45     # air & karbon
    nilai_pilihan = factor * 15 # potensi masa depan
    nilai_eksis = factor * 15   # flora & fauna
    
    c1, c2 = st.columns(2)
    c1.metric("Nilai Guna Langsung", f"{guna_langsung:,.0f} Juta")
    c1.metric("Jasa Lingkungan", f"{jasa_ling:,.0f} Juta")
    c2.metric("Nilai Pilihan", f"{nilai_pilihan:,.0f} Juta")
    c2.metric("Nilai Eksistensi", f"{nilai_eksis:,.0f} Juta")
    st.success(f"### TOTAL TEV: Rp {guna_langsung + jasa_ling + nilai_pilihan + nilai_eksis:,.0f} Juta")

elif menu == "4. Trade-off Lahan":
    st.header("Simulasi Trade-off Lahan ⚖️")
    v1 = st.slider("Nilai Hutan Lestari (Milyar)", 10, 200, 100)
    v2 = st.slider("Nilai Konversi Lahan Penduduk (Milyar)", 10, 200, 70)
    
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.barh(['Hutan Lestari', 'Konversi Lahan'], [v1, v2], color=['#1a5227', '#bd623b'])
    st.pyplot(fig)

elif menu == "5. Kebijakan PES":
    st.header("Kebijakan Payment for Ecosystem Services (PES) 💧")
    st.markdown("Pihak pemanfaat: BPAB-DC, PDAM Tirtawening, dan PLTA Dago Bengkok.")
    penggunaan = st.number_input("Debit Air yang Dimanfaatkan (m3/thn)", value=5000000)
    tarif = st.slider("Tarif Jasa Lingkungan (Rp/m3)", 100, 1000, 250)
    st.metric("Total Kompensasi Jasa Air", f"Rp {penggunaan * tarif:,.0f}")

elif menu == "6. Kasus Interaktif":
    st.header("Kasus Interaktif Tahura 🐒")
    st.info("Analisis peran Tahura sebagai penyangga kehidupan Kota Bandung melalui mekanisme PES dan ekowisata.")
    st.table(pd.DataFrame({
        "Sektor": ["Penyediaan Air", "Ekowisata", "Mitigasi Bencana"],
        "Pemanfaat": ["PDAM/Masyarakat", "Wisatawan", "Cekungan Bandung"]
    }))

elif menu == "7. Visualisasi TEV":
    st.header("Visualisasi TEV 📊")
    factor = st.session_state.luas * (st.session_state.kerapatan / 100)
    vals = [factor * 25, factor * 45, factor * 15, factor * 15]
    
    fig, ax = plt.subplots()
    ax.pie(vals, labels=['Langsung', 'Jasa Ling', 'Pilihan', 'Eksistensi'], autopct='%1.1f%%')
    st.pyplot(fig)
