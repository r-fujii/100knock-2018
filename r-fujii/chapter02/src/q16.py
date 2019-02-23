#!/usr/bin/env python3

import sys

def ask_ndiv():
    while True:
        try:
            N = int(input('分割したいファイル数を入力: '))
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
            N = ask_ndiv()
    else: N = ask_ndiv()

else: N = ask_ndiv()

def count_lines(seq):
    for n, _ in enumerate(seq, start = 1):
        pass
    return n
    
with open('./data/popular-names.txt') as data:
    n = count_lines(data)
    data.seek(0)
    q, mod = divmod(n, N)
    
    fpath = './work/popular-names_{0}.txt'
    for i in range(N):
        with open(fpath.format(i), 'w') as out:
            for j, line in enumerate(data, start = 1):
                out.write(line)
                if j > q:
                    break
                elif j == q:
                    if mod <= i:
                        break