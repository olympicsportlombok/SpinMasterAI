import streamlit as st
from google import genai

# ==============================================================================
# 1. DATABASE DAN LOGIKA KUSTOM ANDA DARI GOOGLE AI STUDIO
# ==============================================================================

# DATABASE BLADE DARI FILE 'Blade Comparison.pdf' - DIGUNAKAN OLEH AI
BLADE_DATABASE = """
Nama Bet | Power | Speed | Spin | Kontrol | Karakter Singkat | Level Pemain
--- | --- | --- | --- | --- | --- | ---
Butterfly Sardius | 5 | 5 | 2 | 3 | Sangat kencang, kaku, tembakan lurus, sulit dikontrol. | Jago
Butterfly Zhang Jike ALC | 4 | 4 | 4 | 3 | Kencang, stabil, "touch" baik, serba bisa untuk serang. | Menengah/Jago
DHS Hurricane Long 5 | 5 | 4 | 5 | 3 | "Dual-speed" (pelan jika pelan, kencang jika keras), fleksibel, power loop | Jago
Donic New Impuls 7.5 | 3 | 4 | 3 | 3 | 7-ply all-wood, cepat tapi "empuk", kontrol baik. | Menengah
Donic Skachkov Carbon | 5 | 5 | 3 | 2 | Sangat kencang (Outer Carbon), kaku, ofensif murni. | Jago
Donic Waldner Blackdevil | 4 | 4 | 3 | 3 | Kencang dan ringan (inti balsa), "empuk" tapi cepat. | Menengah
Donic Waldner Legend | 3 | 3 | 4 | 4 | Klasik 5-ply (all-wood), serang, "feel" bagus. | Menengah
Doublefish Athlon 1 | 3 | 3 | 3 | 3 | Ofensif (estimasi), kaku (estimasi). | Menengah
Doublefish Dragon Blade 1 | 2 | 2 | 3 | 4 | All-round (estimasi), kontrol (estimasi). | Pemula/Menengah
Doublefish Dragon Blade 2 | 3 | 3 | 3 | 4 | All-round+ (estimasi), sedikit lebih cepat dari 1. | Menengah
Doublefish King Power | 4 | 4 | 3 | 2 | Kencang, power (estimasi, 5+2 Carbon). | Menengah
Doublefish King Speed | 5 | 5 | 2 | 2 | Sangat kencang (estimasi). | Menengah/Jago
Joola Classic Carbon | 4 | 4 | 3 | 3 | Ofensif, kaku, "sweet spot" besar. | Menengah
Joola Santoru KLC Inner | 4 | 4 | 5 | 3 | Fleksibel, spin tinggi, "inner carbon" untuk loop. | Menengah/Jago
Joola Tezzo Guardian | 2 | 2 | 3 | 5 | Defensif/All-round, kontrol tinggi. | Pemula/Menengah
Joola Tezzo Spartan | 3 | 3 | 4 | 4 | Ofensif (all-wood), "feel" baik, kontrol bagus. | Menengah
Joola Zelebro PBO-C | 5 | 5 | 3 | 2 | Sangat cepat, kaku, "outer layer" PBO-C, power murni. | Jago
Joola Zhou Ji Hao Hyper Ary 90 | 5 | 5 | 3 | 1 | Sangat kencang, tebal (9mm Hinoki), "catapult" tinggi. | Jago
Kokutaku Graphene Carbon | 4 | 4 | 3 | 3 | Kaku, kencang (estimasi Graphene). | Menengah/Jago
Kokutaku Graphene ZC Grid | 5 | 5 | 3 | 2 | Sangat kaku, power murni (estimasi). | Jago
Nittaku DHS H30 NXD | 4 | 4 | 5 | 3 | Inner composite (NXD), spin, power, "feel" khas. | Jago
Nittaku Ease Carbon | 3 | 3 | 3 | 4 | All-round serang, ringan, mudah dikontrol. | Pemula/Menengah
Nittaku Flyatt Carbon | 4 | 4 | 3 | 3 | Cepat tapi ringan, kontrol baik untuk karbon. | Menengah
Nittaku Gyo En | 4 | 4 | 4 | 3 | 5-ply all-wood, serang, "feel" solid. | Menengah
Nittaku So Ten | 4 | 4 | 3 | 3 | 7-ply kayu murni, kencang, power-wood. | Menengah/Jago
Nittaku Tribus Carbon | 4 | 4 | 4 | 4 | Inner carbon (KVL), seimbang, "dwell time" baik. | Menengah/Jago
Sanwei 1091 | 2 | 2 | 3 | 4 | All-round, kontrol (estimasi). | Pemula
Sanwei C&C | 4 | 4 | 4 | 3 | Hinoki-Carbon, kencang, "touch" empuk. | Menengah/Jago
Sanwei Future Carbon | 3 | 4 | 3 | 3 | Ofensif karbon, harga terjangkau. | Menengah
Sanwei J | 2 | 2 | 3 | 4 | All-round (estimasi), sangat dasar. | Pemula
Sanwei T5000 | 5 | 5 | 2 | 2 | Kaku, sangat kencang, mirip Butterfly T5000. | Jago
Stiga Carbonado 145 | 5 | 5 | 4 | 2 | Sangat kencang, kaku, trayektori bola tinggi, ofensif. | Jago
Stiga Carbonado 45 | 4 | 4 | 5 | 3 | Kencang tapi fleksibel (45° carbon), spin tinggi. | Menengah/Jago
Stiga Clipper CR | 4 | 4 | 4 | 3 | Ofensif klasik (7-ply all-wood), stabil, "rasa" kayu murni. | Menengah/Jago
Stiga Dynasty Carbon | 5 | 5 | 4 | 2 | Sangat kencang (kayu Xu Xin), "touch" lebih lembut dari Carbonado. | Jago
Stiga Ebenholz NCT V | 4 | 4 | 4 | 3 | 5-ply kayu eksotis, kencang, "feel" jernih. | Jago
Stiga Legacy Carbon | 5 | 5 | 3 | 2 | Sangat kencang, kaku, power serang. | Jago
Tmount Hyper Carbon F720 | 4 | 4 | 3 | 3 | Ofensif (estimasi, 7-ply+carbon). | Menengah/Jago
Tmount Hyper Carbon T560 | 4 | 4 | 3 | 3 | Ofensif (estimasi, 5-ply+carbon). | Menengah
Tmount KTS 740 | 3 | 3 | 3 | 4 | All-round+ (estimasi). | Menengah
Tmount KTS 760 | 4 | 4 | 3 | 3 | Ofensif (estimasi). | Menengah
Tmount KTS 920 | 4 | 5 | 3 | 2 | Ofensif+ (estimasi). | Menengah/Jago
Tmount KTS Fury LC | 4 | 4 | 4 | 3 | Inner Carbon (estimasi Limba Carbon), spin, kontrol. | Menengah/Jago
TSP Swat Power | 4 | 4 | 3 | 3 | 7-ply kayu, power serang, "feel" solid. | Menengah/Jago
Victas Firefall AC | 4 | 4 | 4 | 3 | Outer AC (Arylate Carbon), kencang, stabil. | Menengah/Jago
Victas Firefall HC | 5 | 5 | 3 | 2 | Hinoki-Carbon, sangat kencang, "catapult" tinggi. | Jago
Victas Firefall SC | 4 | 4 | 3 | 3 | Kencang, kaku (Silver Carbon), power. | Menengah/Jago
Victas Koji Matsushita | 2 | 4 | 5 | 5 | Defensif murni, kepala bet besar, sangat lambat, kontrol maksimal. | Menengah/Jago (Tipe Defensif)
Victas Koki Niwa All Wood | 4 | 4 | 4 | 3 | 7-ply kayu, ofensif cepat, "feel" murni. | Menengah/Jago
Victas Koki Niwa DSE | 4 | 4 | 5 | 3 | Inner carbon, seimbang, power dan spin. | Jago
Victas Quartet Carbon | 5 | 5 | 3 | 2 | Sangat kaku, sangat kencang, power murni. | Jago
XIOM 36.5 ALX | 4 | 4 | 4 | 3 | Kencang, fleksibel (outer ALC), all-round serang modern. | Menengah/Jago
XIOM 36.5 ALXI | 4 | 4 | 5 | 4 | Inner ALC, fleksibel, spin tinggi, kontrol. | Menengah/Jago
XIOM Axelo | 5 | 5 | 3 | 2 | Hinoki-Carbon, tebal, sangat kencang, "catapult". | Jago
XIOM AZX ICE CREAM | 5 | 5 | 4 | 3 | Dua sisi beda (ALC/ZLC), kencang, inovatif. | Jago
XIOM Cho Dae Song | 4 | 5 | 4 | 3 | Outer ALC, kencang, stabil, serang modern. | Menengah/Jago
XIOM Hayabusa ARX | 4 | 4 | 4 | 4 | Aramid-Carbon, "feel" empuk, kencang tapi terkontrol. | Menengah/Jago
XIOM Hayabusa ZL Pro | 5 | 5 | 3 | 2 | Zylon (ZL), sangat kencang, "sweet spot" besar. | Jago
XIOM Hayabusa ZLX | 5 | 5 | 3 | 2 | Zylon-Carbon, kencang, kaku (estimasi). | Jago
XIOM Strato | 4 | 4 | 4 | 3 | Outer ALC, kencang, "feel" klasik, serba bisa serang. | Menengah/Jago
"""

