import streamlit as st

st.title("🎈 aplikasi kelas c")
import streamlit as st
import streamlit as st

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)


st.title("🧮 Kalkulator Sederhana")

# Input angka
angka1 = st.number_input("Masukkan angka pertama", value=0.0)
angka2 = st.number_input("Masukkan angka kedua", value=0.0)

# Pilihan operasi
operasi = st.selectbox(
    "Pilih operasi",
    ["Penjumlahan (+)", "Pengurangan (-)", "Perkalian (×)", "Pembagian (÷)"]
)

# Tombol hitung
if st.button("Hitung"):
    if operasi == "Penjumlahan (+)":
        hasil = angka1 + angka2
    elif operasi == "Pengurangan (-)":
        hasil = angka1 - angka2
    elif operasi == "Perkalian (×)":
        hasil = angka1 * angka2
    elif operasi == "Pembagian (÷)":
        if angka2 != 0:
            hasil = angka1 / angka2
        else:
            hasil = "Tidak bisa dibagi 0"

    st.success(f"Hasil: {hasil}")
