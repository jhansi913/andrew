import streamlit as st
import pdfplumber
from PIL import Image
import io

def extract_images_from_pdf(pdf_file):
    images = []
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            for img in page.images:
                images.append(img)
    return images

def main():
    st.title("PDF Image Extractor")

    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        st.markdown("## Images detected in PDF")

        # Extract images from the PDF
        images = extract_images_from_pdf(uploaded_file)

        if images:
            st.write(f"Number of images detected: {len(images)}")
            st.markdown("---")

            for i, img in enumerate(images):
                if img["stream"]:
                    image_data = img["stream"].getvalue()
                    try:
                        pil_image = Image.open(io.BytesIO(image_data))
                        st.image(pil_image, caption=f"Page {img['page_number']}, Image {i + 1}")
                    except Exception as e:
                        st.warning(f"Error displaying image {i + 1}: {e}")
                else:
                    st.warning(f"No image data found for image {i + 1}")

        else:
            st.write("No images found in the PDF.")

if __name__ == "__main__":
    main()
