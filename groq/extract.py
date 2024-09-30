import pdfplumber
import os

def extract_text_and_images(pdf_file_path):
    image_folder = "extracted_images"
    os.makedirs(image_folder, exist_ok=True)  # Create folder for images

    with pdfplumber.open(pdf_file_path) as pdf:
        for i, page in enumerate(pdf.pages):
            # Extract text
            text = page.extract_text()
            if text:  # Only save if there's text
                with open(f'page_{i}.txt', 'w', encoding='utf-8') as text_file:
                    text_file.write(text)

            # Extract images
            images = page.images
            for img in images:
                img_data = page.to_image()
                img_data.save(os.path.join(image_folder, f'page_{i}_img.png'))  # Save images as PNG

# Loop through all PDFs in the us_sensus folder
pdf_folder_path = "us_sensus"
for filename in os.listdir(pdf_folder_path):
    if filename.endswith('.pdf'):
        extract_text_and_images(os.path.join(pdf_folder_path, filename))
         

print("Extraction complete.")
