import streamlit as st
from google import genai

# ==============================================================================
# 1. LOGIKA KUSTOM ANDA DARI GOOGLE AI STUDIO
# ==============================================================================

# INI ADALAH INSTRUKSI SISTEM LENGKAP YANG DIRANGKUM DARI PROMPT ANDA.
SYSTEM_PROMPT_ANDA = (
    "Kamu adalah AI rekomendasi bet pingpong profesional bernama SpinMaster AI by Olympic Sport Lombok. "
    "Tugasmu adalah menganalisis gaya bermain pengguna dan mencocokkannya dengan blade yang tersedia dalam database yang sudah disediakan. "
    "Kamu harus selalu menghindari merekomendasikan merek Andro, Yinhe, Tibhar, dan Yasaka, dan hanya merekomendasikan blade yang ada dalam stok toko. "
    "Jangan pernah menampilkan atau menebak harga. Jika user menanyakan harga, jawab dengan sopan: 'Untuk harga bisa langsung hubungi pemilik toko ya kak 😊'. "
    "CARA KERJA AI (HARUS DIIKUTI): Tanyakan dulu profil user, meliputi: Gaya bermain (Offensive / All-round / Defensive), Teknik dominan (Topspin, Block, Drive, Counter, Chop), Dominasi tangan (Forehand / Backhand), Kecepatan swing (Cepat / Sedang / Lambat), Level pemain (Pemula / Menengah / Jago), Preferensi feel blade (Keras / Medium / Soft), dan Berapa lama sudah main tenis meja? (untuk mengarahkan ke kelas pemula jika baru mulai). "
    "Berikan output dengan format berikut: Ringkasan analisis gaya bermain user, Blade yang direkomendasikan + alasan teknis lengkap, 2–3 alternatif blade lain yang cocok, Saran pairing tipe rubber (tanpa harga), Tips tambahan sesuai gaya bermain. "
    "Gunakan bahasa yang profesional namun mudah dimengerti. Jika user menanyakan model lain di luar database, jelaskan bahwa rekomendasi utama hanya berdasarkan database yang tersedia. "
    "Saat memberikan ulasan atau skor performa (misalnya Power, Spin, Control), selalu gunakan format nilai/5 (contoh: 4/5). "
    "LARANGAN KERAS: Tidak boleh menampilkan harga, Tidak boleh membuat data di luar database kecuali info umum, Tidak boleh membuat tabel harga atau estimasi harga."
)

# NAMA MODEL DIUBAH SESUAI PERMINTAAN ANDA
MODEL_NAME = "gemini-2.0-flash" 

# Pengaturan tambahan untuk konsistensi
MODEL_TEMPERATURE = 0.2 
MODEL_TOP_P = 0.8

# Kamus konfigurasi final untuk API
model_config = {
    "system_instruction": SYSTEM_PROMPT_ANDA,
    "temperature": MODEL_TEMPERATURE,
    "top_p": MODEL_TOP_P,
}


# ==============================================================================
# 2. KONEKSI DAN ANTARMUKA STREAMLIT
# ==============================================================================

# KONEKSI API (Mengambil kunci dari Streamlit Secrets)
try:
    api_key = st.secrets["API_KEY"]
    client = genai.Client(api_key=api_key)
except KeyError:
    st.error("🚨 Kunci API 'API_KEY' tidak ditemukan di Streamlit Secrets.")
    st.stop()
except Exception as e:
    st.error("❌ Gagal koneksi ke Gemini.")
    st.stop()


# DESAIN ANTARMUKA STREAMLIT
st.set_page_config(page_title="SpinMaster AI", page_icon="🏓")
st.title("🏓 SpinMaster AI")
st.subheader("by Olympic Sport Lombok") 
st.markdown("---")

st.info("Saya adalah AI Rekomendasi Bet Pingpong Profesional. Masukkan profil bermain Anda untuk mendapatkan analisis blade terbaik.")

input_user = st.text_area(
    "Masukkan Profil Bermain Anda:", 
    placeholder="Contoh: Gaya bermain saya Offensive, dominan Topspin FH, swing cepat, level menengah. Saya sudah bermain 3 tahun dan suka feel medium.",
    height=150
)

# ==============================================================================
# 3. LOGIKA PEMANGGILAN MODEL
# ==============================================================================

if st.button("Dapatkan Rekomendasi Blade", type="primary"):
    if not input_user:
        st.warning("Mohon masukkan profil bermain Anda terlebih dahulu.")
    else:
        try:
            with st.spinner("⏳ SpinMaster AI sedang menganalisis gaya bermain dan mencocokkan database..."):
                # PEMANGGILAN GEMINI DENGAN SEMUA LOGIKA KUSTOM
                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=input_user,
                    config=model_config 
                )
            
            st.markdown("## ✅ Hasil Analisis Blade:")
            st.markdown(response.text)
            
            # Tombol Kontak Instagram
            st.markdown("---")
            instagram_url = "https://www.instagram.com/olympicsportlombok"
            st.markdown(
                f'<a href="{instagram_url}" target="_blank">'
                f'<button style="background-color: #C13584; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: