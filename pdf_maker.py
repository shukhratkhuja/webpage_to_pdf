import os, re, img2pdf
from datetime import datetime
from log_config import get_logger

logger = get_logger("pdf_maker", "app.log")

def pdf_maker(screenshots_folder, pdf_files_folder):
    if os.path.isdir(screenshots_folder):
        logger.info(f"📂 Folder: {screenshots_folder}")

        # Taking sorted screenshots list
        images = sorted(
            [f for f in os.listdir(screenshots_folder) if f.endswith(".png")],
            key=lambda x: int(re.search(r'\d+', x).group())
        )

        if not images:
            logger.warning("⚠️ Image not found.")
            return

        # Taking each screenshot with full path
        image_paths = [os.path.join(screenshots_folder, img) for img in images]

        # Creating a pdf file from folder name
        folder_name_only = os.path.basename(screenshots_folder)
        
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        pdf_file_name = os.path.join(pdf_files_folder, f"{folder_name_only}_{timestamp}.pdf")

        # Creating PDF 
        with open(pdf_file_name, "wb") as f:
            logger.info("📄 Creating PDF...")
            f.write(img2pdf.convert(image_paths))

        logger.info(f"✅ PDF is ready: {pdf_file_name}\n")
