""" using generator(sequence in java) to get fibonacci sequence """
# 신기한 사용법이네

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

if __name__ == "__main__":
    target_number = 10
    fg = fibonacci_generator()
    for i in range(target_number):
        print(next(fg), end = " ")
