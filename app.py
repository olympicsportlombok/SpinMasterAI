import streamlit as st
from google import genai

# KONEKSI KE GOOGLE AI STUDIO (AMAN)
api_key = st.secrets["API_KEY"]
client = genai.Client(api_key=api_key)

st.title("SpinMaster AI by Olympic Sport Lombok")

input_user = st.text_area("Masukkan pertanyaan / data:")

if st.button("Kirim"):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=input_user
    )
    st.subheader("Hasil:")
    st.write(response.text)
