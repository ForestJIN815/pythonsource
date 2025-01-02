# 클래스 정의
# self : 인스턴스 변수
# self 없이 사용 : 클래스 변수


class UserInfo:
    # 생성자 오버로딩 없음
    def __init__(self, name, age, email=None):
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        return f"name : {self.name}, age : {self.age}, email : {self.email}"


# 객체 생성
user1 = UserInfo("홍길동", 30, "hong123@gmail.com")
print(user1)

user2 = UserInfo("성춘향", 30)
print(user2)


class Car:
    # 생성자
    def __init__(self, color, speed=50, model="산타페"):
        self.color = color
        self.speed = speed
        self.model = model

    def up_speed(self, value):
        self.speed += value

    def down_speed(self, value):
        self.speed -= value

    def __str__(self):
        return f"color : {self.color}, speed : {self.speed}, model : {self.model}"


car1 = Car("Red")
print(car1)

car2 = Car("Black", speed=100)
print(car2)

car3 = Car("white", 200, "모닝")
print(car3)
