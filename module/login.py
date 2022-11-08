from typing import Optional
from module.user import User


def login(storage=None) -> Optional[User]:
    # 會員登入
    if storage is None:
        print("未使用資料庫，無法登入")
        return None

    print("請輸入帳號: ", end="")
    account = input()
    print("請輸入密碼: ", end="")
    password = input()

    # 從 storage 取得 User 物件
    user = storage.get(f'account_data:{account}')

    # 檢查密碼是否正確
    if user is not None and user.password == password:
        print("登入成功")
        return user
    else:
        print("登入失敗")
        return None
