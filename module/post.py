from module.user import User
from table2ascii import table2ascii, Alignment, PresetStyle


class Post:
    def __init__(self, content, author) -> None:
        self.content = content
        self.author = author
        self.good_list = []

        self.head = None
        self.next = None

    def __str__(self) -> str:
        return f"{self.author}:\n{self.content}"

    def set_link(self, head, next):
        self.head = head
        self.next = next


def show_all_post(post: Post):
    body = []
    # 顯示文章
    idx = 1
    body.append([idx, post.content, post.author, "\n".join(post.good_list)])
    while post.next is not None:
        post = post.next
        idx += 1
        body.append([idx, post.content, post.author,
                    "\n".join(post.good_list)])

    output = table2ascii(
        header=["id", "Post", "Author", "Good_List"],
        body=body,
        alignments=[Alignment.LEFT, Alignment.LEFT,
                    Alignment.CENTER, Alignment.LEFT],
        style=PresetStyle.ascii_compact,
    )

    print(output)


def delete_post(index: int, user: User):
    # 刪除文章
    post = user.post

    if post is None:
        print("沒有文章")
        return

    if index == 1:
        user.post = post.next
        if post.next is not None:
            post.next.head = None
        return

    idx = 1
    while post.next is not None:
        post = post.next
        idx += 1
        if idx == index:
            post.head.next = post.next
            if post.next is not None:
                post.next.head = post.head
            return

    print("沒有這篇文章")


def create_post(user: User, content: str = "") -> Post:
    # 建立文章
    new_post = Post(content, user.account)

    if user.post is None:
        user.post = new_post
    else:
        post = user.post
        while post.next is not None:
            post = post.next

        post.next = new_post
        new_post.head = post

    return new_post


def good_post(index: int, user: User, author: User):
    # 讚
    post = author.post

    if post is None:
        print("沒有文章")
        return

    idx = 1
    while post.next is not None:
        post = post.next
        idx += 1
        if idx == index:
            if user.account in post.good_list:
                print("已經讚過了")
            else:
                post.good_list.append(user.account)
                print("讚成功")
            return
