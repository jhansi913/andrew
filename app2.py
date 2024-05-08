import streamlit as st
import fitz  # PyMuPDF
from PIL import Image

def extract_images_from_pdf(pdf_file):
    images = []
    pdf_document = fitz.open(pdf_file)

    for page_idx in range(len(pdf_document)):
        page = pdf_document[page_idx]
        image_list = page.get_images(full=True)
        
        for image_index, img in enumerate(image_list):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(io.BytesIO(image_bytes))
            images.append(image)

    pdf_document.close()
    return images

def main():
    st.title("PDF Image Cropper")

    # Upload PDF file
    pdf_file = st.file_uploader("Upload a PDF file", type="pdf")

    if pdf_file:
        st.write("PDF file uploaded!")

        # Extract images from PDF
        images = extract_images_from_pdf(pdf_file)

        if images:
            st.write(f"Number of images found in PDF: {len(images)}")

            # Display each image with cropper
            for i, image in enumerate(images):
                st.write(f"Image {i + 1}")
                cropped_image = st.cropper(image, realtime_update=True, aspect_ratio=(1, 1))
                st.image(cropped_image, caption=f"Cropped Image {i + 1}")

        else:
            st.warning("No images found in the PDF.")

if __name__ == "__main__":
    main()
