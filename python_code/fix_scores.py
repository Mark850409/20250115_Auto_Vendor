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
    # 錯誤的成績
    wrong_scores = [35, 46, 57, 91, 29]

    # 修正成績
    corrected_scores = fix_scores(wrong_scores)
    print("修正後的成績:", corrected_scores)
