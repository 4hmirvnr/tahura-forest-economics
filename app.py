import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================

# KONFIGURASI HALAMAN

# =====================================

st.set_page_config(
page_title="Tahura Ir. H. Djuanda",
page_icon="🌳",
layout="wide"
)

# =====================================

# SIDEBAR

# =====================================

menu = st.sidebar.selectbox(
"Pilih Menu",
[
"Beranda",
"Profil Tahura",
"Kalkulator TEV",
"Trade-off Lahan",
"Kebijakan PES",
"Kasus Interaktif",
"Visualisasi TEV"
]
)

# =====================================

# BERANDA

# =====================================

if menu == "Beranda":

```
st.title("🌳 PBL 6 – Ekonomi Sumber Daya Alam dan Lingkungan")

st.subheader("Identitas Kelompok 3")

st.write("• Ahmad Irvan Nur Varizki (10090224011)")
st.write("• Freya Helga Pebrian (10090224017)")
st.write("• Muhammad Yaasin As-Suhaimi (10090224028)")

st.markdown("---")

st.write("**Dosen Pengampu:**")
st.write("Yuhka Sundaya, S.E., M.Si")

st.markdown("---")

st.success(
    "Dashboard analisis ekonomi lingkungan "
    "Taman Hutan Raya Ir. H. Djuanda."
)
```

# =====================================

# PROFIL TAHURA

# =====================================

elif menu == "Profil Tahura":

```
st.title("Profil Taman Hutan Raya Ir. H. Djuanda")

st.write("""
```

Taman Hutan Raya (Tahura) Ir. H. Djuanda merupakan kawasan
pelestarian alam pertama di Indonesia yang diresmikan
pada 14 Januari 1985.

Lokasi:
Ciburial, Kecamatan Cimenyan, Kabupaten Bandung, Jawa Barat.

Luas kawasan sekitar 590 hektare dengan ketinggian
770–1.330 mdpl.
""")

```
st.subheader("Flora")

st.write("""
```

• Pinus (Pinus merkusii)

• Bambu

• Kaliandra

• Berbagai tanaman konservasi
""")

```
st.subheader("Fauna")

st.write("""
```

• Monyet ekor panjang

• Tupai

• Musang

• Burung ketilang

• Kepodang

• Ayam hutan
""")

# =====================================

# KALKULATOR TEV

# =====================================

elif menu == "Kalkulator TEV":

```
st.title("Kalkulator Total Economic Value (TEV)")

wisata = st.number_input(
    "Nilai Wisata (Rp)",
    value=4000000000
)

hasil_hutan = st.number_input(
    "Nilai Hasil Hutan (Rp)",
    value=1000000000
)

air = st.number_input(
    "Nilai Penyediaan Air (Rp)",
    value=7000000000
)

karbon = st.number_input(
    "Nilai Penyimpanan Karbon (Rp)",
    value=5000000000
)

pilihan = st.number_input(
    "Nilai Pilihan (Rp)",
    value=2000000000
)

eksistensi = st.number_input(
    "Nilai Eksistensi (Rp)",
    value=3000000000
)

tev = (
    wisata
    + hasil_hutan
    + air
    + karbon
    + pilihan
    + eksistensi
)

st.metric(
    "Total Economic Value",
    f"Rp {tev:,.0f}"
)
```

# =====================================

# TRADE OFF LAHAN

# =====================================

elif menu == "Trade-off Lahan":

```
st.title("Trade-off Lahan")

df = pd.DataFrame({
    "Alternatif": [
        "Hutan Lestari",
        "Konversi Lahan Penduduk"
    ],
    "Nilai": [
        22,
        12
    ]
})

st.dataframe(df)

fig = px.bar(
    df,
    x="Alternatif",
    y="Nilai",
    title="Perbandingan Nilai Ekonomi"
)

st.plotly_chart(fig, use_container_width=True)
```

# =====================================

# KEBIJAKAN PES

# =====================================

elif menu == "Kebijakan PES":

```
st.title("Payment for Ecosystem Services (PES)")

st.write("""
```

Pemanfaat jasa lingkungan Tahura:

• BPAB-DC

• PDAM Tirtawening

• PLTA Dago Bengkok

• Wisatawan
""")

```
jumlah = st.slider(
    "Jumlah Pembayar PES",
    1,
    10,
    4
)

iuran = st.number_input(
    "Iuran per Institusi (Rp)",
    value=500000000
)

total = jumlah * iuran

st.metric(
    "Potensi Dana PES",
    f"Rp {total:,.0f}"
)
```

# =====================================

# KASUS INTERAKTIF

# =====================================

elif menu == "Kasus Interaktif":

```
st.title("Kasus Interaktif")

pilihan = st.radio(
    "Jika 100 hektare dibuka untuk pembangunan:",
    [
        "Tetap Konservasi",
        "Konversi Sebagian"
    ]
)

if pilihan == "Tetap Konservasi":

    st.success(
        "Keanekaragaman hayati dan fungsi ekologis tetap terjaga."
    )

else:

    st.error(
        "Pendapatan meningkat namun jasa lingkungan menurun."
    )
```

# =====================================

# VISUALISASI TEV

# =====================================

elif menu == "Visualisasi TEV":

```
st.title("Visualisasi TEV")

data = pd.DataFrame({
    "Komponen": [
        "Wisata",
        "Hasil Hutan",
        "Air",
        "Karbon",
        "Pilihan",
        "Eksistensi"
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
    data,
    x="Komponen",
    y="Nilai",
    title="Komponen TEV"
)

st.plotly_chart(fig1, use_container_width=True)

fig2 = px.pie(
    data,
    names="Komponen",
    values="Nilai",
    title="Proporsi TEV"
)

st.plotly_chart(fig2, use_container_width=True)
```
