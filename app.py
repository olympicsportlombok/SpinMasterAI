import streamlit as st
from google import genai

# KONEKSI KE GOOGLE AI STUDIO
client = genai.Client(api_key="ISI_API_KEY_KAMU_DI_SINI")

st.title("SpinMaster AI by Olympic Sport Lombok")

input_user = st.text_area("Masukkan pertanyaan / data:")

if st.button("Kirim"):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",   # ⬅️ MODEL GRATIS
            contents=input_user
        )
        st.subheader("Hasil:")
        st.write(response.text)

    except Exception as e:
        st.error(f"Terjadi error: {e}")
