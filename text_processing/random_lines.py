#!/usr/bin/python
# -*- coding: utf-8 -*- 

##
# @file RandomNLine.py
# @brief Because of storing N lines in list, it is space-comsuming if N is too large.
# @author tuqiang
# @version 
# @date 2013-01-25

import argparse
import sys
import random

def main():
    parser = argparse.ArgumentParser('output random lines of files')
    parser.add_argument('n', type=int, help='delimiter of columns, default is Tab')
    args = parser.parse_args()

    result = []
    line_num = 0

    for line in sys.stdin:
        if line_num < args.n:
            result.append(line)
        else:
            index = random.randint(0, line_num)
            if index < args.n:
                result[index] = line
        line_num += 1

    for line in result:
        sys.stdout.write(line)


if __name__ == '__main__':
    main()
