import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Konfigurasi Halaman Utama
st.set_page_config(
    page_title="PBL 6 - TEV Tahura Ir. H. Juanda",
    page_icon="🌳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inisialisasi Session State untuk Kalkulator TEV agar nilainya sinkron ke menu Visualisasi
if 'direct_tourism' not in st.session_state:
    st.session_state['direct_tourism'] = 7500000000
    st.session_state['direct_products'] = 500000000
    st.session_state['indirect_water'] = 12000000000
    st.session_state['indirect_carbon'] = 4500000000
    st.session_state['option_value'] = 2000000000
    st.session_state['existence_value'] = 3500000000

# Navigasi Sidebar
st.sidebar.title("📌 Menu Navigasi")
menu = st.sidebar.radio(
    "Pilih Halaman:",
    [
        "1. Beranda",
        "2. Profil Tahura Ir. H. Juanda",
        "3. Kalkulator TEV",
        "4. Trade-off Lahan",
        "5. Kebijakan PES",
        "6. Kasus Interaktif",
        "7. Visualisasi Grafik TEV"
    ]
)

# -----------------------------------------------------------------------------
# MENU 1: BERANDA
# -----------------------------------------------------------------------------
if menu == "1. Beranda":
    st.title("🌳 Ekonomi Sumber Daya Alam dan Lingkungan")
    st.subheader("Project-Based Learning (PBL) 6")
    st.markdown("---")
    
    # Menggunakan layout kolom untuk tampilan yang rapi
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.info("### 👋 Selamat Datang di Aplikasi Analisis Ekonomi Lingkungan Tahura Ir. H. Juanda")
        st.write(
            "Aplikasi ini dibuat untuk memenuhi tugas PBL 6 mata kuliah Ekonomi Sumber Daya Alam "
            "dan Lingkungan. Di sini, Anda dapat mempelajari profil kawasan, mensimulasikan nilai ekonomi "
            "total (TEV), menganalisis trade-off alih fungsi lahan, serta memahami kebijakan imbal jasa "
            "lingkungan (PES)."
        )
        
    with col2:
        st.success("### 👥 Identitas Kelompok 3")
        st.markdown(
            """
            * **Ahmad Irvan Nur Varizki** (10090224011)  
            * **Freya Helga Pebrian** (10090224017)  
            * **Muhammad Yaasin As-Suhaimi** (10090224028)  
            
            **Dosen Pengampu:** Yuhka Sundaya, S.E., M.S.i
            """
        )

# -----------------------------------------------------------------------------
# MENU 2: PROFIL TAHURA
# -----------------------------------------------------------------------------
elif menu == "2. Profil Taman Hutan Raya Ir. H. Juanda":
    st.title("ℹ️ Profil Taman Hutan Raya Ir. H. Juanda")
    st.markdown("---")
    
    tab1, tab2, tab3 = st.tabs(["📌 Sejarah & Geografis", "🌿 Kekayaan Flora", "🐒 Habitat Fauna"])
    
    with tab1:
        st.markdown("### Sejarah dan Letak Geografis")
        st.write(
            "Taman Hutan Raya (Tahura) Ir. H. Djuanda merupakan kawasan pelestarian alam sekaligus "
            "Taman Hutan Raya pertama di Indonesia yang diresmikan oleh Presiden Soeharto pada tanggal "
            "14 Januari 1985. Berlokasi di kawasan Ciburial, Kecamatan Cimenyan, Bandung, Jawa Barat, "
            "kawasan ini dinamai demikian untuk menghormati jasa pahlawan nasional Ir. H. Djuanda. "
            "Secara geografis, Tahura Ir. H. Djuanda memiliki bentang lahan seluas kurang lebih 590 hektare "
            "yang berada pada ketinggian antara 770 hingga 1.330 meter di atas permukaan laut. Kawasan yang "
            "terletak di cekungan Bandung Purba ini tidak hanya berfungsi sebagai destinasi wisata sejarah "
            "dan alam—seperti keberadaan Gua Belanda dan Gua Jepang—tetapi juga memegang peran ekologis "
            "yang sangat krusial sebagai daerah tangkapan air utama untuk aliran Sungai Cikapundung."
        )
        
    with tab2:
        st.markdown("### Data Tutupan Lahan dan Keanekaragaman Flora")
        st.write(
            "Sebagai area konservasi, data tutupan lahan di Tahura Ir. H. Djuanda menyimpan kekayaan botani "
            "yang sangat luar biasa. Di dalam kawasan hutan seluas 590 hektare tersebut, tercatat ada lebih "
            "dari 2.500 jenis flora yang mewakili sekitar 40 famili tumbuhan. Vegetasi yang tumbuh di kawasan "
            "ini merupakan perpaduan antara hutan alam sekunder dan koleksi tanaman dari berbagai wilayah. "
            "Beberapa jenis flora yang paling mendominasi dan membentuk kanopi utama hutan ini antara lain "
            "adalah pohon pinus (*Pinus merkusii*), berbagai jenis bambu, dan kaliandra. Selain itu, kawasan "
            "ini juga menyimpan koleksi berbagai pohon langka dan eksotis yang sebagian di antaranya merupakan "
            "hasil kerja sama botani dengan Kebun Raya Bogor pada masa lampau."
        )
        
    with tab3:
        st.markdown("### Ekosistem dan Kekayaan Fauna")
        st.write(
            "Di samping kekayaan floranya, lebatnya hutan di Tahura Ir. H. Djuanda juga menjadi habitat "
            "alami yang aman bagi berbagai spesies fauna liar. Satwa mamalia yang paling mendominasi dan sering "
            "berinteraksi langsung dengan pengunjung adalah kawanan kera ekor panjang atau monyet kra "
            "(*Macaca fascicularis*). Selain primata tersebut, ekosistem hutan ini juga menjadi rumah bagi "
            "mamalia kecil lainnya seperti tupai dan musang. Bagi para pencinta burung, kawasan ini menyimpan "
            "keanekaragaman avifauna yang menarik; tercatat banyak spesies burung yang hidup bebas di sini, seperti "
            "burung kepodang yang memiliki warna mencolok, burung ketilang yang rajin berkicau, hingga ayam hutan yang "
            "sering berkeliaran di semak-semak kawasan hutan yang lebih dalam."
        )
# -----------------------------------------------------------------------------
# MENU 3: KALKULATOR TEV
# -----------------------------------------------------------------------------
elif menu == "3. Kalkulator TEV":
    st.title("🧮 Kalkulator Total Economic Valuation (TEV)")
    st.write("Simulasikan perkiraan nilai ekonomi dari fungsi dan manfaat Tahura Ir. H. Juanda per tahun.")
    st.markdown("---")
    
    st.warning("Catatan: Angka di bawah ini adalah estimasi awal untuk simulasi pembelajaran ekonomi lingkungan. Anda dapat merubah nilainya sesuai data ril riset terbaru.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 1. Nilai Guna Langsung (Direct Use Value)")
        st.session_state['direct_tourism'] = st.number_input("Manfaat Wisata & Retribusi (Rp/tahun)", value=st.session_state['direct_tourism'], step=500000000)
        st.session_state['direct_products'] = st.number_input("Hasil Hutan Bukan Kayu & Bibit (Rp/tahun)", value=st.session_state['direct_products'], step=50000000)
        
        st.markdown("#### 2. Jasa Lingkungan / Guna Tidak Langsung (Indirect Use Value)")
        st.session_state['indirect_water'] = st.number_input("Penyediaan Air Bersih & Hidrologi (Rp/tahun)", value=st.session_state['indirect_water'], step=1000000000)
        st.session_state['indirect_carbon'] = st.number_input("Penyimpanan Karbon & Serapan Oksigen (Rp/tahun)", value=st.session_state['indirect_carbon'], step=500000000)

    with col2:
        st.markdown("#### 3. Nilai Pilihan (Option Value)")
        st.session_state['option_value'] = st.number_input("Potensi Pemanfaatan & Farmasi Masa Depan (Rp/tahun)", value=st.session_state['option_value'], step=200000000)
        
        st.markdown("#### 4. Nilai Eksistensi (Existence Value)")
        st.session_state['existence_value'] = st.number_input("Nilai Keberadaan Flora & Fauna Langka (Rp/tahun)", value=st.session_state['existence_value'], step=500000000)

    # Perhitungan TEV
    tev_total = (st.session_state['direct_tourism'] + st.session_state['direct_products'] + 
                 st.session_state['indirect_water'] + st.session_state['indirect_carbon'] + 
                 st.session_state['option_value'] + st.session_state['existence_value'])
    
    st.markdown("---")
    st.metric(label="💰 TOTAL ECONOMIC VALUE (TEV) TAHURA", value=f"Rp {tev_total:,.0f}")
    st.success("Nilai ini tersimpan otomatis dan dapat dilihat visualisasinya pada grafik di menu nomor 7.")

# -----------------------------------------------------------------------------
# MENU 4: TRADE-OFF LAHAN
# -----------------------------------------------------------------------------
elif menu == "4. Trade-off Lahan":
    st.title("⚖️ Analisis Keseimbangan / Trade-off Lahan")
    st.markdown("---")
    
    st.write(
        "Menu ini menganalisis skenario perbandingan jika sebagian area luar atau penyangga "
        "Tahura dikonversi menjadi lahan pemukiman/wisata komersial penduduk dibandingkan jika dipertahankan "
        "sebagai Hutan Lestari."
    )
    
    # Hitung TEV dari session state saat ini
    tev_sekarang = (st.session_state['direct_tourism'] + st.session_state['direct_products'] + 
                    st.session_state['indirect_water'] + st.session_state['indirect_carbon'] + 
                    st.session_state['option_value'] + st.session_state['existence_value'])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🌲 Nilai Hutan Lestari")
        st.write("Manfaat mencakup seluruh instrumen ekologis, ekonomi berkelanjutan, dan perlindungan DAS.")
        st.metric(label="Nilai Manfaat Hutan (TEV)", value=f"Rp {tev_sekarang:,.0f}")
        
    with col2:
        st.subheader("🏘️ Nilai Konversi Lahan Penduduk")
        luas_konversi = st.slider("Luas lahan yang diasumsikan dikonversi (Hektar)", 1, 100, 20)
        harga_lahan = st.number_input("Perkiraan Nilai Ekonomi Hasil Konversi (Rp / Hektar / Tahun)", value=250000000, step=50000000)
        
        total_konversi = luas_konversi * harga_lahan
        st.metric(label="Total Manfaat Ekonomi Konversi", value=f"Rp {total_konversi:,.0f}")
        
    st.markdown("### Kesimpulan Analisis Ekonomi")
    selisih = tev_sekarang - total_konversi
    if selisih > 0:
        st.success(f"**Pertahankan Hutan!** Keuntungan melestarikan hutan jauh lebih besar sebesar **Rp {selisih:,.0f}** per tahun dibandingkan melakukan konversi lahan.")
    else:
        st.danger(f"**Peringatan Komersialisasi Berlebih!** Secara jangka pendek nilai ekonomi konversi lebih tinggi sebesar **Rp {abs(selisih):,.0f}**, namun kehilangan fungsi ekologi jangka panjang (banjir, hilangnya mata air) belum terhitung sepenuhnya dalam kalkulasi konversi warga.")

# -----------------------------------------------------------------------------
# MENU 5: KEBIJAKAN PES
# -----------------------------------------------------------------------------
elif menu == "5. Kebijakan PES":
    st.title("💧 Kebijakan Payment for Ecosystem Services (PES)")
    st.markdown("---")
    
    st.write(
        "Tahura Ir. H. Djuanda bukan sekadar kawasan konservasi, melainkan 'penyangga kehidupan' "
        "(khususnya cadangan air) bagi Kota Bandung dan sekitarnya. Berdasarkan studi-studi ekonomi sumber daya, "
        "terdapat beberapa pihak yang secara langsung memanfaatkan jasa lingkungan dari kawasan ini:"
    )
    
    st.info(
        "🔹 **Sumber Daya Air:** Pemanfaatan air oleh masyarakat (BPAB-DC), PDAM Tirtawening Kota Bandung "
        "untuk kebutuhan air bersih warga Bandung Utara, serta penggunaan air dari Sungai Cikapundung oleh "
        "PLTA Dago Bengkok untuk pembangkit listrik.\n\n"
        "🔹 **Jasa Wisata:** Pemanfaatan kawasan untuk ekowisata, penelitian, dan rekreasi yang diatur melalui "
        "tarif retribusi daerah."
    )
    
    st.subheader("🎛️ Simulasi Kebijakan Tarif Jasa Lingkungan Air Bersih (PES)")
    st.write("Bagaimana jika pengguna air memberikan kontribusi langsung (retribusi konservasi) untuk menjaga hulu sungai di Tahura?")
    
    vol_air = st.number_input("Volume Penggunaan Air oleh PDAM / Masyarakat per Tahun (m³)", value=15000000, step=1000000)
    tarif_pes = st.slider("Besaran Tarif PES Konservasi Air yang disarankan (Rp per m³)", 50, 500, 150)
    
    dana_pes = vol_air * tarif_pes
    st.success(f"💰 **Total Potensi Dana Konservasi Terkumpul:** Rp {dana_pes:,.0f} / tahun")
    st.caption("Dana ini dapat dialokasikan kembali untuk reboisasi, peningkatan keamanan hutan, dan pemberdayaan masyarakat sekitar hutan agar tidak merusak vegetasi hulu.")

# -----------------------------------------------------------------------------
# MENU 6: KASUS INTERAKTIF
# -----------------------------------------------------------------------------
elif menu == "6. Kasus Interaktif":
    st.title("🎮 Kasus Interaktif: Dilema Pengelolaan Tahura Djuanda")
    st.markdown("---")
    
    st.write(
        "Sebagai Manajer Kawasan atapun Pengambil Kebijakan di Pemprov Jawa Barat, "
        "Anda dihadapkan pada skenario nyata berikut. Pilihlah keputusan yang paling bijak!"
    )
    
    st.subheader("Kasus: Lonjakan Pembangunan Villa & Wisata Komersial di Zona Penyangga Ciburial")
    st.write(
        "Pertumbuhan properti di sekitar area Cimenyan berkembang pesat. Investor menawarkan "
        "dana hibah pembangunan fasilitas pariwisata modern bernilai miliaran, namun berisiko memotong 10 hektar hutan pinus "
        "dan mengganggu jalur daerah tangkapan air Sungai Cikapundung."
    )
    
    pilihan = st.radio(
        "Apa tindakan strategis yang akan Anda ambil?",
        [
            "Pilihan A: Menerima investasi penuh demi mendongkrak PAD (Pendapatan Asli Daerah) dari sektor pariwisata.",
            "Pilihan B: Menolak tegas investasi dan memperketat zonasi serta memberlakukan denda berat bagi pelanggaran tutupan lahan.",
            "Pilihan C: Menggunakan konsep Green Tourism, membatasi luas bangunan komersial, dan mewajibkan investor membayar skema PES tahunan untuk pemeliharaan hulu sungai Cikapundung."
        ]
    )
    
    if st.button("Kirim Keputusan"):
        if pilihan == "Pilihan A":
            st.error(
                "❌ **Dampak Keputusan A:** Meskipun nilai guna langsung pariwisata meningkat di tahun-tahun awal, "
                "terjadi degradasi parah pada jasa lingkungan (banjir bandang di hilir Sungai Cikapundung dan penurunan volume air bersih). "
                "Nilai Eksistensi keanekaragaman hayati turun drastis karena kera ekor panjang mulai masuk ke pemukiman warga akibat kehilangan habitat."
            )
        elif pilihan == "Pilihan B":
            st.warning(
                "⚠️ **Dampak Keputusan B:** Kelestarian alam dan suplai air terjaga 100%. "
                "Namun, daerah kehilangan potensi pertumbuhan ekonomi, dan masyarakat sekitar tidak mendapatkan lapangan pekerjaan baru dari industri pariwisata."
            )
        else:
            st.success(
                "✅ **Dampak Keputusan C (Pilihan Terbaik!):** Ini adalah pendekatan Ekonomi Lingkungan yang berimbang! "
                "Anda menerapkan pembangunan berkelanjutan (*Sustainable Development*). Perekonomian tetap bergerak berkat pariwisata hijau, "
                "sementara kelestarian ekosistem dan pasokan air PDAM tetap terjamin melalui pendanaan skema PES."
            )

# -----------------------------------------------------------------------------
# MENU 7: VISUALISASI TEV BERUPA GRAFIK
# -----------------------------------------------------------------------------
elif menu == "7. Visualisasi Grafik TEV":
    st.title("📊 Visualisasi Hasil Pengukuran Nilai Ekonomi Total (TEV)")
    st.write("Grafik interaktif yang menyajikan kontribusi dari setiap komponen nilai ekonomi di Tahura Ir. H. Juanda.")
    st.markdown("---")
    
    # Menyiapkan data dari kalkulator
    data_tev = {
        'Komponen Nilai': [
            'Wisata & Retribusi (Direct)', 
            'Hasil Hutan Bukan Kayu (Direct)', 
            'Penyediaan Air Bersih (Indirect)', 
            'Penyimpanan Karbon (Indirect)', 
            'Potensi Masa Depan (Option)', 
            'Eksistensi Flora & Fauna (Existence)'
        ],
        'Kategori': ['Nilai Guna Langsung', 'Nilai Guna Langsung', 'Jasa Lingkungan', 'Jasa Lingkungan', 'Nilai Pilihan', 'Nilai Eksistensi'],
        'Nilai (Rp)': [
            st.session_state['direct_tourism'],
            st.session_state['direct_products'],
            st.session_state['indirect_water'],
            st.session_state['indirect_carbon'],
            st.session_state['option_value'],
            st.session_state['existence_value']
        ]
    }
    
    df = pd.DataFrame(data_tev)
    df['Persentase (%)'] = (df['Nilai (Rp)'] / df['Nilai (Rp)'].sum()) * 100
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Distribusi Komponen Nilai (Pie Chart)")
        fig_pie = px.pie(
            df, 
            values='Nilai (Rp)', 
            names='Komponen Nilai', 
            color_discrete_sequence=px.colors.sequential.Darkmint,
            hole=0.3
        )
        st.plotly_chart(fig_pie, use_container_width=True)
        
    with col2:
        st.subheader("2. Perbandingan Nilai Rupiah (Bar Chart)")
        fig_bar = px.bar(
            df, 
            x='Komponen Nilai', 
            y='Nilai (Rp)', 
            color='Kategori',
            text_auto='.2s',
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        fig_bar.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_bar, use_container_width=True)

    st.subheader("📑 Tabel Data Rincian TEV")
    st.dataframe(df.style.format({'Nilai (Rp)': 'Rp {:,.0f}', 'Persentase (%)': '{:.2f}%'}))
