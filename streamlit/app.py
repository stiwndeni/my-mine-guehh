import streamlit as st
import time

# --- PENGATURAN HALAMAN ---
st.set_page_config(page_title="Pesan Khusus Untukmu ❤️", page_icon="💖", layout="centered")

# --- CSS CUSTOM UNTUK TAMPILAN CANTIK ---
st.markdown("""
    <style>
    .main {
        background-color: #FFF5F5;
    }
    h1 {
        color: #D32F2F;
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .stButton>button {
        background-color: #FF4081;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 24px;
        font-size: 18px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #F50057;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("Hai Sayang! ❤️")
st.write("### sebuah tanda yang menunjukan bahwa sesayang itu aku sama dia...")

st.write("---")

# --- BAGIAN 1: GALERI FOTO / MEMORI ---
st.subheader("📸 ur my romantic gurl")
st.write("Setiap detik bersamamu selalu jadi favoritku.")

# Tips: Ganti URL gambar di bawah dengan foto kalian berdua
col1, col2 = st.columns(2)
with col1:
    st.image("https://drive.google.com/file/d/1dDFULv6PbVm2BEhpHkjhdQNohuoPIvNV/view?usp=sharing", caption="UR EYES 🥰")
with col2:
    st.image("https://images.unsplash.com/photo-1522673607200-164d1b6ce486?w=500", caption="Selalu bahagia bareng kamu 💕")

st.write("---")

# --- BAGIAN 2: FITUR INTERAKTIF (PESAN RAHASIA) ---
st.subheader("💌 Ada Surat Rahasia Untukmu")

if st.button("Buka Surat Rahasia 🔓"):
    with st.spinner('Membuka pesan cinta...'):
        time.sleep(1.5)
    
    st.balloons() # Efek balon terbang!
    st.success("Surat Berhasil Dibuka!")
    
    st.markdown("""
    > *"Terima kasih ya sudah hadir dan selalu bikin hari-hariku jauh lebih berwarna. 
    > Kamu itu alasan aku tersenyum setiap hari. Tetap sama-sama terus ya!"* 
    > 
    > **I Love You So Much! 💖**
    """)

st.write("---")

# --- BAGIAN 3: KUIS / PERTANYAAN MANIS ---
st.subheader("❓ Kuis Singkat")
jawaban = st.radio(
    "Seberapa sayang kamu sama aku hari ini?",
    ["Sayang banget!", "Sayang banget banget!!", "Nggak bisa diukur pake kata-kata! 🥰"]
)

if jawaban:
    st.write(f"Jawaban kamu: **{jawaban}**")
    st.write("Sama! Aku juga jauh lebih sayang sama kamu! 😘")

# --- FOOTER ---
st.write("---")
st.caption("Dibuat dengan ❤️ dan kode Python khusus untukmu.")
