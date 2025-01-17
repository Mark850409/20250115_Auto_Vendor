from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from config import config
import logging

# 設置日誌模板
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def wait_for_page_load(driver, timeout=5):
    """
    等待頁面完全加載
    """
    WebDriverWait(driver, timeout).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

def capture_home(driver):
    # 等待頁面完全加載
    wait_for_page_load(driver)
    logger.info("等待頁面完全加載！")

    # 截圖並保存
    screenshot_home_path = config["screenshot_home_path"]
    driver.save_screenshot(screenshot_home_path)
    logger.info(f"截圖已保存至 {screenshot_home_path}")

if __name__ == "__main__":
     # 初始化瀏覽器
    chrome_options = Options()
    chrome_options.add_argument(f"--app={config['base_url']}")

    # 設定手機版的 user-agent 和視窗大小
    chrome_options.add_experimental_option("mobileEmulation", config["mobile_emulation"])

    # 自動下載並啟動 ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 設定視窗大小
    driver.set_window_size(config["window_size"]["width"], config["window_size"]["height"])

    try:
        # 呼叫函數
        capture_home(driver)
    finally:
        # 確保瀏覽器被正確關閉
        driver.quit()
        logger.info("瀏覽器已正確關閉")