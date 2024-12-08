import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul Dashboard
st.title("Dashboard Kelompok Dea Febianty Utama-240534001 Slamet Riyadi-240534002 Refdi Rahmandha-240534005")

# Sidebar
st.sidebar.header("Pengaturan")
option = st.sidebar.selectbox("Pilih Data:", ["Data 1", "Data 2"])

# Dummy Data
if option == "Data 1":
    data = pd.DataFrame({
        "Bulan": ["Januari", "Februari", "Maret", "April"],
        "Penjualan": [100, 120, 90, 150]
    })
else:
    data = pd.DataFrame({
        "Bulan": ["Mei", "Juni", "Juli", "Agustus"],
        "Penjualan": [80, 110, 130, 170]
    })

# Menampilkan Data
st.subheader("Data Penjualan")
st.dataframe(data)

# Visualisasi Data
fig, ax = plt.subplots()
ax.bar(data["Bulan"], data["Penjualan"], color="skyblue")
ax.set_title("Grafik Penjualan")
ax.set_xlabel("Bulan")
ax.set_ylabel("Penjualan")
st.pyplot(fig)
