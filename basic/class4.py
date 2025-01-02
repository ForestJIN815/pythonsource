class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init__ 호출")

    def test(self):
        print("Parent 클래스의 test 호출")

    def func1(self):
        print("Parent func1() 입니다.")


class Child(Parent):
    def __init__(self):
        Parent.__init__(self)  # super() 역할
        print("Child 클래스의 __init__ 호출")

    def func1(self):
        print("Child func1() 입니다.")


child = Child()
child.test()
child.func1()

print(child.value)
