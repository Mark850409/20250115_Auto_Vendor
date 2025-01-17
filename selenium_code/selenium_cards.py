from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from config import config
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
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


def capture_discontinued_cards(driver):
    # 等待頁面完全加載
    wait_for_page_load(driver, timeout=15)
    logger.info("等待頁面完全加載！")

    # 點選左上角選單
    try:
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

        # 點選 "卡片介紹"
        card_intro = find_element(driver, "card_intro", timeout=5)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(card_intro))
        card_intro.click()
        logger.info("等待【卡片介紹】內容加載")

        # 找到 "停發卡" 區塊
        discontinued_section = find_element(driver, "discontinued_section", timeout=5)
        driver.execute_script("arguments[0].scrollIntoView();", discontinued_section)
        logger.info("找到【停發卡】區塊")

        # 找到 "停發卡" 區塊程式碼
        discontinued_component = find_element(driver, "discontinued_component", timeout=5)
        logger.info("找到【停發卡】區塊程式碼")

        # 抓取所有卡片
        cards = discontinued_component.find_elements(By.CSS_SELECTOR, config["elements"]["cards"]["value"])
        logger.info("抓取所有卡片")

        # 初始化計數器
        discontinued_count = len(cards)
        logger.info(f"停發卡區塊中有 {discontinued_count} 張卡片")

        # 遍歷每張卡片並截圖
        for index, card in enumerate(cards):
            # 滾動到卡片位置
            driver.execute_script("arguments[0].scrollIntoView();", card)
            logger.info("滾動到卡片位置")

            # 調整視窗大小並設置精確的滾動位置
            driver.set_window_size(config["screenshot_window_size"]["width"], config["screenshot_window_size"]["height"])
            driver.execute_script("window.scrollBy(0, -220);")  # 往上微調滾動位置
            logger.info("調整視窗大小並設置精確的滾動位置")

            # 截圖並保存
            screenshot_cards_path = f'{config["screenshot_cards_path"]}_{index + 1}.png'
            driver.save_screenshot(screenshot_cards_path)
            logger.info(f"第 {index + 1} 張卡片的截圖已保存至 {screenshot_cards_path}")
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
        capture_discontinued_cards(driver)
    finally:
        # 確保瀏覽器被正確關閉
        driver.quit()
        logger.info("瀏覽器已正確關閉")