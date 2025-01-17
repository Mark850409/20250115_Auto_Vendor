# 題目內容
# QA部門今天舉辦團康活動，有n個人圍成一圈，順序排號。從第一個人開始報數（從1到3報數），凡報到3的人退出圈子。請利用一段程式計算出，最後留下的那位同事，是所有同事裡面的第幾順位?

def last_person_standing(n):
    people = list(range(1, n + 1))  # 初始化人員列表
    index = 0  # 起始索引

    while len(people) > 1:
        index = (index + 2) % len(people)  # 每次跳到報數為3的位置
        people.pop(index)  # 移除報數為3的人

    return people[0]  # 剩下的最後一人

if __name__ == "__main__":
    while True:
        try:
            # 讀取使用者輸入
            user_input = input("請輸入團康活動的總人數 (輸入 'q' 結束程式): ")
            
            # 檢查是否要退出程式(不分大小寫)
            if user_input.lower() == 'q':
                print("程式結束")
                break
            
            # 轉換輸入為整數並驗證
            n = int(user_input)
            if n <= 0:
                print("請輸入大於0的正整數！")
                continue
                
            # 計算並顯示結果
            result = last_person_standing(n)
            print(f"在{n}人中，最後留下的同事是第 {result} 順位")
            # 加入分隔線進行輸出美化
            print("-" * 50)
            
        except ValueError:
            print("輸入無效！請輸入正整數。")
            continue