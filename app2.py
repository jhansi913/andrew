import streamlit as st
import pdf2image
import zipfile
import os
from io import BytesIO

# https://discuss.streamlit.io/t/how-to-download-image/3358/10


pdf_uploaded = st.file_uploader("Select a file", type="pdf")
button = st.button("Confirm")
image_down = []
st.write("test1")
if button and pdf_uploaded is not None:
    st.write("test2")
    if pdf_uploaded.type == "application/pdf":
        st.write("test3")
        images = pdf2image.convert_from_bytes(pdf_uploaded.read())
        for i, page in enumerate(images):
            st.write(i)
            st.write(page)
            st.image(page, use_column_width=True)
            img = page
            buf = BytesIO()
            img.save(buf, format="JPEG")
            byte_im = buf.getvalue()
            st.download_button("Download", data=byte_im, file_name=f"Image_{i}.png")
