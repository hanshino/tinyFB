from table2ascii import table2ascii, Alignment, PresetStyle


class User:
    def __init__(self, account, password):
        self.account = account
        self.password = password
        self.post = None
        self.friends = []

    def set_post(self, post):
        self.post = post

    def add_friend(self, friend):
        self.friends.append(friend)


def fetch_user(account, storage):
    user = storage.get(f'account_data:{account}')
    if user is not None:
        return user
    else:
        return None


def show_friends(user: User):
    # 顯示好友
    if len(user.friends) == 0:
        print("沒有好友")
        return

    body = []
    for friend in user.friends:
        body.append([friend.account])

    output = table2ascii(
        header=["Account"],
        body=body,
        alignments=[Alignment.LEFT],
        style=PresetStyle.ascii_compact,
    )

    print(output)
