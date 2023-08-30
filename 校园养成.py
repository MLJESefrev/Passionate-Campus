class Student:
    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.knowledge = 0
        self.social = 0

    def study(self):
        self.energy -= 20
        self.knowledge += 10
        print("您上了一节课，知识增加了，精力减少了。")

    def participate_activity(self):
        self.energy -= 30
        self.social += 15
        print("您参加了一个活动，社交增加了，精力减少了。")

    def rest(self):
        self.energy += 30
        print("您休息了一段时间，精力恢复了。")

def main():
    player_name = input("欢迎来到《校园生活模拟器》！请输入您的角色名：")
    player = Student(player_name)

    print(f"\n欢迎您，{player.name}！开始您的校园生活。")

    while True:
        print("\n1. 上课学习")
        print("2. 参加活动")
        print("3. 休息")
        print("4. 查看状态")
        print("5. 退出游戏")
        choice = input("请选择操作（输入数字）：")

        if choice == "1":
            player.study()

        elif choice == "2":
            player.participate_activity()

        elif choice == "3":
            player.rest()

        elif choice == "4":
            print(f"\n角色名：{player.name}")
            print(f"精力：{player.energy}")
            print(f"知识：{player.knowledge}")
            print(f"社交：{player.social}")

        elif choice == "5":
            print(f"感谢您的游玩，《校园生活模拟器》期待您的下次回来！")
            break

if __name__ == "__main__":
    main()
