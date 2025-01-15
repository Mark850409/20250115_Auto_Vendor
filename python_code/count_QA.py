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
    # 測試最後留下的同事順位
    n = 10  # 假設有10個人
    print("最後留下的同事是第", last_person_standing(n), "順位")