# SYSTEM INSTRUCTION LENGKAP DENGAN PENYEBUTAN DATABASE
SYSTEM_PROMPT_ANDA = (
    f"Kamu adalah AI rekomendasi bet pingpong profesional bernama SpinMaster AI by Olympic Sport Lombok. "
    f"Tugasmu adalah menganalisis gaya bermain pengguna dan mencocokkannya dengan blade yang tersedia dalam DATABASE berikut: \n\n--- DATABASE STOK TOKO ---\n{BLADE_DATABASE}\n\n--- AKHIR DATABASE ---\n\n"
    f"Kamu harus selalu menghindari merekomendasikan merek Andro, Yinhe, Tibhar, dan Yasaka, dan hanya merekomendasikan blade yang ada dalam stok toko (yaitu yang ada di DATABASE di atas). "
    f"Jangan pernah menampilkan atau menebak harga. Jika user menanyakan harga, jawab dengan sopan: 'Untuk harga bisa langsung hubungi pemilik toko ya kak 😊'. "
    f"CARA KERJA AI (HARUS DIIKUTI): Tanyakan dulu profil user, meliputi: Gaya bermain (Offensive / All-round / Defensive), Teknik dominan (Topspin, Block, Drive, Counter, Chop), Dominasi tangan (Forehand / Backhand), Kecepatan swing (Cepat / Sedang / Lambat), Level pemain (Pemula / Menengah / Jago), Preferensi feel blade (Keras / Medium / Soft), dan Berapa lama sudah main tenis meja? (untuk mengarahkan ke kelas pemula jika baru mulai). "
    f"Berikan output dengan format berikut: Ringkasan analisis gaya bermain user, Blade yang direkomendasikan + alasan teknis lengkap, 2–3 alternatif blade lain yang cocok, Saran pairing tipe rubber (tanpa harga), Tips tambahan sesuai gaya bermain. "
    f"Gunakan bahasa yang profesional namun mudah dimengerti. Jika user menanyakan model lain di luar database, jelaskan bahwa rekomendasi utama hanya berdasarkan database yang tersedia. "
    f"Saat memberikan ulasan atau skor performa (misalnya Power, Spin, Control), selalu gunakan format nilai/5 (contoh: 4/5). "
    f"LARANGAN KERAS: Tidak boleh menampilkan harga, Tidak boleh membuat data di luar database kecuali info umum, Tidak boleh membuat tabel harga atau estimasi harga."
)

# NAMA MODEL: GEMINI 2.0 FLASH
MODEL_NAME = "gemini-2.0-flash" 
MODEL_TEMPERATURE = 0.2 
MODEL_TOP_P = 0.8

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
except Exception:
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
            
            # Tombol Kontak Instagram (Sudah diperbaiki)
            st.markdown("---")
            instagram_url = "https://www.instagram.com/olympicsportlombok"
            st.markdown(
                f"""
                <a href="{instagram_url}" target="_blank">
                <button style="background-color: #C13584; 
                               color: white; 
                               border: none; 
                               padding: 10px 20px; 
                               text-align: center; 
                               text-decoration: none; 
                               display: inline-block; 
                               font-size: 16px; 
                               margin: 4px 2px; 
                               cursor: pointer; 
                               border-radius: 8px;">
                    DM Instagram @olympicsportlombok untuk Harga & Stok
                </button></a>
                """, 
                unsafe_allow_html=True
            )

        except Exception as e:
            st.error(f"❌ Terjadi kesalahan pada pemanggilan API: {e}")
            st.write("Cek kembali kunci API atau batas penggunaan.")

st.markdown("---")
st.caption("2025 Olympic Sport Lombok. Aplikasi ini didukung oleh Google Gemini.")