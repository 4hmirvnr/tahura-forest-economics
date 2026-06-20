import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Konfigurasi Halaman
st.set_page_config(page_title="Valuasi Ekonomi Tahura Djuanda", layout="wide")

# ==========================================
# STATE MANAGEMENT
# ==========================================
if 'luas' not in st.session_state: st.session_state.luas = 590
if 'kerapatan' not in st.session_state: st.session_state.kerapatan = 80

# Sidebar Navigasi
menu = st.sidebar.radio("Pilih Menu:", [
    "1. Beranda", "2. Profil Tahura", "3. Kalkulator TEV", 
    "4. Trade-off Lahan", "5. Kebijakan PES", "6. Kasus Interaktif", "7. Visualisasi TEV"
])

# ==========================================
# LOGIKA MENU
# ==========================================
if menu == "1. Beranda":
    st.title("PBL 6 - Ekonomi Sumber Daya Alam dan Lingkungan 🌍")
    st.markdown("### Identitas Kelompok 3")
    st.write("• Ahmad Irvan Nur Varizki (10090224011)")
    st.write("• Freya Helga Pebrian (10090224017)")
    st.write("• Muhammad Yaasin As-Suhaimi (10090224028)")
    st.write("**Dosen Pengampu:** Yuhka Sundaya, S.E., M.S.i")

elif menu == "2. Profil Tahura":
    st.title("Profil Taman Hutan Raya Ir. H. Juanda 🏞️")
    st.write("Tahura pertama di Indonesia, diresmikan 1985. Luas 590 Ha, elevasi 770-1330 mdpl.")
    st.write("Berfungsi sebagai daerah tangkapan air Sungai Cikapundung.")
    st.write("Kekayaan botani meliputi 2.500 jenis flora, dan habitat fauna seperti monyet kra, burung kepodang, dan tupai.")

elif menu == "3. Kalkulator TEV":
    st.header("Kalkulator TEV 🧮")
    st.session_state.luas = st.number_input("Luas Lahan (Ha)", value=st.session_state.luas)
    st.session_state.kerapatan = st.slider("Kerapatan Vegetasi (%)", 10, 100, st.session_state.kerapatan)
    
    factor = st.session_state.luas * (st.session_state.kerapatan / 100)
    manfaat_langsung = factor * 25
    manfaat_hidrologis = factor * 45
    nilai_warisan_eksistensi = factor * 30
    total = manfaat_langsung + manfaat_hidrologis + nilai_warisan_eksistensi
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Manfaat Langsung", f"{manfaat_langsung:,.0f} Juta")
    col2.metric("Manfaat Hidrologis", f"{manfaat_hidrologis:,.0f} Juta")
    col3.metric("Nilai Warisan/Eksistensi", f"{nilai_warisan_eksistensi:,.0f} Juta")
    st.success(f"TOTAL TEV: Rp {total:,.0f} Juta")

elif menu == "4. Trade-off Lahan":
    st.header("Simulasi Trade-off Lahan ⚖️")
    kayu = st.slider("Laba Komersial (Milyar)", 10, 100, 40)
    konversi = st.slider("Laba Konversi (Milyar)", 10, 150, 65)
    total_tev_m = (st.session_state.luas * (50 * (st.session_state.kerapatan / 100))) / 1000
    
    fig, ax = plt.subplots()
    ax.barh(['Hutan Lestari', 'Hasil Komersial', 'Konversi'], [total_tev_m, kayu, konversi], color=['green', 'gray', 'red'])
    st.pyplot(fig)

elif menu == "5. Kebijakan PES":
    st.header("Kebijakan Payment for Ecosystem Services (PES) 💧")
    harga_c = st.slider("Harga Karbon ($/Ton)", 1, 50, 15)
    tarif_air = st.slider("Tarif Air (Rp/m3)", 100, 1000, 250)
    total_pes = ((harga_c * 15000) * 15500) + (tarif_air * 5000000)
    st.metric("Total Potensi Dana PES (Rp)", f"{total_pes:,.0f}")

elif menu == "6. Kasus Interaktif":
    st.header("Kasus Interaktif Tahura 🐒")
    df = pd.DataFrame({
        "Kategori": ["Provisioning", "Regulating", "Cultural", "Supporting"],
        "Metode": ["Market Price", "Replacement Cost", "Travel Cost", "Indirect"]
    })
    st.table(df)

elif menu == "7. Visualisasi TEV":
    st.header("Visualisasi TEV 📊")
    factor = st.session_state.luas * (st.session_state.kerapatan / 100)
    sizes = [factor * 25, factor * 45, factor * 30]
    
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=['Langsung', 'Hidrologis', 'Warisan'], autopct='%1.1f%%')
    st.pyplot(fig)
