""" 피보나치 수열에서 n번째 수 반환 """
import math

def find_fibonacci_seq_iter(n): # 반복
    if n < 2: return n # why not < 1?
    a = 0
    b = 1
    for i in range(n):
        temp = b
        b = a + b
        a = temp
        # a, b = b, a + b
    return a

def find_fibonacci_seq_rec(n):  # 재귀
    if n < 2: return n
    return find_fibonacci_seq_rec(n-1) + find_fibonacci_seq_rec(n-2)

def find_fibonacci_seq_form(n): # 피보나치 수열의 일반항 공식 응용
    sq5 = math.sqrt(5)
    phi = (1 + sq5) / 2
    return int(math.floor(phi ** n / sq5))

def test_fimd_fib():
    n = 10
    assert(find_fibonacci_seq_iter(n) == 55)
    assert(find_fibonacci_seq_rec(n) == 55)
    assert(find_fibonacci_seq_form(n) == 55)
    print("pass the test")

if __name__ == "__main__":
    test_fimd_fib()
