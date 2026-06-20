import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Konfigurasi Halaman
st.set_page_config(page_title="Valuasi Ekonomi Tahura Djuanda", page_icon="🌲", layout="wide")

# Inisialisasi Session State agar data antar menu tersambung
if 'luas_lahan' not in st.session_state:
    st.session_state['luas_lahan'] = 590
if 'kerapatan' not in st.session_state:
    st.session_state['kerapatan'] = 80
if 'total_value' not in st.session_state:
    # 50 juta/ha asumsi dasar * rasio kerapatan
    st.session_state['total_value'] = 590 * (50 * (80 / 100))

# Sidebar Navigasi - 7 Pilihan Menu
st.sidebar.title("🌲 Navigasi Aplikasi")
menu = st.sidebar.radio("Pilih Menu:", [
    "1. Beranda", 
    "2. Profil Tahura Ir. H. Juanda", 
    "3. Kalkulator TEV", 
    "4. Trade-off Lahan", 
    "5. Kebijakan PES", 
    "6. Kasus Interaktif Tahura", 
    "7. Visualisasi TEV"
])

st.sidebar.markdown("---")
st.sidebar.info("Aplikasi Evaluasi Ekonomi Sumber Daya Hutan berdasarkan Analisis Teoretis Tietenberg & Lewis (Chapter 13).")

