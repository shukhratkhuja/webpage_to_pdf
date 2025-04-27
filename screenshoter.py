import os, re
from datetime import datetime
from log_config import get_logger
from pdf_maker import pdf_maker

logger = get_logger("screenshoter", "app.log")
    
def webpage_to_pdf(url, driver, screenshots_folder, pdf_files_folder):

    logger.info(f"🔗 URL: {url}")
    driver.get(url)

    # Creating a folder based on URL
    safe_folder_name = re.sub(r'\W+', '_', url)  # Creating safe name from URL
    folder_path = os.path.join(screenshots_folder, safe_folder_name)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

     # Window height (Here the full screen size is taken as 1080x1920)
    window_height = 1080
    overlap = 90  # Overlapping 90 pxs for each screenshot (This value taken based on tests)
    driver.set_window_size(1920, window_height)

    total_height = driver.execute_script("return document.body.scrollHeight")
    scroll_position = 0
    screenshot_count = 1

    # Scrolling and taking screenshot
    while scroll_position < total_height:

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_name = os.path.join(folder_path, f"part_{screenshot_count}_{timestamp}.png")
        
        driver.save_screenshot(screenshot_name)
        logger.info(f"✅ Saved: {screenshot_name}")

        scroll_position += (window_height - overlap)  # Scrolling with overlap
        driver.execute_script(f"window.scrollTo(0, {scroll_position});")

        screenshot_count += 1
        total_height = driver.execute_script("return document.body.scrollHeight")

    pdf_maker(screenshots_folder=folder_path, pdf_files_folder=pdf_files_folder)
