import streamlit as st
from google import genai
import time

## 1. KONFIGURASI DAN KONEKSI API
# Streamlit akan mengambil kunci dari Secrets bernama "API_KEY"

try:
    api_key = st.secrets["API_KEY"]
    client = genai.Client(api_key=api_key)
except KeyError:
    st.error("🚨 Kunci API 'API_KEY' tidak ditemukan di Streamlit Secrets.")
    st.stop()
except Exception as e:
    st.error(f"❌ Gagal koneksi ke Gemini: {e}")
    st.stop()


## 2. LOGIKA KUSTOM ANDA DARI GOOGLE AI STUDIO
# GANTI TEKS DI BAWAH INI DENGAN SYSTEM PROMPT ANDA YANG SEBENARNYA!
SYSTEM_PROMPT_ANDA = (
    📌 SYSTEM INSTRUCTION — TABLE TENNIS BLADE ANALYZER
Kamu adalah AI rekomendasi bet pingpong profesional.
Tugasmu adalah menganalisis gaya bermain pengguna dan mencocokkannya dengan blade yang tersedia dalam database berikut.
Jangan pernah menampilkan atau menebak harga.
Jika user menanyakan harga, jawab dengan sopan:
“Untuk harga bisa langsung hubungi pemilik toko ya kak 😊”
📌 CARA KERJA AI (HARUS DIIKUTI)
Tanyakan dulu profil user, meliputi:
Gaya bermain (Offensive / All-round / Defensive)
Teknik dominan (Topspin, Block, Drive, Counter, Chop)
Dominasi tangan (Forehand / Backhand)
Kecepatan swing (Cepat / Sedang / Lambat)
Level pemain (Pemula / Menengah / Jago)
Preferensi feel blade (Keras / Medium / Soft)
Analisis profil user → cocokkan dengan database blade.
Berikan output dengan format berikut:
Ringkasan analisis gaya bermain user
Blade yang direkomendasikan + alasan teknis lengkap
2–3 alternatif blade lain yang cocok
Saran pairing tipe rubber (tanpa harga)
Tips tambahan sesuai gaya bermain
Gunakan bahasa yang profesional namun mudah dimengerti.
Jika user menanyakan model lain di luar database, jelaskan bahwa rekomendasi utama hanya berdasarkan database yang tersedia.
Larangan keras
Tidak boleh menampilkan harga.
Tidak boleh membuat data di luar database kecuali info umum (contoh: ciri blade OFF).
Tidak boleh membuat tabel harga atau estimasi harga.
📌 CONTOH OUTPUT
Profil user:
Offensive loop
FH dominan
Swing cepat
Level menengah
Rekomendasi utama:
Butterfly Zhang Jike ALC
Reasoning: Balance antara speed–spin–kontrol, cocok untuk topspin cepat dan counter-loop.
Stabil untuk user menengah yang ingin meningkatkan agresivitas permainan.
Alternatif:
DHS Hurricane Long 5 → untuk loop FH kuat
Donic Skachkov Carbon → untuk speed maksimal (kontrol lebih rendah)
Catatan harga:
Untuk harga bisa langsung hubungi pemilik toko ya kak 😊
Gemini 3 Pro Preview
Ran for 28s
lightbulb
Thought for 28 seconds
metadata.json
check_circle
index.html
check_circle
index.tsx
check_circle
types.ts
check_circle
constants.ts
check_circle
services/geminiService.ts
check_circle
components/Button.tsx
check_circle
components/Wizard.tsx
check_circle
components/Results.tsx
check_circle
App.tsx
check_circle
User
Saya AI rekomendasi bet pingpong profesional. Untuk memberikan rekomendasi terbaik, mohon berikan informasi mengenai gaya bermain Anda (Offensive / All-round / Defensive), teknik dominan (Topspin, Block, Drive, Counter, Chop), dominasi tangan (Forehand / Backhand), kecepatan swing (Cepat / Sedang / Lambat), level pemain (Pemula / Menengah / Jago), dan preferensi feel blade (Keras / Medium / Soft).
Gemini 3 Pro Preview
Ran for 101s
lightbulb
Thought for 93 seconds
services/geminiService.ts
check_circle
components/Results.tsx
check_circle
User
tambahkan input untuk analisa user, berapa lama anda sudah main tenis meja? kaitannya jika dirasa baru mulai diarahkan untuk bet pingpong yang kelasnya untuk pemula. untuk catatan jangan rekomendasi bet pingpong merk andro, yinhe, tibhar, yasaka
Gemini 3 Pro Preview
Ran for 92s
lightbulb
Thought for 86 seconds
types.ts
check_circle
constants.ts
check_circle
services/geminiService.ts
check_circle
App.tsx
check_circle
User
nama aplikasi spinmaster AI sudah bagus, namun agar tidak ada pihak yg tidak bertanggung jawab mengklaim app ini bisa tolong ditambahkan subheading di atas atau bawahnya nama aplikasi tersebut tulisan "by Olympic Sport Lombok" . di bawah tulisan yang ada 2025 SpinMaster AI juga diganti dengan 2025 Olympic Sport Lombok (tulisan selanjutnya mengikuti)
Gemini 3 Pro Preview
Ran for 77s
lightbulb
Thought for 62 seconds
App.tsx
check_circle
User
di akhir sesi bisa tambahkan tombol untuk kontak via dm instagram @olympicsportlombok . Jadi user tersebut ketika mengklik tombol tersebut langsung diarahkan ke akun instagram @olympicsportlombok agar bisa komunikasi lebih lanjut tentang rekomendasi bet pingpong dan peralatan tenis meja lainnya
Gemini 3 Pro Preview
Ran for 94s
lightbulb
Thought for 68 seconds
To satisfy your request, I will update the Results component to include a prominent Instagram button at the end of the analysis. This will allow users to easily contact @olympicsportlombok for further consultation, pricing, and stock inquiries.
components/Results.tsx
check_circle
User
apakah bisa untuk gambar blade rekomendasi diganti dengan gambar blade yang sebenarnya? jika tidak bisa lebih baik dihilangkan
Gemini 3 Pro Preview
Ran for 53s
lightbulb
Thought for 31 seconds
To ensure the application remains professional and avoids displaying incorrect or broken images, I will follow your request to remove the image section entirely since we don't have a reliable database of specific blade images.
Here are the changes to remove the image placeholder from the result display.
components/Results.tsx
check_circle
User
untuk rekomendasi agar lebih terarah ke blade yang saat ini ready stock di toko kami bisakah diarahkan atau dikerucutkan ke database bet pingpong berikut ini saja? untuk menghindari rekomendasi produk yang tidak kami jual
Blade Comparison.pdf
Gemini 3 Pro Preview
Ran for 129s
lightbulb
Thought for 107 seconds
To ensure the recommendations are strictly limited to the blades currently in stock at "Olympic Sport Lombok", I will replace the generic blade database with the specific list provided in your document. I will also configure the AI to strictly adhere to this list and ignore any outside models.
Updated files:
constants.ts
Replaced the generic BLADE_DATABASE with the specific stock list extracted from your document (Butterfly, Donic, Doublefish, Joola, Kokutaku, Nittaku, Sanwei, Stiga, Tmount, TSP, Victas, Xiom).
services/geminiService.ts
Updated the system instruction to force the AI to select recommendations ONLY from the new BLADE_DATABASE.
constants.ts
check_circle
services/geminiService.ts
check_circle
User
bisa ubah sedikit ketika memberikan skor pada ulasan misal "dengan spin 4" bisa ditambahkan 4/5 jadi supaya user tahu nilainya 4 dari 5 bukan salah sangka 4 dari 10 dsb
Gemini 3 Pro Preview
Ran for 63s
lightbulb
Thought for 43 seconds
To ensure the scoring is clear (e.g., "4/5" instead of just "4"), I will update the database strings in constants.ts to include the denominator and explicitly instruct the AI in geminiService.ts to use this format.
Updated files:
constants.ts
Updated the BLADE_DATABASE to include /5 in the Power and Control stats (e.g., "Power: 4/5") so the data source itself is unambiguous.
)

