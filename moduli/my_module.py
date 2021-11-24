import time


def my_sum(x, y):
    return x+y


def my_hello():
    print("Hello, world!")


if __name__ == "__main__":
    print(time.localtime())
    print(my_sum(2, 5))
    time.sleep(5)
    my_hello()
