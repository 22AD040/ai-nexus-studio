import streamlit as st
from utils.gemini_client import ask_gemini

def coding_page():
    st.header("💻 Coding Nexus")

    prompt = st.text_area("Describe coding problem")

    if st.button("Generate Code"):

        query = f"""
        You are an expert software engineer.

        User request:
        {prompt}

        Provide:

        1. Explanation of the problem
        2. Correct programming language code
        3. Clean optimized code
        4. Comments inside the code
        5. Example input/output
        6. Best practices
        7. Complexity analysis if relevant
        """

        result = ask_gemini(query)

        st.markdown(result)