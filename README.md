# 專案簡介

此專案包含使用 Selenium 自動化測試的腳本以及一些 Python 程式碼範例。

## 專案結構

- `images/`: 存放截圖結果的目錄
  - `code_result/`: 存放程式碼執行結果的截圖
  - `mind_map_result/`: 存放心智圖結果的截圖
  - `selenium_result/`: 存放 Selenium 測試結果的截圖
    - `cards/`: 存放停發卡片的截圖
    - `credit_card_list/`: 存放信用卡列表的截圖
    - `home/`: 存放首頁的截圖
- `python_code/`: 存放 Python 程式碼
  - `count_letters.py`: 計算字母出現次數的程式
  - `count_QA.py`: 計算 QA 部門團康活動最後留下的同事順位的程式
  - `fix_scores.py`: 修正學生成績的程式
- `selenium_code/`: 存放 Selenium 自動化測試腳本
  - `selenium_home.py`: 截取首頁截圖的腳本
  - `selenium_credit_card_list.py`: 截取信用卡列表截圖的腳本
  - `selenium_cards.py`: 截取停發卡片截圖的腳本
- `requirements.txt`: 專案所需的 Python 套件
- `README.md`: 專案說明文件

## 目錄說明

- [專案簡介](#專案簡介)
  - [專案結構](#專案結構)
  - [目錄說明](#目錄說明)
  - [如何使用](#如何使用)

## 如何使用

1. 安裝必要的 Python 套件：

    ```sh
    pip install -r requirements.txt
    ```

2. 執行 Selenium 自動化測試腳本：

    - 執行 `selenium_home.py`：

        ```sh
        python selenium_code/selenium_home.py
        ```

    - 執行 `selenium_credit_card_list.py`：

        ```sh
        python selenium_code/selenium_credit_card_list.py
        ```

    - 執行 `selenium_cards.py`：

        ```sh
        python selenium_code/selenium_cards.py
        ```

3. 執行 Python 程式碼範例：

    - 計算字母出現次數：

        ```sh
        python python_code/count_letters.py
        ```

    - 計算 QA 部門團康活動最後留下的同事順位：

        ```sh
        python python_code/count_QA.py
        ```

    - 修正學生成績：

        ```sh
        python python_code/fix_scores.py
        ```