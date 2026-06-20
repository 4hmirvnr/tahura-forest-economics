import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Konfigurasi Halaman
st.set_page_config(page_title="Valuasi Ekonomi Tahura Djuanda", page_icon="🌲", layout="wide")

# Sidebar Navigasi - 4 Pilar Utama
st.sidebar.title("🌲 Menu Navigasi")
menu = st.sidebar.radio("Pilih Modul Pembelajaran:", 
    ["Modul 1: Kalkulator TEV", 
     "Modul 2: Simulasi Trade-off", 
     "Modul 3: Kebijakan PES", 
     "Modul 4: Kasus Interaktif Tahura"]
)

st.sidebar.markdown("---")
st.sidebar.info("Aplikasi Pembelajaran Ekonomi Sumber Daya Hutan berdasarkan Analisis Teoretis Tietenberg & Lewis (Chapter 13).")

# ==========================================
# MODUL 1: KALKULATOR TEV
# ==========================================
if menu == "Modul 1: Kalkulator TEV":
    st.header("Modul 1: Kalkulator Total Economic Value (TEV) 🧮")
    st.markdown("Modul ini mengukur nilai guna langsung, tidak langsung, nilai pilihan, dan nilai eksistensi hutan secara kuantitatif.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Parameter Hutan")
        # Luas Tahura Djuanda sekitar 528 Hektar
        luas = st.number_input("Luas Lahan (Hektar)", min_value=1, max_value=10000, value=528)
        kerapatan = st.slider("Kerapatan Vegetasi (%)", 10, 100, 80)
        
        # Asumsi dasar valuasi per hektar per tahun (dalam juta rupiah)
        base_value_per_ha = 50 * (kerapatan / 100) 
        total_value = luas * base_value_per_ha
        
    with col2:
        st.subheader("Komposisi TEV Hutan Tropis Ideal")
        # Komposisi berdasarkan PPT
        data_tev = {
            "Kategori": [
                "Nilai Guna Langsung (Kayu/Buah) - 25%", 
                "Nilai Pengaturan & Air (Regulating) - 45%", 
                "Nilai Pilihan Masa Depan (Option) - 15%", 
                "Nilai Eksistensi Keanekaragaman - 15%"
            ],
            "Persentase": [25, 45, 15, 15],
            "Nilai Estimasi (Juta Rp)": [
                total_value * 0.25,
                total_value * 0.45,
                total_value * 0.15,
                total_value * 0.15
            ]
        }
        df_tev = pd.DataFrame(data_tev)
        st.dataframe(df_tev.style.format({"Nilai Estimasi (Juta Rp)": "{:,.2f}"}), use_container_width=True)
        st.metric(label="Total Economic Value (TEV) per Tahun", value=f"Rp {total_value:,.2f} Juta")

    st.info("💡 **Insight Ekonomi:** Sebagian besar nilai ekonomi hutan justru terletak pada jasa pengatur hidrologi dan karbon (45%), bukan pada pemanfaatan kayu komersial langsung (25%).")

# ==========================================
# MODUL 2: TRADE-OFF LOKAL
# ==========================================
elif menu == "Modul 2: Simulasi Trade-off":
    st.header("Modul 2: Simulasi Trade-off Lahan ⚖️")
    st.markdown("Membandingkan ekonomi konversi lahan vs mempertahankan kelestarian Tahura Ir. H. Djuanda.")
    
    st.subheader("Sisi Eksploitasi vs Sisi Konservasi Berkelanjutan")
    
    # Visualisasi Bar Chart Sederhana
    categories = ['Hutan Lestari (TEV)', 'Hasil Kayu/Komersial Saja', 'Konversi Komersial/Pariwisata Masif']
    values = [95, 40, 65] # Data berdasarkan referensi PPT
    
    fig, ax = plt.subplots(figsize=(10, 4))
    colors = ['#1a5227', '#7b8494', '#bd623b']
    bars = ax.barh(categories, values, color=colors)
    ax.set_xlabel('Nilai Ekonomi (Milyar Rp / Tahun)')
    ax.invert_yaxis()  # Label dari atas ke bawah
    
    # Menambahkan label nilai pada bar
    for bar in bars:
        width = bar.get_width()
        ax.annotate(f'{width}M / Thn',
                    xy=(width, bar.get_y() + bar.get_height() / 2),
                    xytext=(-3, 0),  
                    textcoords="offset points",
                    ha='right', va='center', color='white', fontweight='bold')

    st.pyplot(fig)
    
    st.warning("⚠️ **Analisis:** Jika hanya menghitung nilai ekstraktif jangka pendek, konversi terlihat menguntungkan (65M). Namun, dengan menghitung Total Economic Value (TEV) yang mencakup jasa lingkungan pelindung banjir untuk kawasan cekungan Bandung, kelestarian hutan jauh lebih unggul secara sosial dan ekonomi (95M).")

