# 題目內容
# 國泰銀行要慶祝六十周年，需要買字母貼紙來布置活動空間，文字為"Hello welcome to Cathay 60th year anniversary"，請寫一個程式計算每個字母(大小寫視為同個字母)出現次數
def count_letters(text):
    # 初始化字母計數字典
    letter_count = {}

    for char in text:
        if char.isalpha():  # 檢查是否為字母
            char = char.lower()  # 將字母轉為小寫
            letter_count[char] = letter_count.get(char, 0) + 1

    return letter_count

if __name__ == "__main__":
    # 活動文字
    text = "Hello welcome to Cathay 60th year anniversary"

    # 計算每個字母出現次數
    letter_counts = count_letters(text)

    # 格式化輸出
    print("輸出：")
    for letter, count in sorted(letter_counts.items()):
        print(f"{letter.upper()} {count}")
