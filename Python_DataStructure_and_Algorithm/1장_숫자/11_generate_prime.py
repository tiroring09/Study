""" random모듈을 사용하여 n비트 내의 임의의 소수를 생성하는 함수 """
import math
import random
import sys

def finding_prime_sqrt(number):
    num = abs(number)
    if num == 1:
        return False
    for divider in range(2, int(math.sqrt(num)) + 1):
        if number % divider == 0:
            return False
    return True

def generate_prime(number = 3):
    while 1:    # 무한반복
        p = random.randint(pow(2, number - 2), pow(2, number - 1) - 1) # 이진수로 number에 상응하는 자릿수만큼 뽑기 위함
        p = 2 * p + 1   # 17줄과 18줄은 한번 다시 생각해봐야 할 듯
        if finding_prime_sqrt(p):   # 소수면 출력, 소수아니면 다시
            return p

if __name__ == "__main__":
    if len(sys.argv) < 2:   # 실행시에 사용자 입력받은 채로 실행하는 방법!
        print("Usage: generate_prime.py $number")
        sys.exit()
    else:
        number = int(sys.argv[1])
        print(generate_prime(number))

"""
sys.argv에 대하여
https://www.pythonforbeginners.com/system/python-sys-argv
sys.argv[0] == 파일명.py
실행할 때 `python3 $파일명.py $인자` 형식으로 실행하면 된다.
len(sys.argv)는 최소 1개이상이다.
`str(sys.argv)` 입력해보면 리스트 형식으로 인자가 들어있음을 알 수 있다.
"""
