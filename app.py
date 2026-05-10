import streamlit as st
from utils import extract_text_from_pdf, summarize_text

# Page configuration
st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.stTextArea textarea {
    font-size: 16px;
}

.summary-box {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #ddd;
}

</style>
""", unsafe_allow_html=True)

# Title
st.title("🧠 AI-Based Text Summarization Platform")

st.write("""
Upload a PDF or enter text manually to generate an AI-powered summary.
""")

# Sidebar
st.sidebar.header("Settings")

summary_length = st.sidebar.slider(
    "Summary Length",
    min_value=50,
    max_value=300,
    value=150
)

# Input Options
option = st.radio(
    "Choose Input Type",
    ["Text Input", "PDF Upload"]
)

text = ""

# Text Input
if option == "Text Input":

    text = st.text_area(
        "Enter your text here",
        height=300
    )

# PDF Upload
elif option == "PDF Upload":

    uploaded_file = st.file_uploader(
        "Upload PDF File",
        type=["pdf"]
    )

    if uploaded_file is not None:

        with st.spinner("Extracting text from PDF..."):

            text = extract_text_from_pdf(uploaded_file)

        st.success("PDF text extracted successfully!")

        with st.expander("View Extracted Text"):
            st.write(text[:5000])

# Summarize Button
if st.button("Generate Summary"):

    if text.strip() == "":
        st.warning("Please provide text or upload a PDF.")

    else:

        with st.spinner("Generating summary using AI..."):

            summary = summarize_text(
                text,
                max_len=summary_length
            )

        st.success("Summary Generated Successfully!")

        st.subheader("📌 Summary")

        st.markdown(
            f"""
            <div class="summary-box">
            {summary}
            </div>
            """,
            unsafe_allow_html=True
        )

        # Download Button
        st.download_button(
            label="Download Summary",
            data=summary,
            file_name="summary.txt",
            mime="text/plain"
        )
        