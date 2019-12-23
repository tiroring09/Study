""" 매개변수 number가 소수인지 여부를 알려준다. 소수란 1과 자기자신만을 약수로 가지는 수로써,(다른말로 약수가 2개뿐인 수) 1은 소수가 아니다. """
import math

def finding_prime(number):
    num = abs(number)
    if num == 1: return False
    for x in range(2, num): # 2부터 num전까지 모든 숫자로 나눔
        if num % x == 0:
            return False
    return True

def finding_prime_sqrt(number):
    num = abs(number)
    if num == 1: return False
    for x in range(2, int(math.sqrt(num)) + 1): # 2부터 number^1/2 까지의 숫자로 나누어도 충분하다. 에라토스테네스의 체 참고
        if num % x == 0:
            return False
    return True

def finding_prime_fermat(number):   # 페르마의 소정리
    if number <= 102:
        for a in range(2, number):
            if pow(a, number - 1, number) != 1: # sqrt는 루트, power는 거듭제곱, pow(a, b)는 a ^ b, pow(a, b, c)는 (a ^ b) % c
                return False
        return True
    else:
        for i in range(100):
            a = random.randint(2, number - 1)
            if pow(a, number - 1, number) != 1:
                return False
        return True

def test_finding_prime():
    testCase = [(17, True), (20, False), (2, True), (3, True), (4, False)]  # 1은 False여야 하지만, fermat함수에서는 True반환한다.
    for number in testCase:
        assert(finding_prime(number[0]) == number[1])
        assert(finding_prime_sqrt(number[0]) == number[1])
        assert(finding_prime_fermat(number[0]) == number[1])
    print("pass the test")

if __name__ == "__main__":
    test_finding_prime()

""" 에라토스테네스의 체를 파이썬 언어로 구현해본것 from wikipedia """
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 원소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 2부터 i=sqrt(n)까지 검사
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정(i + i부터 n까지 i간격)
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]
