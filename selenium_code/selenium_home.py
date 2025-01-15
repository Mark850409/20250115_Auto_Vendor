from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def capture_home(driver):
    # 調整視窗大小以適配截圖
    driver.set_window_size(375, 812)

    # 等待頁面加載
    time.sleep(5)

    # 截圖並保存
    screenshot_path = 'images/selenium_result/home/cathaybk_mobile_screenshot.png'
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
    capture_home(driver)

    # 關閉瀏覽器
    driver.quit()