# ==========================================
# 1. BERANDA
# ==========================================
if menu == "1. Beranda":
    st.title("PBL 6  ̶  Ekonomi Sumber Daya Alam dan Lingkungan 🌍")
    st.markdown("---")
    
    st.subheader("Identitas Kelompok 3")
    st.markdown("""
    * **Ahmad Irvan Nur Varizki** (10090224011) 
    * **Freya Helga Pebrian** (10090224017) 
    * **Muhammad Yaasin As-Suhaimi** (10090224028)
    """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("**Dosen Pengampu:** Yuhka Sundaya, S.E., M.S.i")

# ==========================================
# 2. PROFIL TAHURA
# ==========================================
elif menu == "2. Profil Tahura Ir. H. Juanda":
    st.title("Profil Taman Hutan Raya Ir. H. Juanda 🏞️")
    
    st.markdown("""
    Taman Hutan Raya (Tahura) Ir. H. Djuanda merupakan kawasan pelestarian alam sekaligus Taman Hutan Raya pertama di Indonesia yang diresmikan oleh Presiden Soeharto pada tanggal 14 Januari 1985. Berlokasi di kawasan Ciburial, Kecamatan Cimenyan, Bandung, Jawa Barat, kawasan ini dinamai demikian untuk menghormati jasa pahlawan nasional Ir. H. Djuanda. Secara geografis, Tahura Ir. H. Djuanda memiliki bentang lahan seluas kurang lebih 590 hektare yang berada pada ketinggian antara 770 hingga 1.330 meter di atas permukaan laut. Kawasan yang terletak di cekungan Bandung Purba ini tidak hanya berfungsi sebagai destinasi wisata sejarah dan alam—seperti keberadaan Gua Belanda dan Gua Jepang—tetapi juga memegang peran ekologis yang sangat krusial sebagai daerah tangkapan air utama untuk aliran Sungai Cikapundung.
    
    Sebagai area konservasi, data tutupan lahan di Tahura Ir. H. Djuanda menyimpan kekayaan botani yang sangat luar biasa. Di dalam kawasan hutan seluas 590 hektare tersebut, tercatat ada lebih dari 2.500 jenis flora yang mewakili sekitar 40 famili tumbuhan. Vegetasi yang tumbuh di kawasan ini merupakan perpaduan antara hutan alam sekunder dan koleksi tanaman dari berbagai wilayah. Beberapa jenis flora yang paling mendominasi dan membentuk kanopi utama hutan ini antara lain adalah pohon pinus (*Pinus merkusii*), berbagai jenis bambu, dan kaliandra. Selain itu, kawasan ini juga menyimpan koleksi berbagai pohon langka dan eksotis yang sebagian di antaranya merupakan hasil kerja sama botani dengan Kebun Raya Bogor pada masa lampau.
    
    Di samping kekayaan floranya, lebatnya hutan di Tahura Ir. H. Djuanda juga menjadi habitat alami yang aman bagi berbagai spesies fauna liar. Satwa mamalia yang paling mendominasi dan sering berinteraksi langsung dengan pengunjung adalah kawanan kera ekor panjang atau monyet kra (*Macaca fascicularis*). Selain primata tersebut, ekosistem hutan ini juga menjadi rumah bagi mamalia kecil lainnya seperti tupai dan musang. Bagi para pencinta burung, kawasan ini menyimpan keanekaragaman avifauna yang menarik; tercatat banyak spesies burung yang hidup bebas di sini, seperti burung kepodang yang memiliki warna mencolok, burung ketilang yang rajin berkicau, hingga ayam hutan yang sering berkeliaran di semak-semak kawasan hutan yang lebih dalam.
    """)

# ==========================================
# 3. KALKULATOR TEV
# ==========================================
elif menu == "3. Kalkulator TEV":
    st.header("Kalkulator Total Economic Value (TEV) 🧮")
    st.markdown("Mengukur nilai guna langsung, tidak langsung, nilai pilihan, dan nilai eksistensi hutan secara kuantitatif.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Parameter Hutan")
        # Nilai default ditarik dari session_state
        luas = st.number_input("Luas Lahan (Hektar)", min_value=1, max_value=10000, value=st.session_state['luas_lahan'])
        kerapatan = st.slider("Kerapatan Vegetasi (%)", 10, 100, st.session_state['kerapatan'])
        
        # Hitung kalkulasi
        base_value_per_ha = 50 * (kerapatan / 100) 
        total_value = luas * base_value_per_ha
        
        # Simpan kembali ke session_state agar grafiknya update
        st.session_state['luas_lahan'] = luas
        st.session_state['kerapatan'] = kerapatan
        st.session_state['total_value'] = total_value
        
    with col2:
        st.subheader("Komposisi TEV Hutan Tropis Ideal")
        data_tev = {
            "Kategori": [
                "Nilai Guna Langsung (Kayu/Buah)", 
                "Nilai Pengaturan & Air (Regulating)", 
                "Nilai Pilihan Masa Depan (Option)", 
                "Nilai Eksistensi Keanekaragaman"
            ],
            "Persentase": ["25%", "45%", "15%", "15%"],
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

    st.info("💡 **Insight Ekonomi:** Sebagian besar nilai ekonomi Tahura terletak pada jasa pengatur hidrologi Sungai Cikapundung (45%), bukan pada pemanfaatan kayu atau getah pinus (25%).")

# ==========================================
# 4. TRADE-OFF LAHAN
# ==========================================
elif menu == "4. Trade-off Lahan":
    st.header("Simulasi Trade-off Lahan ⚖️")
    st.markdown("Membandingkan ekonomi konversi lahan vs mempertahankan kelestarian Tahura Ir. H. Djuanda.")
    
    st.subheader("Sisi Eksploitasi vs Sisi Konservasi Berkelanjutan")
    
    categories = ['Hutan Lestari (TEV)', 'Hasil Komersial Ekstraktif', 'Konversi Kawasan Komersial']
    
    # Asumsi skala nilai berdasarkan nilai TEV di session_state (dibagi 1000 agar jadi Milyar)
    nilai_lestari = st.session_state['total_value'] / 1000 
    values = [nilai_lestari, nilai_lestari * 0.4, nilai_lestari * 0.7] 
    
    fig, ax = plt.subplots(figsize=(10, 4))
    colors = ['#1a5227', '#7b8494', '#bd623b']
    bars = ax.barh(categories, values, color=colors)
    ax.set_xlabel('Nilai Ekonomi (Milyar Rp / Tahun)')
    ax.invert_yaxis()
    
    for bar in bars:
        width = bar.get_width()
        ax.annotate(f'{width:,.1f} M',
                    xy=(width, bar.get_y() + bar.get_height() / 2),
                    xytext=(-5, 0),  
                    textcoords="offset points",
                    ha='right', va='center', color='white', fontweight='bold')

    st.pyplot(fig)
    
    st.warning("⚠️ **Analisis:** Mengorbankan tutupan vegetasi hutan untuk pembangunan komersial memang memberi *cash flow* pasar yang cepat, namun mengabaikan eksternalitas negatif jangka panjang. Mempertahankan TEV (termasuk nilai hidrologi dan serapan karbon) jauh lebih unggul secara sosial dan ekonomi makro.")

# ==========================================
# 5. KEBIJAKAN PES
# ==========================================
elif menu == "5. Kebijakan PES":
    st.header("Payment for Ecosystem Services (PES) 💧🍃")
    st.markdown("Simulasi insentif pasar karbon dan pembayaran jasa lingkungan air bersih di DAS Cikapundung.")
    
    col_pes1, col_pes2 = st.columns(2)
    with col_pes1:
        harga_karbon = st.slider("Harga Karbon ($/Ton CO2)", 1, 50, 15)
        # Asumsi Tahura 590 Ha menyerap sekitar 15.000 ton
        serapan_ton = st.number_input("Estimasi Serapan Karbon Tahura (Ton/Tahun)", value=15000)
        
        tarif_air = st.slider("Tarif Jasa Lingkungan Air Bersih (Rp/m3)", 100, 1000, 250)
        volume_air = st.number_input("Debit Air Tahura yang Dimanfaatkan (m3/Tahun)", value=5000000)
        
    with col_pes2:
        pendapatan_karbon_rp = (harga_karbon * serapan_ton) * 15500 
        pendapatan_air_rp = tarif_air * volume_air
        total_pes = pendapatan_karbon_rp + pendapatan_air_rp
        
        st.success("### Total Potensi Dana PES")
        st.metric(label="Kredit Karbon", value=f"Rp {pendapatan_karbon_rp / 1e6:,.2f} Juta")
        st.metric(label="Jasa Air Bersih", value=f"Rp {pendapatan_air_rp / 1e6:,.2f} Juta")
        st.metric(label="Total Kompensasi Finansial", value=f"Rp {total_pes / 1e6:,.2f} Juta")
        
        opportunity_cost = 6000000000 # Asumsi nilai batas minimal kelayakan
        if total_pes > opportunity_cost:
            st.info("✅ **Keseimbangan Ekologis-Ekonomi Tercapai:** Dana kompensasi PES dapat diinvestasikan kembali untuk operasional perlindungan kawasan Tahura.")
        else:
            st.error("❌ **Defisit:** Nilai PES terlalu rendah, rentan terhadap tekanan alih fungsi lahan.")

# ==========================================
# 6. KASUS INTERAKTIF
# ==========================================
elif menu == "6. Kasus Interaktif Tahura":
    st.header("Kasus Interaktif Taman Hutan Raya Ir. H. Juanda 🐒🌲")
    st.markdown("Klasifikasi Database Jasa Lingkungan spesifik untuk kawasan konservasi ini.")
    
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
            "Serapan karbon kanopi hutan, pencegahan erosi cekungan Bandung", 
            "Ekowisata Gua Jepang/Belanda, Penangkaran Rusa, Interaksi Monyet Kra", 
            "Siklus nutrisi tanah hutan sekunder"
        ],
        "Metode Valuasi Ekonomi": [
            "Harga pasar (Market Price)", 
            "Biaya pengganti (Replacement Cost)", 
            "Travel Cost Method (TCM) / Willingness to Pay", 
            "Valuasi tidak langsung (Indirect Valuation)"
        ]
    }
    
    st.table(pd.DataFrame(kasus_data))

