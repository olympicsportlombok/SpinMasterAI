import streamlit as st
from google import genai

## 1. KONFIGURASI DAN INISIALISASI KLIEN GEMINI
# KODE INI BERJALAN SAAT APLIKASI DIMUAT

try:
    # Mengambil kunci API dari Streamlit Secrets
    # Pastikan di Streamlit Cloud Secrets, Anda memasukkan: API_KEY="KUNCI_ANDA"
    api_key = st.secrets["API_KEY"] 
    client = genai.Client(api_key=api_key)
except KeyError:
    # Tampilkan error jika kunci API tidak ditemukan (PENTING untuk troubleshooting)
    st.error("🚨 Kunci API tidak ditemukan! Silakan cek kembali 'API_KEY' di Streamlit Secrets.")
    st.stop()
except Exception as e:
    # Tangani error koneksi atau inisialisasi lainnya
    st.error(f"❌ Gagal menginisialisasi klien Gemini: {e}")
    st.stop()


## 2. LOGIKA KUSTOM (SYSTEM PROMPT)
# Ini adalah instruksi yang memberikan 'persona' kepada AI Anda
SYSTEM_PROMPT = (
    "Anda adalah SpinMaster AI, asisten analisis data dan konsultan olahraga khusus untuk Olympic Sport Lombok. "
    "Berikan respons yang informatif, fokus pada analisis data, teknik, dan berita terkait olahraga, terutama tenis meja dan cabang olahraga Olimpiade lainnya. "
    "Jawablah dengan nada profesional dan bersemangat."
)

# Nama Model yang akan digunakan
MODEL_NAME = "gemini-2.0-flash" 


## 3. DESAIN ANTARMUKA STREAMLIT

st.set_page_config(page_title="SpinMaster AI", page_icon="🏓")
st.title("🏓 SpinMaster AI by Olympic Sport Lombok")
st.markdown("---")

st.markdown(
    "**SpinMaster AI** siap membantu Anda menganalisis data, strategi, dan teknik dalam dunia olahraga."
)

input_user = st.text_area(
    "Masukkan Pertanyaan Analisis / Data Anda:", 
    placeholder="Contoh: Bagaimana cara meningkatkan kecepatan pukulan topspin saya?",
    height=100
)

## 4. LOGIKA PEMANGGILAN API (Dipicu oleh Tombol)

if st.button("Kirim Analisis", type="primary"):
    if not input_user:
        st.warning("Mohon masukkan pertanyaan atau data terlebih dahulu.")
    else:
        try:
            with st.spinner("⏳ SpinMaster AI sedang menganalisis data..."):
                # Panggil API dengan menyertakan System Prompt dalam config
                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=input_user,
                    config={"system_instruction": SYSTEM_PROMPT} # <--- LOGIKA KUSTOM ANDA DI SINI
                )
            
            st.markdown("## 💡 Hasil Analisis:")
            # Gunakan st.markdown untuk tampilan yang lebih baik
            st.markdown(response.text)

        except Exception as e:
            # Tampilkan pesan jika API call gagal setelah tombol diklik
            st.error(f"❌ Terjadi kesalahan pada pemanggilan model: {e}")
            st.write("Coba periksa lagi koneksi atau validitas kunci API Anda.")

st.markdown("---")
st.caption("Aplikasi ini menggunakan Model Gemini oleh Google.")