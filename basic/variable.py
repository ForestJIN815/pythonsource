# 한줄 주석
"""
여러줄 주석 작성
사용
"""

# 변수
str1 = "life is too short, You need Python"
str2 = "123"
num1 = 10
num2 = 10.5

# bool : True, False 표현(자바스크립트, 자바랑 다름)
flag = True

# tpye(변수) : 변수는 어떤 타입인가?
print(str1, type(str1))  # <class 'str'>
print(str1, type(str2))
print(num1, type(num1))  # <class 'int'>
print(num2, type(num2))  # <class 'float'>
print(flag, type(flag))  # <class 'bool'>


# 두 개의 변수에 같은 값 대입
a = b = 3
print("a, b", a, b)

a, b = 10, 15
print(a, b)

# a, b 값 서로 교환
a, b = b, a
print("교환 후", a, b)

# "123" + 100 (자바, 자바스크립트 에서는 연결처리 : 123100)
# str2 = str2 + 100  # TypeError: can only concatenate str (not "int") to str

# int() : int 타입 변환
str2 = int(str2) + 100
print(str2)

print("bool => int 변환", int(flag))
print("int(98.6)", int(98.6))

# float() : float 형 변환
print("float(98.6)", float("98.6"))
print("float(flag)", float(flag))

# str() : str 형 변환
print("str(98.6) ", str("98.6"))

# bool() : bool 형 변환
print("bool(98.6) ", bool("98.6"))

# 문자열 자료형
# "", '', """""", ''''''
str3 = "Python's favorite food is perl"
print(str3)

str3 = '"Python favorite food is perl"'
str3 = '"Python\'s favorite food is perl"'
print(str3)

multiline = """
    Life is too short
    You need Python
"""
print(multiline)
