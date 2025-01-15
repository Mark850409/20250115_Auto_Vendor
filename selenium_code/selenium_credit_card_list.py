from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def capture_credit_card_list(driver):
    # 調整視窗大小以適配截圖
    driver.set_window_size(375, 812)

    # 等待頁面加載
    time.sleep(5)

    # 點選左上角選單
    menu_button = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/a/img[2]')
    menu_button.click()

    # 等待選單展開
    time.sleep(2)

    # 點選 "產品介紹"
    product_intro = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[1]/div')
    product_intro.click()

    # 等待頁面加載
    time.sleep(2)

    # 點選 "信用卡列表"
    credit_card_list = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div')
    credit_card_list.click()

    # 等待頁面加載
    time.sleep(5)

    # 抓取 "cubre-o-menuLinkList__content" 區塊內的所有文字並計算數量
    menu_sort_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.cubre-o-nav__content'))
    )
    list_items = menu_sort_btn.find_elements(By.CSS_SELECTOR, '.cubre-o-menuLinkList__content>a')

    # 判斷如果是空元素則不抓取
    non_empty_href_elements = [elem for elem in list_items if elem.text.strip() != '']
    item_count = len(non_empty_href_elements)
    print(f"信用卡列表中有 {item_count} 個項目")

    item_texts = [item.text.strip() for item in non_empty_href_elements]

    # 列印所有項目文字內容供檢查
    for index, text in enumerate(item_texts, start=1):
        print(f"項目 {index}: {text}")

    # 截圖並保存
    screenshot_path = 'images/selenium_result/credit_card_list/credit_card_list_screenshot.png'
    driver.save_screenshot(screenshot_path)

    print(f"截圖已保存至 {screenshot_path}")


if __name__ == "__main__":
    # 初始化瀏覽器
    # 設定 Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--app=https://www.cathaybk.com.tw/cathaybk/')

    # 設定手機版的 user-agent 和視窗大小
    mobile_emulation = {
        "deviceMetrics": {"width": 375, "height": 812, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Mobile/15E148 Safari/604.1"
    }
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    # 自動下載並啟動 ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 呼叫函數
    capture_credit_card_list(driver)

    # 關閉瀏覽器
    driver.quit()