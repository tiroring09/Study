"""10진수로 주어진 자연수 number를 base진법으로 변환한다."""

def convert_from_decimal(number, base):
    multipler = 1
    result = 0
    while number > 0:
        result += number % base * multipler # number를 base로 나눈 나머지에 multipler를 곱함으로써 자리 수 마련한다.
        multipler *= 10 # 다음 자릿수로 이동
        number = number // base # 다음 자릿수로 이동
    return result

def test_convert_from_decimal():
    number, base = 9, 2
    assert(convert_from_decimal(number, base) == 1001)
    print("pass the test")

if __name__ == "__main__":
    test_convert_from_decimal()
