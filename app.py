import streamlit as st
import pandas as pd
import plotly.express as px

# =========================

# KONFIGURASI HALAMAN

# =========================

st.set_page_config(
page_title="Tahura Ir. H. Djuanda",
page_icon="🌳",
layout="wide"
)

# =========================

# SIDEBAR

# =========================

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

# =========================

# BERANDA

# =========================

if menu == "Beranda":

```
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
    "Dashboard ini menyajikan analisis ekonomi lingkungan "
    "Taman Hutan Raya Ir. H. Djuanda menggunakan pendekatan "
    "Total Economic Value (TEV)."
)
```

# =========================

# PROFIL TAHURA

# =========================

elif menu == "Profil Tahura Ir. H. Djuanda":

```
st.title("Profil Taman Hutan Raya Ir. H. Djuanda")

st.markdown("""
```

Taman Hutan Raya (Tahura) Ir. H. Djuanda merupakan kawasan pelestarian alam sekaligus
Taman Hutan Raya pertama di Indonesia yang diresmikan pada tanggal 14 Januari 1985.

Kawasan ini berlokasi di Ciburial, Kecamatan Cimenyan, Kabupaten Bandung, Jawa Barat.
Tahura memiliki luas sekitar **590 hektare** dan berada pada ketinggian **770–1.330 mdpl**.

Selain menjadi destinasi wisata alam dan sejarah melalui Gua Belanda dan Gua Jepang,
Tahura juga berfungsi sebagai daerah tangkapan air penting bagi Sungai Cikapundung.

### Flora Dominan

* Pinus (Pinus merkusii)
* Bambu
* Kaliandra
* Berbagai tanaman konservasi

### Fauna Dominan

* Monyet ekor panjang (Macaca fascicularis)
* Tupai
* Musang
* Burung ketilang
* Kepodang
* Ayam hutan

### Fungsi Ekologis

* Konservasi keanekaragaman hayati
* Penyimpan karbon
* Penyedia sumber daya air
* Kawasan wisata alam dan edukasi
  """)

# =========================

# KALKULATOR TEV

# =========================

elif menu == "Kalkulator TEV":

```
st.title("Kalkulator Total Economic Value (TEV)")

wisata = st.number_input(
    "Nilai Guna Langsung - Wisata (Rp)",
    value=4000000000
)

hasil_hutan = st.number_input(
    "Nilai Guna Langsung - Hasil Hutan (Rp)",
    value=1000000000
)

air = st.number_input(
    "Jasa Lingkungan - Penyediaan Air (Rp)",
    value=7000000000
)

karbon = st.number_input(
    "Jasa Lingkungan - Penyimpanan Karbon (Rp)",
    value=5000000000
)

nilai_pilihan = st.number_input(
    "Nilai Pilihan (Rp)",
    value=2000000000
)

nilai_eksistensi = st.number_input(
    "Nilai Eksistensi (Rp)",
    value=3000000000
)

tev = (
    wisata
    + hasil_hutan
    + air
    + karbon
    + nilai_pilihan
    + nilai_eksistensi
)

st.markdown("---")

st.metric(
    "Total Economic Value (TEV)",
    f"Rp {tev:,.0f}"
)
```

# =========================

# TRADE OFF LAHAN

# =========================

elif menu == "Trade-off Lahan":

```
st.title("Trade-off Pemanfaatan Lahan")

data_tradeoff = pd.DataFrame({
    "Alternatif": [
        "Hutan Lestari",
        "Konversi Lahan Penduduk"
    ],
    "Nilai (Miliar Rp/Tahun)": [
        22,
        12
    ]
})

st.dataframe(data_tradeoff)

fig = px.bar(
    data_tradeoff,
    x="Alternatif",
    y="Nilai (Miliar Rp/Tahun)",
    title="Perbandingan Nilai Ekonomi"
)

st.plotly_chart(fig, use_container_width=True)

st.info(
    "Nilai ekonomi hutan lestari lebih tinggi dibandingkan "
    "konversi lahan sehingga konservasi memberikan manfaat "
    "jangka panjang yang lebih besar."
)
```

# =========================

# KEBIJAKAN PES

# =========================

elif menu == "Kebijakan PES":

```
st.title("Payment for Ecosystem Services (PES)")

st.markdown("""
```

### Pemanfaat Jasa Lingkungan Tahura

* BPAB-DC
* PDAM Tirtawening Kota Bandung
* PLTA Dago Bengkok
* Wisatawan
* Peneliti
* Masyarakat sekitar

Tahura menyediakan jasa lingkungan berupa air bersih,
cadangan air, konservasi biodiversitas, dan jasa wisata.
""")

```
jumlah_pembayar = st.slider(
    "Jumlah Institusi Pembayar PES",
    1,
    10,
    4
)

iuran = st.number_input(
    "Iuran per Institusi (Rp/Tahun)",
    value=500000000
)

total_pes = jumlah_pembayar * iuran

st.metric(
    "Potensi Dana PES",
    f"Rp {total_pes:,.0f}"
)
```

# =========================

# KASUS INTERAKTIF

# =========================

elif menu == "Kasus Interaktif":

```
st.title("Kasus Interaktif Tahura Ir. H. Djuanda")

st.warning(
    "Pemerintah berencana membuka 100 hektare kawasan "
    "untuk pembangunan komersial."
)

pilihan = st.radio(
    "Pilih Kebijakan",
    [
        "Tetap Konservasi",
        "Konversi Sebagian"
    ]
)

if pilihan == "Tetap Konservasi":

    st.success("""
```

Keanekaragaman hayati tetap terjaga.

Cadangan air tetap stabil.

Penyimpanan karbon tetap tinggi.

Manfaat ekonomi jangka panjang lebih besar.
""")

```
else:

    st.error("""
```

Pendapatan jangka pendek meningkat.

Risiko banjir dan erosi bertambah.

Keanekaragaman hayati menurun.

Nilai jasa lingkungan berkurang.
""")

# =========================

# VISUALISASI TEV

# =========================

elif menu == "Visualisasi TEV":

```
st.title("Visualisasi Total Economic Value (TEV)")

data_tev = pd.DataFrame({
    "Komponen": [
        "Wisata",
        "Hasil Hutan",
        "Air",
        "Karbon",
        "Nilai Pilihan",
        "Nilai Eksistensi"
    ],
    "Nilai": [
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
    y="Nilai",
    title="Komponen TEV Tahura (Miliar Rupiah)"
)

st.plotly_chart(fig1, use_container_width=True)

fig2 = px.pie(
    data_tev,
    names="Komponen",
    values="Nilai",
    title="Proporsi Komponen TEV"
)

st.plotly_chart(fig2, use_container_width=True)

st.dataframe(data_tev)
```
