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
    st.header("Kalkulator TEV")
    st.session_state.luas = st.number_input("Luas Lahan (Ha)", value=st.session_state.luas)
    st.session_state.kerapatan = st.slider("Kerapatan (%)", 10, 100, st.session_state.kerapatan)
    
    total = st.session_state.luas * (50 * (st.session_state.kerapatan / 100))
    st.metric("Total TEV (Juta Rp)", f"{total:,.2f}")

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
