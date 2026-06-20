import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Konfigurasi Halaman
st.set_page_config(page_title="Valuasi Ekonomi Tahura Djuanda", layout="wide")

# Sidebar Navigasi
st.sidebar.title("🌲 Navigasi")
menu = st.sidebar.radio("Pilih Menu:", [
    "1. Beranda", "2. Profil Tahura", "3. Kalkulator TEV", 
    "4. Trade-off Lahan", "5. Kebijakan PES", "6. Kasus Interaktif", "7. Visualisasi TEV"
])

# ==========================================
# INPUT INTERAKTIF (DISIMPAN DI SESSION STATE)
# ==========================================
if 'luas' not in st.session_state: st.session_state.luas = 590
if 'kerapatan' not in st.session_state: st.session_state.kerapatan = 80

# ==========================================
# LOGIKA MENU
# ==========================================
if menu == "1. Beranda":
    st.title("PBL 6 - Ekonomi Sumber Daya Alam")
    st.write("Kelompok 3: Ahmad Irvan, Freya Helga, Muhammad Yaasin")

elif menu == "3. Kalkulator TEV":
    st.header("Kalkulator Total Economic Value (TEV) 🧮")
    st.markdown("Input parameter hutan lokal untuk memproyeksikan nilai ekonomi total.")
    
    # Input Parameter
    st.session_state.luas = st.number_input("Luas Lahan (Ha)", value=st.session_state.luas)
    st.session_state.kerapatan = st.slider("Kerapatan Vegetasi (%)", 10, 100, st.session_state.kerapatan)
    
    # Faktor pengali (asumsi per hektar)
    factor = st.session_state.luas * (st.session_state.kerapatan / 100)
    
    # Perhitungan 3 Poin TEV
    manfaat_langsung = factor * 25  # Kayu & Non-kayu
    manfaat_hidrologis = factor * 45 # Hidrologis & Erosi
    nilai_warisan_eksistensi = factor * 30 # Warisan & Satwa
    
    total_tev = manfaat_langsung + manfaat_hidrologis + nilai_warisan_eksistensi
    
    # Tampilan Hasil
    col1, col2, col3 = st.columns(3)
    col1.metric("Manfaat Langsung (Juta Rp)", f"{manfaat_langsung:,.0f}")
    col2.metric("Manfaat Hidrologis (Juta Rp)", f"{manfaat_hidrologis:,.0f}")
    col3.metric("Nilai Warisan & Satwa (Juta Rp)", f"{nilai_warisan_eksistensi:,.0f}")
    
    st.markdown("---")
    st.metric("TOTAL ECONOMIC VALUE (TEV)", f"Rp {total_tev:,.0f} Juta")
    
    st.info("""
    **Penjelasan Komponen:**
    1. **Manfaat Langsung**: Estimasi nilai pasar dari hasil hutan kayu dan bukan kayu (buah/getah). [cite: 42]
    2. **Manfaat Hidrologis**: Estimasi nilai ekonomi dari jasa perlindungan tata air dan pencegahan erosi tanah. [cite: 42]
    3. **Nilai Warisan & Eksistensi**: Nilai ekonomi yang mencerminkan keberadaan satwa liar dan hak generasi mendatang untuk menikmati hutan (bequest value). [cite: 43]
    """)

elif menu == "7. Visualisasi TEV":
    st.header("Visualisasi TEV")
    
    # HITUNG ULANG DI SINI AGAR SELALU UPDATE
    total = st.session_state.luas * (50 * (st.session_state.kerapatan / 100))
    
    labels = ['Guna Langsung', 'Regulating', 'Option Value', 'Existence']
    sizes = [total * 0.25, total * 0.45, total * 0.15, total * 0.15]
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
        st.pyplot(fig1)
        
    with col2:
        fig2, ax2 = plt.subplots()
        ax2.bar(labels, sizes, color=['red', 'blue', 'green', 'orange'])
        ax2.set_ylabel('Juta Rupiah')
        st.pyplot(fig2)

    st.success(f"Total TEV saat ini: Rp {total:,.2f} Juta")
