import os
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from screenshoter import webpage_to_pdf
from dotenv import load_dotenv

load_dotenv()


HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
# Screenshots main folder
SCREENSHOTS_FOLDER = "screenshots"
# Pdf files folder
PDF_FILES_FOLDER = "pdf_files"

# Method to create web driver
def get_driver():

    # Brauzer opsiyalar
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")
    if HEADLESS:
        options.add_argument("--headless")  # if needed

    driver = uc.Chrome(options=options)
    return driver

# Method to read urls from urls.txt file
def get_urls():

    urls_list = []
    with open("urls.txt", "r") as f:
        urls = f.readlines()
        for url in urls:
            if url:
                urls_list.append(url.strip())

    return urls_list


def main():

    # Creating folders for output
    if not os.path.exists(SCREENSHOTS_FOLDER):
        os.makedirs(SCREENSHOTS_FOLDER)

    if not os.path.exists(PDF_FILES_FOLDER):
        os.makedirs(PDF_FILES_FOLDER)

    # get undetected chromedriver
    driver = get_driver()

    # get urls
    urls = get_urls()

    # Creating pdf files one by one for each url
    for url in urls:
        webpage_to_pdf(url=url, 
                       driver=driver, 
                       screenshots_folder=SCREENSHOTS_FOLDER, 
                       pdf_files_folder=PDF_FILES_FOLDER)

    driver.quit()

if __name__ == "__main__":
    
    main()
