class User:
    def __init__(self, account, password):
        self.account = account
        self.password = password
        self.post = None

    def set_post(self, post):
        self.post = post