# ==========================================
# MODUL 3: KEBIJAKAN PES
# ==========================================
elif menu == "Modul 3: Kebijakan PES":
    st.header("Modul 3: Payment for Ecosystem Services (PES) 💧🍃")
    st.markdown("Simulasi insentif pasar karbon dan pembayaran jasa air bersih di DAS Cikapundung.")
    
    st.write("Sistem akan menghitung secara real-time titik keseimbangan finansial untuk mencegah deforestasi.")
    
    col_pes1, col_pes2 = st.columns(2)
    with col_pes1:
        harga_karbon = st.slider("Harga Karbon ($/Ton CO2)", 1, 50, 15)
        serapan_ton = st.number_input("Estimasi Serapan Karbon Tahura (Ton/Tahun)", value=12000)
        
        tarif_air = st.slider("Tarif Jasa Lingkungan Air Bersih (Rp/m3)", 100, 1000, 250)
        volume_air = st.number_input("Debit Air yang Dimanfaatkan (m3/Tahun)", value=5000000)
        
    with col_pes2:
        pendapatan_karbon_rp = (harga_karbon * serapan_ton) * 15500 # Asumsi kurs 15.500
        pendapatan_air_rp = tarif_air * volume_air
        total_pes = pendapatan_karbon_rp + pendapatan_air_rp
        
        st.success("### Total Potensi Dana PES")
        st.metric(label="Kredit Karbon", value=f"Rp {pendapatan_karbon_rp / 1e6:,.2f} Juta")
        st.metric(label="Jasa Air Bersih", value=f"Rp {pendapatan_air_rp / 1e6:,.2f} Juta")
        st.metric(label="Total Kompensasi Finansial", value=f"Rp {total_pes / 1e6:,.2f} Juta")
        
        opportunity_cost = 5000000000 # Asumsi biaya peluang konversi 5 Milyar
        if total_pes > opportunity_cost:
            st.info("✅ **Keseimbangan Tercapai:** Dana kompensasi PES sudah melebihi daya tarik ekonomi dari konversi lahan/penebangan.")
        else:
            st.error("❌ **Defisit:** Perlu peningkatkan tarif jasa lingkungan atau harga karbon untuk mengamankan ekosistem.")

# ==========================================
# MODUL 4: KASUS INTERAKTIF TAHURA
# ==========================================
elif menu == "Modul 4: Kasus Interaktif Tahura":
    st.header("Modul 4: Eksplorasi Kasus Riil Tahura Ir. H. Djuanda 🐒🌲")
    st.markdown("Klasifikasi Database Jasa Lingkungan spesifik untuk Taman Hutan Raya Ir. H. Djuanda.")
    
    # Data diadaptasi dari PPT dan dikontekstualisasikan untuk Tahura
    kasus_data = {
        "Kategori Ekosistem": ["Provisioning", "Regulating", "Cultural", "Supporting"],
        "Definisi Singkat": [
            "Penyedia barang fisik langsung", 
            "Pengatur proses alamiah", 
            "Manfaat rekreasi & spiritual", 
            "Proses dasar kelangsungan hidup"
        ],
        "Konteks Tahura Djuanda": [
            "Getah pinus, air baku Sungai Cikapundung", 
            "Serapan karbon vegetasi rapat, pencegahan erosi hulu", 
            "Ekowisata Gua Jepang/Belanda, Penangkaran Rusa", 
            "Siklus nutrisi tanah hutan hujan tropis"
        ],
        "Metode Valuasi Ekonomi": [
            "Harga pasar komoditas (Market Price)", 
            "Biaya pengganti (Replacement Cost)", 
            "Metode Biaya Perjalanan (Travel Cost Method / WTP)", 
            "Valuasi tidak langsung (Indirect Valuation)"
        ]
    }
    
    st.table(pd.DataFrame(kasus_data))
    
    st.write("---")
    st.markdown("**Fase Evaluasi (Studi Kasus Lanjutan):** Pengguna dapat berlatih menerapkan metode *Travel Cost Method* (Biaya Perjalanan) dengan mengumpulkan data pengeluaran pengunjung wisata Tahura untuk mengetahui *Willingness To Pay* (WTP) aktual masyarakat Kota Bandung terhadap kelestarian kawasan konservasi ini.")