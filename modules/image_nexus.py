import streamlit as st
from PIL import Image
from google import genai
import os


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def image_page():

    st.header("🖼️ Image Analysis Nexus")

    uploaded_file = st.file_uploader(
        "Upload Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:

        image = Image.open(uploaded_file)

        st.image(image, width=450)

        if st.button("Analyze Image"):

            prompt = """
You are a professional computer vision expert.

Analyze the uploaded image carefully and accurately.

Provide:

1. Main objects present in the image
2. Scene description
3. Activities happening
4. Environment / location
5. Colors and visual elements
6. Overall interpretation

Important:
Only describe what is actually visible in the image.
Do NOT hallucinate objects or scenes.
"""

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[prompt, image]
            )

            st.success("Image Analysis")

            st.write(response.text)