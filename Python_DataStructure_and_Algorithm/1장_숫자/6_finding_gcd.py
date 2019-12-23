""" 두 정수의 최대공약수를 구한다. 두 수의 크기순서는 상관없다. """

def finding_gcd(alpha, beta):
    while (beta != 0): # b가 0이 되면 정지
        result = beta  # 최대공약수가 b라고 가정
        temp = beta
        beta = alpha % beta   # a를 b로 나눈 나머지를 새로운 b로 대입
        alpha = temp    # 원래 b를 새로운 a로 대입
        # alpha, beta = beta, alpha % beta
    return result

def test_finding_gcd():
    number1 = 21
    number2 = 12
    assert(finding_gcd(number1, number2) == 3)
    print("pass the test")

if __name__ == "__main__":
    test_finding_gcd()