# ==========================================
# 7. VISUALISASI TEV
# ==========================================
elif menu == "7. Visualisasi TEV":
    st.header("Visualisasi Total Economic Value (TEV) 📊")
    st.markdown("Distribusi porsi nilai ekonomi Tahura berdasarkan parameter luas dan kerapatan dari Kalkulator TEV.")
    
    total = st.session_state['total_value']
    
    # Nilai komponen
    komponen = ['Guna Langsung (25%)', 'Regulating (45%)', 'Option Value (15%)', 'Existence Value (15%)']
    nilai = [total * 0.25, total * 0.45, total * 0.15, total * 0.15]
    
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.subheader("Proporsi TEV (Pie Chart)")
        fig1, ax1 = plt.subplots(figsize=(6, 6))
        colors_pie = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
        ax1.pie(nilai, labels=komponen, autopct='%1.1f%%', startangle=90, colors=colors_pie, textprops={'fontsize': 10})
        ax1.axis('equal')  
        st.pyplot(fig1)
        
    with col_chart2:
        st.subheader("Nilai Finansial (Bar Chart)")
        fig2, ax2 = plt.subplots(figsize=(6, 5))
        ax2.bar(komponen, nilai, color=colors_pie)
        ax2.set_ylabel('Juta Rupiah')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        st.pyplot(fig2)
        
    st.success(f"Berdasarkan simulasi saat ini, Total Economic Value Tahura Ir. H. Djuanda diestimasi mencapai **Rp {total:,.2f} Juta per tahun**.")
