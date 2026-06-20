```python
import streamlit as st
import pandas as pd
import plotly.express as px

# ==================================================
# KONFIGURASI HALAMAN
# ==================================================

st.set_page_config(
    page_title="PBL 6 - Tahura Ir. H. Djuanda",
    page_icon="🌳",
    layout="wide"
)

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("🌳 Menu Navigasi")

menu = st.sidebar.selectbox(
    "Pilih Menu",
    [
        "Beranda",
        "Profil Tahura Ir. H. Djuanda",
        "Kalkulator TEV",
        "Trade-off Lahan",
        "Kebijakan PES",
        "Kasus Interaktif",
        "Visualisasi TEV"
    ]
)

# ==================================================
# BERANDA
# ==================================================

if menu == "Beranda":

    st.title("PBL 6 – Ekonomi Sumber Daya Alam dan Lingkungan")

    st.markdown("---")

    st.subheader("Identitas Kelompok 3")

    st.write("• Ahmad Irvan Nur Varizki (10090224011)")
    st.write("• Freya Helga Pebrian (10090224017)")
    st.write("• Muhammad Yaasin As-Suhaimi (10090224028)")

    st.markdown("### Dosen Pengampu")
    st.write("Yuhka Sundaya, S.E., M.Si")

    st.markdown("---")

    st.success(
        "Dashboard ini digunakan untuk menganalisis nilai ekonomi "
        "Taman Hutan Raya Ir. H. Djuanda menggunakan pendekatan "
        "Ekonomi Sumber Daya Alam dan Lingkungan."
    )

# ==================================================
# PROFIL TAHURA
# ==================================================

elif menu == "Profil Tahura Ir. H. Djuanda":

    st.title("Profil Taman Hutan Raya Ir. H. Djuanda")

    st.markdown("""
Taman Hutan Raya (Tahura) Ir. H. Djuanda merupakan kawasan pelestarian alam sekaligus
Taman Hutan Raya pertama di Indonesia yang diresmikan oleh Presiden Soeharto pada
tanggal 14 Januari 1985.

Berlokasi di kawasan Ciburial, Kecamatan Cimenyan, Bandung, Jawa Barat,
kawasan ini dinamai untuk menghormati jasa pahlawan nasional Ir. H. Djuanda.

Tahura Ir. H. Djuanda memiliki luas sekitar **590 hektare**
dengan ketinggian antara **770–1.330 mdpl**.

Selain menjadi destinasi wisata sejarah dan alam yang terkenal melalui
Gua Belanda dan Gua Jepang, kawasan ini juga berfungsi sebagai daerah
tangkapan air penting bagi Sungai Cikapundung.

### Flora

Terdapat lebih dari 2.500 jenis flora dari sekitar 40 famili tumbuhan.

Vegetasi dominan:

- Pinus (Pinus merkusii)
- Bambu
- Kaliandra
- Berbagai tanaman koleksi konservasi

### Fauna

Kawasan ini menjadi habitat bagi berbagai satwa liar seperti:

- Monyet ekor panjang (Macaca fascicularis)
- Tupai
- Musang
- Kepodang
- Burung ketilang
- Ayam hutan

Tahura memiliki fungsi ekologis penting sebagai penyedia jasa lingkungan,
penyimpan karbon, konservasi biodiversitas, dan penyedia sumber air bagi
wilayah Bandung Raya.
""")

# ==================================================
# KALKULATOR TEV
# ==================================================

elif menu == "Kalkulator TEV":

    st.title("Kalkulator Total Economic Value (TEV)")

    st.write("Masukkan nilai masing-masing komponen ekonomi (Rp/tahun).")

    wisata = st.number_input(
        "Nilai Wisata",
        value=4000000000,
        step=100000000
    )

    hasil_hutan = st.number_input(
        "Nilai Hasil Hutan Non Kayu",
        value=1000000000,
        step=100000000
    )

    air = st.number_input(
        "Nilai Penyediaan Air",
        value=7000000000,
        step=100000000
    )

    karbon = st.number_input(
        "Nilai Penyimpanan Karbon",
        value=5000000000,
        step=100000000
    )

    pilihan = st.number_input(
        "Nilai Pilihan",
        value=2000000000,
        step=100000000
    )

    eksistensi = st.number_input(
        "Nilai Eksistensi",
        value=3000000000,
        step=100000000
    )

    tev = (
        wisata
        + hasil_hutan
        + air
        + karbon
        + pilihan
        + eksistensi
    )

    st.markdown("---")

    st.metric(
        "Total Economic Value (TEV)",
        f"Rp {tev:,.0f}"
    )

# ==================================================
# TRADE OFF LAHAN
# ==================================================

elif menu == "Trade-off Lahan":

    st.title("Trade-off Pemanfaatan Lahan")

    tradeoff = pd.DataFrame({
        "Alternatif": [
            "Hutan Lestari",
            "Konversi Lahan Penduduk"
        ],
        "Nilai (Rp)": [
            22000000000,
            12000000000
        ]
    })

    st.dataframe(tradeoff)

    fig = px.bar(
        tradeoff,
        x="Alternatif",
        y="Nilai (Rp)",
        title="Perbandingan Nilai Ekonomi"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
Nilai ekonomi kawasan yang dipertahankan sebagai hutan lestari
lebih tinggi dibandingkan konversi lahan untuk permukiman.
Hal ini menunjukkan pentingnya mempertahankan fungsi ekologis
dan jasa lingkungan Tahura.
""")

# ==================================================
# KEBIJAKAN PES
# ==================================================

elif menu == "Kebijakan PES":

    st.title("Payment for Ecosystem Services (PES)")

    st.markdown("""
Tahura Ir. H. Djuanda merupakan penyangga kehidupan bagi Bandung Raya.

### Pihak yang Memanfaatkan Jasa Lingkungan

- BPAB-DC
- PDAM Tirtawening Kota Bandung
- PLTA Dago Bengkok
- Wisatawan
- Peneliti
- Masyarakat sekitar
""")

    jumlah = st.slider(
        "Jumlah Institusi Pembayar PES",
        1,
        10,
        4
    )

    iuran = st.number_input(
        "Iuran per Institusi (Rp/Tahun)",
        value=500000000
    )

    total_pes = jumlah * iuran

    st.metric(
        "Potensi Dana PES",
        f"Rp {total_pes:,.0f}"
    )

# ==================================================
# KASUS INTERAKTIF
# ==================================================

elif menu == "Kasus Interaktif":

    st.title("Kasus Interaktif Tahura Ir. H. Djuanda")

    st.warning("""
Pemerintah berencana membuka 100 hektare kawasan hutan
untuk pembangunan komersial.
""")

    pilihan = st.radio(
        "Pilih Kebijakan:",
        [
            "Tetap Konservasi",
            "Konversi Sebagian"
        ]
    )

    if pilihan == "Tetap Konservasi":

        st.success("""
Keanekaragaman hayati tetap terjaga.

Fungsi hidrologis tetap optimal.

Penyimpanan karbon tetap tinggi.

Nilai ekonomi jangka panjang lebih besar.
""")

    else:

        st.error("""
Pendapatan jangka pendek meningkat.

Risiko kerusakan lingkungan bertambah.

Cadangan air berpotensi menurun.

Nilai jasa lingkungan berkurang.
""")

# ==================================================
# VISUALISASI TEV
# ==================================================

elif menu == "Visualisasi TEV":

    st.title("Visualisasi Total Economic Value")

    data_tev = pd.DataFrame({
        "Komponen": [
            "Wisata",
            "Hasil Hutan",
            "Penyediaan Air",
            "Karbon",
            "Nilai Pilihan",
            "Nilai Eksistensi"
        ],
        "Nilai (Miliar Rp)": [
            4,
            1,
            7,
            5,
            2,
            3
        ]
    })

    fig1 = px.bar(
        data_tev,
        x="Komponen",
        y="Nilai (Miliar Rp)",
        title="Komponen TEV Tahura Ir. H. Djuanda"
    )

    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.pie(
        data_tev,
        names="Komponen",
        values="Nilai (Miliar Rp)",
        title="Proporsi Komponen TEV"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.dataframe(data_tev)
```
