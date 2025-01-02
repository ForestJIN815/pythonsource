# 클래스 정의
# self : 인스턴스 변수
# self 없이 사용 : 클래스 변수


class UserInfo:

    user_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        UserInfo.user_count += 1

    def user_info(self):
        return f"name : {self.name}, age : {self.age}"

    def __del__(self):
        UserInfo.user_count -= 1

    # 클래스 메소드 : static 메소드
    def function1():
        print("function1 호출")

    @classmethod
    def function2(cls):
        print("function2 호출")

    # toString() 역할
    def __str__(self):
        return f"name : {self.name}, age : {self.age}"


# 객체 생성
user1 = UserInfo("홍길동", 30)
print(user1.user_info())
# print(user1.user_count)
print(UserInfo.user_count)

user2 = UserInfo("성춘향", 30)
print(user2.user_info())

# static 변수와 같은 개념
print(user1.user_count)
print(user2.user_count)
print(UserInfo.user_count)

del user1
print("user1 삭제 ", UserInfo.user_count)

# __str__ 정의하지 않으면
print(user2)  # <__main__.UserInfo object at 0x0000019DD79E4A50>

# user2.function1()  # TypeError: UserInfo.function1() takes 0 positional arguments but 1 was given

UserInfo.function1()
UserInfo.function2()
