""" 자연수number와 base진법을 매개변수로 받아 10진수로 변환된 값을 반환한다. """

# 2 <= base <= 10
def convertToDecmal(number, base):
    multipler = 1
    result = 0
    while number > 0:
        result += number % 10 * multipler   # 끝의 한 자리를 떼어서 그 자리에 해당하는 값만큼 곱하여 더함
        multipler *= base   # 다음자리에 해당하는 값으로 변경
        number = number // 10
    return result

def test_convert_to_decimal():
    number, base = 1001, 2
    assert(convertToDecmal(number, base) == 9)
    print("pass the test")

if __name__ == "__main__":
    test_convert_to_decimal()
