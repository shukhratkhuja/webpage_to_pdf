# Web Page to PDF Automation Tool

This project automates the process of capturing full-page screenshots from a list of URLs, scrolling dynamically through each page, and generating clean, timestamped PDF files. It's ideal for archiving dynamic content, legal documentation, or web monitoring.

---

## 🚀 Features

- **Undetected Automation**: Uses `undetected_chromedriver` to avoid bot detection.
- **Full Page Scrolling**: Automatically scrolls through the page and captures sections.
- **Overlap Handling**: Screenshots are taken with slight overlap and combined seamlessly.
- **Organized Output**: Screenshots and PDFs are organized per URL.
- **Timestamped Files**: Each screenshot and PDF is timestamped for traceability.
- **Batch Processing**: Handles multiple URLs from a text file.

---

## 🛠 Tech Stack

- Python 3.10.12
- Selenium + undetected_chromedriver
- Pillow (Image cropping)
- img2pdf (PDF generation)

---

## 📂 Project Structure
**/screenshots/** - Per-URL screenshot folders 
**/pdf_files/** - Generated PDF files 
**/urls.txt** - List of URLs to process 
**main.py** - Entry point for running the script 
**screenshoter.py** - Scroll and capture logic 
**pdf_maker.py** - Combine screenshots into a PDF 
**requirements.txt** - Python package dependencies

---

## 📋 How to Use

1. **Clone the repository:**
   # bash
   git clone https://github.com/shukhratkhuja/webpage_to_pdf.git
   cd webpage_to_pdf

2. **Install dependencies:**

    # bash
    pip install -r requirements.txt

3.  **Add URLs:**
- Create or edit urls.txt
- One URL per line.

4. **Run the script:**

    # bash
    python main.py
5. **Outputs:**
- Screenshots: screenshots/
- PDFs: pdf_files/

**📝 Example Output**
- Screenshots: part_1_2024-04-28_15-45-10.png, part_2_2024-04-28_15-45-30.png
- PDF: https___example_com_2024-04-28_15-46-00.pdf

---

**💡 Use Cases**
Legal evidence collection (e.g., trademark infringement)
Web content archiving
Automated website monitoring
Report generation from dynamic web pages

---

**🙌 Contributions**
Contributions are welcome! Feel free to fork this project or open issues for improvements.

---

**✉️ Contact**
For any inquiries, feel free to reach out via GitHub or email.