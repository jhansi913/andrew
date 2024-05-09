import streamlit as st

def main():
    st.title("PDF Viewer")

    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        st.markdown("## Displaying PDF content")
        st.pdf_viewer(uploaded_file)

if __name__ == "__main__":
    main()
