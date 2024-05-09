import streamlit as st
import fitz  # PyMuPDF

def crop_pdf(input_pdf_path, output_pdf_path, x1, y1, x2, y2):
    # Open the input PDF file
    pdf_doc = fitz.open(input_pdf_path)

    # Iterate through each page and apply cropping
    for page in pdf_doc:
        page.crop((x1, y1, x2, y2))

    # Save the cropped PDF to the output file
    pdf_doc.save(output_pdf_path)
    pdf_doc.close()

def main():
    st.title("PDF Cropper")

    # Upload the PDF file
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        st.markdown("## Define Cropping Region")

        # Define cropping coordinates
        x1 = st.number_input("Left", value=0)
        y1 = st.number_input("Top", value=0)
        x2 = st.number_input("Right", value=100)
        y2 = st.number_input("Bottom", value=100)

        # Define output PDF path
        output_pdf_path = "cropped_output.pdf"

        if st.button("Crop PDF"):
            # Crop the uploaded PDF file
            crop_pdf(uploaded_file, output_pdf_path, x1, y1, x2, y2)

            # Provide download link for the cropped PDF file
            st.markdown(get_binary_file_downloader_html(output_pdf_path, 'Download Cropped PDF'), unsafe_allow_html=True)

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = data.encode('base64').decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{bin_file}" target="_blank">{file_label}</a>'
    return href

if __name__ == "__main__":
    main()