# Model yang Anda gunakan di AI Studio
MODEL_NAME = "gemini-2.5-flash" 


## 3. DESAIN ANTARMUKA STREAMLIT

st.set_page_config(page_title="Aplikasi Kustom AI Studio", page_icon="💡")
st.title("💡 Aplikasi Kustom AI Studio Anda")
st.markdown("---")

st.info(f"AI ini menggunakan persona: **{SYSTEM_PROMPT_ANDA[:80]}...**") # Menampilkan sebagian persona Anda

input_user = st.text_area(
    "Masukkan Kebutuhan / Data Anda:", 
    placeholder="Contoh: Buatkan rencana diet untuk berat 70kg dengan sesi latihan sore hari.",
    height=150
)

## 4. PEMANGGILAN MODEL DENGAN LOGIKA KUSTOM
if st.button("Jalankan Logika Kustom", type="primary"):
    if not input_user:
        st.warning("Mohon masukkan input.")
    else:
        try:
            with st.spinner("⏳ AI Kustom Anda sedang bekerja..."):
                # PEMANGGILAN GEMINI DENGAN SYSTEM PROMPT ANDA
                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=input_user,
                    config={"system_instruction": SYSTEM_PROMPT_ANDA} # <--- LOGIKA KUSTOM TERLAKSANA
                )
            
            st.subheader("✅ Hasil Logika Kustom:")
            st.markdown(response.text)

        except Exception as e:
            st.error(f"❌ Terjadi kesalahan pada pemanggilan API: {e}")