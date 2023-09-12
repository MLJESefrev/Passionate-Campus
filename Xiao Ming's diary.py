import time

def intro():
    print("欢迎来到校园日记游戏！")
    time.sleep(1)
    print("你是小明，一个普通的中学生。")
    time.sleep(1)
    print("今天是个新的一天，你要做什么呢？")
    time.sleep(1)

def start_game():
    intro()
    while True:
        print("\n选择一个行动：")
        print("1. 去上课")
        print("2. 参加社团活动")
        print("3. 回家做作业")
        print("4. 退出游戏")
        
        choice = input("请输入选项的数字：")
        
        if choice == "1":
            go_to_class()
        elif choice == "2":
            join_club()
        elif choice == "3":
            do_homework()
        elif choice == "4":
            print("谢谢你玩校园日记游戏！再见！")
            break
        else:
            print("无效的选项，请重新选择。")

def go_to_class():
    print("你去上了数学课。")
    time.sleep(1)
    print("今天的数学课很有趣！")
    time.sleep(1)

def join_club():
    print("你参加了学校的科学俱乐部活动。")
    time.sleep(1)
    print("你在活动中交到了新朋友。")
    time.sleep(1)

def do_homework():
    print("你回家做了数学作业。")
    time.sleep(1)
    print("作业完成了，你感到很有成就感！")
    time.sleep(1)

if __name__ == "__main__":
    start_game()
