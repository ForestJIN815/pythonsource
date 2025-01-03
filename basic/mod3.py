PI = 3.141592


class Math:
    def solv(self, r):
        return PI * (r**2)


def add(a, b):
    return a + b


if __name__ == "__main__":
    print(PI)
    math = Math()
    print(add(5, 8))
    print(math.solv(5))
