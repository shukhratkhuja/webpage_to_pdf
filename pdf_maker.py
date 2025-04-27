import os
import img2pdf
import re
from datetime import datetime


def pdf_maker(screenshots_folder, pdf_files_folder):
    if os.path.isdir(screenshots_folder):
        print(f"📂 Folder: {screenshots_folder}")

        # Taking sorted screenshots list
        images = sorted(
            [f for f in os.listdir(screenshots_folder) if f.endswith(".png")],
            key=lambda x: int(re.search(r'\d+', x).group())
        )

        if not images:
            print("⚠️ Image not found.")
            return

        # Taking each screenshot with full path
        image_paths = [os.path.join(screenshots_folder, img) for img in images]

        # Creating a pdf file from folder name
        folder_name_only = os.path.basename(screenshots_folder)
        
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        pdf_file_name = os.path.join(pdf_files_folder, f"{folder_name_only}_{timestamp}.pdf")

        # Creating PDF 
        with open(pdf_file_name, "wb") as f:
            print("📄 Creating PDF...")
            f.write(img2pdf.convert(image_paths))

        print(f"✅ PDF is ready: {pdf_file_name}\n")
