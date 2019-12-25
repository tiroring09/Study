""" 한 파일에서 사용된 모든 단어를 알파벳순으로 출력하며, 각 단어가 등장한 횟수도 함께 출력한다. split과 strip메서드 사용 """

import string
import sys

def count_unique_word():
    wordsDict = {}

    # 모든 띄어쓰기종류 + 모든 특수문자 + 0~9까지 숫자 + 따옴표
    stripLib = string.whitespace + string.punctuation + string.digits + "\"'"

    for filename in sys.argv[1:]:   # 인자로 주어지는 모든 파일들을 순회
        with open(filename) as file:    # 파일을 연다.
            for line in file:           # 파일의 각 줄에 대해
                for eachWord in line.lower().split():   # 공백기준으로 쪼개고 소문자변환한 각 단어 대상으로
                    eachWord = eachWord.strip(stripLib) # 특수문자들을 제거한다.
                    if (len(eachWord) > 2): # 왜 3개부터지?
                        wordsDict[eachWord] = wordsDict.get(eachWord, 0) + 1    # 딕션에 추가하고 카운트

    for eachWord in sorted(wordsDict):
        print("{0}: {1}번".format(eachWord, wordsDict[eachWord]))

if __name__ == "__main__":
    count_unique_word()
