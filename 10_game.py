import random

def hangman(word):
    wrong = 0
    stages = ["",
              "________       ",
              "|              ",
              "|      |       ",
              "|      0       ",
              "|     /|\      ",
              "|     / \      ",
              "|              "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字予想してね！"
        char = input(msg)
        if char in rletters:
            cild = rletters.index(char)
            board[cild] = char
            rletters[cild] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}.".format(word))

work_list = ["cat","dog","dug","cow"]

hangman(work_list[random.randint(0,3)])

