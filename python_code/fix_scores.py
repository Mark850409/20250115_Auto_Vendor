# 題目內容
# 國泰補習班中，有五位學生期中考的成績分別為[53, 64, 75, 19, 92]，但是老師在輸入成績的時候看反了，把五位學生的成績改成了[35, 46, 57, 91, 29]，請用一個函數來將學生的成績修正。

# 程式碼
def fix_scores(wrong_scores):
    # 原始的錯誤成績
    correct_scores = []

    for score in wrong_scores:
        reversed_score = int(str(score)[::-1])  # 將數字轉為字串後反轉，再轉回整數
        correct_scores.append(reversed_score)

    return correct_scores

if __name__ == "__main__":
    while True:
        try:
            # 讀取使用者輸入的成績，用逗號分隔
            scores_input = input("請輸入錯誤的成績(多筆成績請用逗號分隔，例如: 35,46,57,91,29)\n輸入'q'結束程式: ")
            
            # 檢查是否要退出程式(不分大小寫)
            if scores_input.lower() == 'q':
                print("程式結束")
                break
            
            # 分割字串並轉換為整數列表
            wrong_scores = [int(score.strip()) for score in scores_input.split(',')]
            
            # 修正成績
            corrected_scores = fix_scores(wrong_scores)
            print("修正後的成績:", corrected_scores)
            # 加入分隔線進行輸出美化
            print("-" * 50)
        
        except ValueError:
            print("輸入格式錯誤！請確認輸入的是數字，並用逗號分隔。")
            print("-" * 50)

    
