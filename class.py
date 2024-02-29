import hashlib


class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = self.hash_password(password)

    def display(self):
        print('회원 이름:', self.name)
        print('회원 아이디:', self.username)
        # 해시화된 암호를 '*'로 변환
        print('비밀번호: ', '*' * len(self.password))

    # hashlib모듈을 이용한 'password'의 암호화
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


# 회원 정보와 게시물 정보를 담을 리스트
members = []
posts = []

# 회원 정보 입력
for _ in range(3):
    name = input('회원 이름을 입력하세요: ')
    username = input('회원 아이디를 입력하세요: ')
    password = input('비밀번호를 입력하세요: ')
    print()

    member = Member(name, username, password)
    members.append(member)

# 회원 정보 출력
print('\n회원 정보:')
for member in members:
    member.display()
    print()

# 게시물 입력
for _ in range(9):
    title = input('게시물 제목을 입력하세요: ')
    content = input('게시물 내용을 입력하세요: ')
    author = input('작성자 아이디를 입력하세요: ')
    print()

    post = Post(title, content, author)
    posts.append(post)

# 특정 유저가 작성한 게시글의 'title' 출력
print('\n특정 유저가 작성한 게시글 제목:')
specific_user = input('게시글을 검색할 유저 아이디를 입력하세요: ')
for post in posts:
    if post.author == specific_user:
        print(post.title)

# 특정 단어가 'content'에 포함된 게시글 제목 출력
print('\n특정 단어가 포함된 게시글 제목:')
specific_word = input('검색할 단어를 입력하세요: ')
for post in posts:
    if specific_word in post.content:
        print(post.title)
