from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from config import config
from selenium.common.exceptions import TimeoutException, NoSuchElementException
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

def find_element(driver, config_key, timeout=10):
    """
    尋找指定的元素，增加錯誤處理
    """
    try:
        element_config = config["elements"].get(config_key)
        if not element_config:
            raise ValueError(f"Config key {config_key} not found in config.")
        locator_type = By.XPATH if element_config["type"] == "XPATH" else By.CSS_SELECTOR
        locator_value = element_config["value"]
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((locator_type, locator_value))
        )
    except TimeoutException:
        logger.error(f"查找元素 {config_key} 時超時，請檢查定位條件：{element_config}")
        raise
    except NoSuchElementException:
        logger.error(f"元素 {config_key} 無法找到，請確認是否存在：{element_config}")
        raise
    except Exception as e:
        logger.error(f"查找元素 {config_key} 時發生未知錯誤：{str(e)}")
        raise

def capture_credit_card_list(driver):
    # 等待頁面完全加載
    wait_for_page_load(driver)
    logger.info("等待頁面完全加載！")

    try:
        # 點選左上角選單
        menu_button = find_element(driver, "menu_button", timeout=5)
        menu_button.click()
        logger.info("點選左上角選單")

        # 等待 "產品介紹" 元素存在並點擊
        product_intro = find_element(driver, "product_intro", timeout=5)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(product_intro))
        product_intro.click()
        logger.info("等待【產品介紹】元素存在並點擊")

        # 等待 "信用卡列表" 元素存在並點擊
        credit_card_list = find_element(driver, "credit_card_list", timeout=5)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(credit_card_list))
        credit_card_list.click()
        logger.info("等待【信用卡列表】元素存在並點擊")

        # 等待信用卡列表內容加載
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config["elements"]["menu_sort_btn"]["value"]))
        )
        logger.info("等待【信用卡列表】內容加載")

        # 抓取 "menu_sort_btn" 區塊內的所有文字
        menu_sort_btn = find_element(driver, "menu_sort_btn", timeout=5)
        list_items = menu_sort_btn.find_elements(By.CSS_SELECTOR, config["elements"]["menu_link_list"]["value"])

        # 過濾掉空白的元素
        non_empty_href_elements = [elem for elem in list_items if elem.text.strip()]
        
        # 輸出列表中的項目
        item_count = len(non_empty_href_elements)
        logger.info(f"信用卡列表中有 {item_count} 個項目")

        # 輸出每個項目的文字
        for index, text in enumerate([item.text.strip() for item in non_empty_href_elements], start=1):
            logger.info(f"項目 {index}: {text}")

        # 截圖並保存
        screenshot_credit_card_list_path = config["screenshot_credit_card_list_path"]
        driver.save_screenshot(screenshot_credit_card_list_path)
        logger.info(f"截圖已保存至 {screenshot_credit_card_list_path}")
    except Exception as e:
            logger.error(f"發生錯誤，請檢查程式碼!\n{str(e)}")
            raise

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
        capture_credit_card_list(driver)
    finally:
        # 確保瀏覽器被正確關閉
        driver.quit()
        logger.info("瀏覽器已正確關閉")
