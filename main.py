from module.register import register
from module.login import login
from module.post import create_post, show_all_post, delete_post, good_post
from module.user import fetch_user, show_friends
import module.storage as storage
from table2ascii import table2ascii, Alignment, PresetStyle

global is_login, current_user
is_login = False


def page_without_login():
    output = table2ascii(
        header=["Option", "Description"],
        body=[
            ["1", "Register"],
            ["2", "Login"],
            ["3", "Exit"],
        ],
        alignments=[Alignment.CENTER, Alignment.LEFT],
        style=PresetStyle.ascii_compact,
    )
    print("歡迎使用 TinyFB 社群網站")
    print(output)
    print("請輸入選項: ", end="")
    option = input()

    if option == "1":
        user = register(storage=storage)
        print("註冊成功，請使用以下資訊登入")
        print("帳號: %s" % user.account)
        print("密碼: %s" % user.password)
    elif option == "2":
        print("登入")
        user = login(storage=storage)
        print(user)
        if user is not None:
            global is_login
            is_login = True
            global current_user
            current_user = user
    elif option == "3":
        print("離開")
        exit(0)
    elif option == "4":
        # Show all data in storage
        print(storage.__str__())
    else:
        print("輸入錯誤")


def page_with_login():
    print("您好，%s" % current_user.account)
    output = table2ascii(
        header=["Option", "Description"],
        body=[
            ["1", "Post"],
            ["2", "Show All Post"],
            ["3", "Delete Post"],
            ["4", "Add Friend"],
            ["5", "Show All Friend"],
            ["6", "Show Friend Post"],
            ["7", "Good Post"],
            ["8", "Logout"],
        ],
        alignments=[Alignment.CENTER, Alignment.LEFT],
        style=PresetStyle.ascii_compact,
    )
    print(output)
    print("請輸入選項: ", end="")

    option = input()

    if option == "1":
        print("發文")
        content = input("請輸入內容: ")
        create_post(current_user, content)
    elif option == "2":
        print("顯示所有文章")
        if current_user.post is None:
            print("沒有文章")
        else:
            show_all_post(current_user.post)
    elif option == "3":
        print("刪除文章")
        index = int(input("請輸入文章編號: "))
        delete_post(index, current_user)
    elif option == "4":
        print("加好友")
        account = input("請輸入好友帳號: ")
        friend = fetch_user(account, storage)
        if friend is None:
            print("找不到好友")
        else:
            current_user.add_friend(friend)
            print("加好友成功")
    elif option == "5":
        print("顯示所有好友")
        show_friends(current_user)
    elif option == "6":
        print("顯示好友文章")
        for friend in current_user.friends:
            show_all_post(friend.post)
    elif option == "7":
        print("讚")
        account = input("請輸入好友帳號: ")
        friend = fetch_user(account, storage)
        if friend is None:
            print("找不到好友")
        else:
            show_all_post(friend.post)
            index = int(input("請輸入文章編號: "))
            good_post(index=index, author=friend, user=current_user)

    elif option == "8":
        print("登出")
        global is_login
        is_login = False


def main():

    while True:
        if is_login:
            page_with_login()
        else:
            page_without_login()


if __name__ == "__main__":
    main()
