""" 재귀적 호출을 통해 10진수 number를 base진법으로 변환한다. """

def convert_dec_to_any_base_rec(number, base):
    convertString = "0123456789ABCDEF"
    # convertList = [0, 1, 2, 3 , 4, 5, 6, 7, 8, 9, A, B, C, D, E, F]
        if number < base:
        return convertString[number]
    else:
        return convert_dec_to_any_base_rec(number // base, base) \+ convertString[number % base]

def test_convert_to_any_base_rec():
    number, base = 9, 2
    assert(convert_dec_to_any_base_rec(number, base) == "1001")
    print("pass the test")

if __name__ = "__main__":
    test_convert_to_any_base_rec()
