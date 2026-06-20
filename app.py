import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Konfigurasi Halaman
st.set_page_config(page_title="Valuasi Ekonomi Tahura Djuanda", page_icon="🌲", layout="wide")

# ==========================================
# STATE MANAGEMENT (PENTING AGAR DATA TERSINKRON)
# ==========================================
if 'luas' not in st.session_state: st.session_state.luas = 590
if 'kerapatan' not in st.session_state: st.session_state.kerapatan = 80
if 'kayu_val' not in st.session_state: st.session_state.kayu_val = 40
if 'konv_val' not in st.session_state: st.session_state.konv_val = 65

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
    st.write("Tahura pertama di Indonesia yang diresmikan oleh Presiden Soeharto pada 14 Januari 1985.")
    st.write("Memiliki luas ±590 Ha di ketinggian 770-1.330 mdpl, sebagai daerah tangkapan air Sungai Cikapundung.")
    st.write("Kekayaan flora mencapai 2.500 jenis dan habitat fauna seperti monyet kra, burung kepodang, dan tupai.")

elif menu == "3. Kalkulator TEV":
    st.header("Kalkulator Total Economic Value (TEV) 🧮")
    st.session_state.luas = st.number_input("Luas Lahan (Ha)", value=st.session_state.luas)
    st.session_state.kerapatan = st.slider("Kerapatan Vegetasi (%)", 10, 100, st.session_state.kerapatan)
    
    factor = st.session_state.luas * (st.session_state.kerapatan / 100)
    ml = factor * 25 # Manfaat Langsung
    mh = factor * 45 # Manfaat Hidrologis
    mw = factor * 30 # Nilai Warisan
    total = ml + mh + mw
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Manfaat Langsung", f"{ml:,.0f} Juta")
    c2.metric("Manfaat Hidrologis", f"{mh:,.0f} Juta")
    c3.metric("Nilai Warisan/Eksistensi", f"{mw:,.0f} Juta")
    st.success(f"### TOTAL TEV: Rp {total:,.0f} Juta/Tahun")

elif menu == "4. Trade-off Lahan":
    st.header("Simulasi Trade-off Lahan ⚖️")
    st.session_state.kayu_val = st.slider("Laba Hasil Komersial (Milyar/Thn)", 10, 100, st.session_state.kayu_val)
    st.session_state.konv_val = st.slider("Laba Konversi Wisata/Tambang (Milyar/Thn)", 10, 150, st.session_state.konv_val)
    
    tev_m = (st.session_state.luas * (50 * (st.session_state.kerapatan / 100))) / 1000
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.barh(['Hutan Lestari (TEV)', 'Hasil Komersial', 'Konversi'], [tev_m, st.session_state.kayu_val, st.session_state.konv_val], color=['#1a5227', '#7b8494', '#bd623b'])
    st.pyplot(fig)

elif menu == "5. Kebijakan PES":
    st.header("Kebijakan Payment for Ecosystem Services (PES) 💧")
    harga_c = st.slider("Harga Karbon ($/Ton)", 1, 50, 15)
    tarif_air = st.slider("Tarif Jasa Lingkungan Air (Rp/m3)", 100, 1000, 250)
    total_pes = ((harga_c * 15000) * 15500) + (tarif_air * 5000000)
    st.metric("Total Potensi Dana PES (Rp)", f"{total_pes:,.0f}")

elif menu == "6. Kasus Interaktif":
    st.header("Kasus Interaktif Tahura 🐒")
    st.table(pd.DataFrame({
        "Kategori": ["Provisioning", "Regulating", "Cultural", "Supporting"],
        "Metode Valuasi": ["Harga Pasar", "Replacement Cost", "Travel Cost", "Indirect"]
    }))

elif menu == "7. Visualisasi TEV":
    st.header("Visualisasi Proporsi TEV 📊")
    factor = st.session_state.luas * (st.session_state.kerapatan / 100)
    sizes = [factor * 25, factor * 45, factor * 30]
    
    c1, c2 = st.columns(2)
    with c1:
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=['Langsung', 'Hidrologis', 'Warisan'], autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99'])
        st.pyplot(fig1)
    with c2:
        fig2, ax2 = plt.subplots()
        ax2.bar(['Langsung', 'Hidrologis', 'Warisan'], sizes, color=['#ff9999','#66b3ff','#99ff99'])
        st.pyplot(fig2)
