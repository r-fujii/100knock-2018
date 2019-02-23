#!/usr/bin/env python3

import sys

def ask_nlines():
    while True:
        try:
            N = int(input('表示したい行数Nを入力: '))
            break
        except ValueError:
            continue
    return N

def count_lines(seq):
    for n, _ in enumerate(seq, start = 1):
        pass
    return n

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
    n = count_lines(data)
    data.seek(0)
    # 行数のカウントをしてseekでファイルの先頭に戻る
    
    for i, line in enumerate(data, start = 1):
        if n - 5 < i:
            print(line.rstrip())