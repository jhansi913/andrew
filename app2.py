import streamlit as st
import pdfplumber
from PIL import Image

def extract_images_from_pdf(pdf_file):
    images = []
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            for img in page.images:
                try:
                    img_data = pdf.extract_image(img['xref'])
                    if img_data['image']:
                        pil_image = Image.open(img_data['image'])
                        images.append(pil_image)
                except Exception as e:
                    st.warning(f"Error extracting image: {e}")
    return images

def crop_images(images, crop_box):
    cropped_images = []
    for img in images:
        try:
            cropped_img = img.crop(crop_box)
            cropped_images.append(cropped_img)
        except Exception as e:
            st.warning(f"Error cropping image: {e}")
    return cropped_images

def main():
    st.title("PDF Image Cropper")

    # Upload PDF file
    pdf_file = st.file_uploader("Upload a PDF file", type="pdf")
    
    if pdf_file:
        st.write("PDF file uploaded!")

        # Define crop box
        crop_box = st.sidebar.text_input("Crop Box (left, upper, right, lower)", value="100, 100, 400, 400")
        crop_box = tuple(map(int, crop_box.split(',')))

        # Extract images from PDF
        images = extract_images_from_pdf(pdf_file)

        if images:
            st.write(f"Number of images found in PDF: {len(images)}")

            # Crop images
            cropped_images = crop_images(images, crop_box)

            # Display cropped images
            st.write("Cropped Images:")
            for i, cropped_img in enumerate(cropped_images):
                st.image(cropped_img, caption=f"Cropped Image {i+1}")

        else:
            st.warning("No images found in the PDF.")

if __name__ == "__main__":
    main()
