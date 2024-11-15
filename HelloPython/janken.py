import random

x = 0
y = 1
# じゃんけんの「手」を定義
hands = ["グー", "チョキ", "パー"]

# 勝敗を判定する関数
def judge(a, b):
    global x, y
    if a == b:
        return "引き分け"
    elif (a == 0 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 0):
        x = x+1
        return "Aの勝ち"
    else:
        y = y+1
        return "Bの勝ち"

# じゃんけんをシミュレートする関数
n = 3
for i in range(n):
    def play_janken():
        a_hand = random.randint(0, 2)  # Aの手をランダムに選ぶ
        b_hand = random.randint(0, 2)  # Bの手をランダムに選ぶ

        # 結果を表示
        print(f"Aの手︓{hands[a_hand]} v.s. Bの手︓{hands[b_hand]} → {judge(a_hand, b_hand)}")
        
        if x == y:
            print("最終的な結果:引き分け")
        elif x>y:
            print("最終的な結果:Aの勝ち")
        else:
            print("最終的な結果:Bの勝ち")
        

    if __name__ == "__main__":
        play_janken()
