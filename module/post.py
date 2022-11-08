from module.user import User
from table2ascii import table2ascii, Alignment, PresetStyle


class Post:
    def __init__(self, content, author) -> None:
        self.content = content
        self.author = author

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
    body.append([idx, post.content, post.author])
    while post.next is not None:
        post = post.next
        idx += 1
        body.append([idx, post.content, post.author])

    output = table2ascii(
        header=["id", "Post", "Author"],
        body=body,
        alignments=[Alignment.LEFT, Alignment.LEFT, Alignment.CENTER],
        style=PresetStyle.ascii_compact,
    )

    print(output)


def delete_post(post: Post):
    # 刪除文章
    if post.head is not None:
        post.head.next = post.next
    if post.next is not None:
        post.next.head = post.head


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
