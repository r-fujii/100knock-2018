#!/usr/bin/env python3
# 以下をスクリプトに落とし込む

import sys

def ask_nlines():
    while True:
        try:
            N = int(input('表示したい行数Nを入力: '))
            break
        except ValueError:
            continue
    return N

if __name__ == '__main__':
    # モジュールとしての実行でない場合
    if len(sys.argv) > 1:
        try:
            N = int(sys.argv[1])
        except ValueError:
            N = ask_nlines()
    else: N = ask_nlines()

else: N = ask_nlines()
    
with open('./data/popular-names.txt') as data:
    for i, line in enumerate(data, start = 1):
        if i <= N:
            print(line.rstrip())
        else : pass