# 연산
# 1. 산술연산자(+, -, *, /, //, **, %)
# / : 나머지도 나누기(자바스크립트랑 같은 개념)
# // : 몫만 (자바 / 같은 개념)

a, b = 5, 3
print(a + b, a - b, a * b, a / b, a // b, a**b, a % b)
# a**b(a를 b번 제곱), a % b(a를 b로 나눈 나머지)

# 문자열 연결 : +
s1, s2, s3 = "100", "100.123", "1234567"
print(s1 + s2 + s3)

# 문자열 + 정수 : 파이썬에서는 오류 발생
print(s1 + str(1))

# 복합대입 연산자
a = 10
a += 5  # a = a + 5
print(a)
a -= 5
print(a)
a /= 5  # 실수 나누기
print(a)
a //= 5  # 정수 나누기
print(a)
a %= 5
print(a)


# [실습] 7,777원을 가지고 있다. 동전으로 교환하기
# 500 : 15개, 100원 : 2개, 50원 : 1개, 10원 : 2개, 나머지 돈 : 7원
money = 7777
c500, c100, c50, c10 = 0, 0, 0, 0

c500 = money // 500
money %= 500

c100 = money // 100
money %= 100

c50 = money // 50
money %= 50

c10 = money // 10
money %= 10

print("500원 : %d 개" % c500)
print("100원 : %d 개" % c100)
print("50원 : %d 개" % c50)
print("10원 : %d 개" % c10)
print("나머지 돈 : %d 원" % money)

# 관계(비교) 연산자 : 결과가 True, False
a, b = 10, 0
print("a == b", (a == b))
print("a != b", (a != b))
print("a >= b", (a >= b))
print("a <= b", (a <= b))

# 논리 연산자 : and, or, not
# and : &&, or : ||, not : ! (자바, 자바스크립트)
a, b, c = 100, 60, 15
print("a > b and b > c", a > b and b > c)
print("a > b or b > c", a > b or b > c)
print("not False ", not False)
print("not b < c ", not b < c)
