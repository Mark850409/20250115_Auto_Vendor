from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


def capture_discontinued_cards(driver):
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
    time.sleep(2)

    # 點選 "卡片介紹"
    card_intro = driver.find_element(By.CSS_SELECTOR, '#lnk_Link')
    card_intro.click()

    # 等待頁面加載
    time.sleep(5)

    # 找到 "停發卡" 區塊
    discontinued_section = driver.find_element(By.XPATH, "//div[contains(@class, 'cubre-a-iconTitle__text') and text()='停發卡']")
    driver.execute_script("arguments[0].scrollIntoView();", discontinued_section)
    time.sleep(2)  # 等待滾動完成

    # 找到 "停發卡" 區塊程式碼
    discontinued_component = discontinued_section.find_element(By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[1]")

    # 抓取所有卡片
    cards = discontinued_component.find_elements(By.CSS_SELECTOR, '.cubre-o-slide__item')

    # 初始化計數器
    discontinued_count = len(cards)
    print(f"停發卡區塊中有 {discontinued_count} 張卡片")

    # 遍歷每張卡片並截圖
    for index, card in enumerate(cards):
        # 滾動到卡片位置
        driver.execute_script("arguments[0].scrollIntoView();", card)
        time.sleep(1)  # 等待滾動完成

        # 調整視窗大小並設置精確的滾動位置
        driver.set_window_size(375, 1200)
        driver.execute_script("window.scrollBy(0, -220);")  # 往上微調滾動位置
        time.sleep(2)  # 等待滾動完成

        # 截圖並保存
        screenshot_path = f'images/selenium_result/cards/discontinued_card_screenshot_{index + 1}.png'
        driver.save_screenshot(screenshot_path)
        print(f"第 {index + 1} 張卡片的截圖已保存至 {screenshot_path}")


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
    capture_discontinued_cards(driver)

    # 關閉瀏覽器
    driver.quit()