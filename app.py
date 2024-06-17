import streamlit as st
from PIL import Image
import io
from backend import start


def process_image(image):
    # Convert PIL image to bytes
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='JPEG')
    img_byte_arr = img_byte_arr.getvalue()

    # Call your backend function to analyze the image
    response = start(img_byte_arr)

    # Extract and return the processed results (you can modify this according to your backend code)
    processed_results = ""
    for annotation in response:
        processed_results += f"{annotation}\n"
    return processed_results


def main():
    st.title("Image Processing with Streamlit")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Process the uploaded image
        if st.button("Process"):
            with st.spinner('Processing...'):
                processed_results = process_image(image)
            st.success("Processing completed!")

            # Display the processed results
            st.subheader("Processed Results:")
            st.text_area("Text", value=processed_results, height=500, label_visibility="hidden")


if __name__ == "__main__":
    main()
