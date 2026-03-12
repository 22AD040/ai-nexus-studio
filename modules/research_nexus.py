import streamlit as st
from utils.gemini_client import ask_gemini

def research_page():
    st.header("🔎 Research Nexus")

    query = st.text_area("Enter research topic")

    if st.button("Generate Research"):

        prompt = f"""
        Provide a structured research summary about: {query}

        Include the following sections:

        1. Introduction to the topic
        2. Key concepts and background
        3. Current research trends
        4. Applications and real-world use cases
        5. Challenges and future research directions

        Also recommend 5 relevant research papers related to this topic from sources like:
        - Google Scholar
        - ResearchGate
        - Academia.edu
        - Scribbr

        For each paper include:
        • Paper Title
        • Authors
        • Year
        • Short contribution summary
        • Source platform
        """

        result = ask_gemini(prompt)

        st.write(result)