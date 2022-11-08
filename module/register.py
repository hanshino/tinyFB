from module.user import User


def register(storage=None) -> User:
    # 會員註冊
    print("請輸入帳號: ", end="")
    account = input()
    print("請輸入密碼: ", end="")
    password = input()

    # 建立一個新的 User 物件
    user = User(account, password)

    # 將 User 物件存入 storage
    if storage is not None:
        storage.put(f'account_data:{account}', user)

    return user
