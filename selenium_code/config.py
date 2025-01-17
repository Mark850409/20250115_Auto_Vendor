config = {
    "base_url": "https://www.cathaybk.com.tw/cathaybk/",
    "mobile_emulation": {
        "deviceMetrics": {"width": 375, "height": 812, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Mobile/15E148 Safari/604.1"
    },
    "window_size": {"width": 375, "height": 812},
    "screenshot_window_size": {"width": 375, "height": 1200},
    "elements": {
        "menu_button": {"type": "XPATH", "value": "/html/body/div[1]/header/div/div[1]/a/img[2]"},
        "product_intro": {"type": "XPATH", "value": "//div[contains(@class, 'cubre-a-menuSortBtn') and contains(text(), '產品介紹')]"},
        "credit_card_list": {"type": "XPATH", "value": "//div[contains(@class, 'cubre-a-menuSortBtn') and contains(text(), '信用卡')]"},
        "menu_sort_btn": {"type": "CSS_SELECTOR", "value": ".cubre-o-nav__content"},
        "menu_link_list": {"type": "CSS_SELECTOR", "value": ".cubre-o-menuLinkList__content>a"},
        "card_intro": {"type": "CSS_SELECTOR", "value": "#lnk_Link"},
        "discontinued_section": {"type": "XPATH", "value": "//div[contains(@class, 'cubre-a-iconTitle__text') and text()='停發卡']"},
        "discontinued_component": {"type": "XPATH", "value": "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[1]"},
        "cards": {"type": "CSS_SELECTOR", "value": ".cubre-o-slide__item"}
    },
    "screenshot_credit_card_list_path": "images/selenium_result/credit_card_list/credit_card_list_screenshot.png",
    "screenshot_home_path" : "images/selenium_result/home/cathaybk_mobile_screenshot.png",
    "screenshot_cards_path": "images/selenium_result/cards/discontinued_card_screenshot"
}
