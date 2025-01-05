def add(a, b):
    return a + b


def sub(a, b):
    return a - b


# 확인용 코드
# __name__ : 파이썬이 내부적으로 사용하는 변수명
#            mod1 을 직접 실행 시 이름은 __main__ 이 저장됨
#            외부에서 mod1 실행 시 __name__ 에는 mod1 으로 저장됨
if __name__ == "__main__":
    print(add(1, 4))
    print(sub(9, 4))
