import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils.gemini_client import ask_gemini


def data_page():

    st.header("📊 Data Analysis Nexus")

    file = st.file_uploader("Upload CSV Dataset", type=["csv"])

    if file:

        df = pd.read_csv(file)


        st.subheader("📌 Dataset Overview")
        rows = df.shape[0]
        cols = df.shape[1]
        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"""
            ### 📊 Dataset Size

            **Rows:** `{rows}`  
            **Columns:** `{cols}`
            """)

        with col2:
            st.markdown(f"""
            <div style="background:#13223d;padding:15px;border-radius:10px">
            <b>Dataset Explanation</b><br><br>
            This dataset contains <b>{rows}</b> rows and <b>{cols}</b> columns.<br>
            Each column represents a feature used for analysis.
            </div>
            """,
            unsafe_allow_html=True
            )
        st.write("Missing Values:")
        st.dataframe(df.isnull().sum().to_frame("Missing Values"), height=250)
        st.write("Data Types:")
        st.write(df.dtypes)

        st.markdown("---")


        st.subheader("Preview Data")
        st.dataframe(df.head(), height=300, use_container_width=True)
        st.markdown("---")

        st.subheader("🔍 Column Explorer")

        column = st.selectbox("Select Column", df.columns)

        st.write("Column Statistics")
        st.write(df[column].describe())

        st.markdown("---")

        st.subheader("📊 Visualizations")

        viz_type = st.selectbox(
            "Choose Visualization",
            ["Histogram", "Scatter Plot", "Box Plot"]
        )

        if viz_type == "Histogram":

            fig, ax = plt.subplots(figsize=(6,4))
            ax.hist(df[column].dropna())
            st.pyplot(fig)

        elif viz_type == "Scatter Plot":

            x = st.selectbox("X Axis", df.columns)
            y = st.selectbox("Y Axis", df.columns)

            fig, ax = plt.subplots(figsize=(6,4))
            ax.scatter(df[x], df[y])
            ax.set_xlabel(x)
            ax.set_ylabel(y)
            st.pyplot(fig)

        elif viz_type == "Box Plot":

            fig, ax = plt.subplots(figsize=(6,4))
            sns.boxplot(x=df[column], ax=ax)
            st.pyplot(fig)

        st.markdown("---")


        st.subheader("🔥 Correlation Heatmap")

        numeric_df = df.select_dtypes(include=["number"])

        if len(numeric_df.columns) > 1:

            fig, ax = plt.subplots(figsize=(7, 4))
            sns.heatmap(
                numeric_df.corr(),
                annot=True,
                cmap="coolwarm",
                ax=ax
            )

            st.pyplot(fig)

        else:
            st.warning("Not enough numeric columns for correlation.")

        st.markdown("---")


        st.subheader("🧹 Data Cleaning Tools")

        if st.button("Remove Missing Values"):
            df = df.dropna()
            st.success("Missing values removed")

        if st.button("Remove Duplicate Rows"):
            df = df.drop_duplicates()
            st.success("Duplicates removed")

        st.markdown("---")

        st.subheader("🧠 AI Data Insights")

        if st.button("Generate AI Insights"):

            summary = df.describe().to_string()

            prompt = f"""
            Analyze this dataset summary and provide insights:

            {summary}

            Provide:
            - Important patterns
            - Interesting correlations
            - Possible predictions
            - Business insights
            """

            insights = ask_gemini(prompt)

            st.write(insights)

        st.markdown("---")

        st.subheader("📥 Download Clean Dataset")

        csv = df.to_csv(index=False)

        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="clean_dataset.csv",
            mime="text/csv"
        )