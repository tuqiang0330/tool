#!/usr/bin/python
#-*- encoding: utf-8 -*-
# 表格生成工具
# 默认使用Tab分割字段
# 如果列数不相同，左对齐

import sys
import argparse

def main():
    # 判断参数
    parser = argparse.ArgumentParser('make a table')
    parser.add_argument('-d', '--delimiter', default='\t', help='delimiter of columns, default is Tab')
    args = parser.parse_args()

    # 准备变量
    row_list = []           # 缓存所有的输入行，消耗内存
    column_length_list = [] # 每列的长度
    column_count = 0        # 列数

    # 读取输入
    for line in sys.stdin:
        column_list = line.strip().split(args.delimiter)
        row_list.append(column_list)
        # 更新列数
        if len(column_list) > column_count:
            column_count = len(column_list)
        # 更新没列长度
        while len(column_length_list) < column_count:
            column_length_list.append(0)
        for i in range(0, min(column_list, column_count)):
            if len(column_list[i]) > column_length_list[i]:
                column_length_list[i] = len(column_list[i])

    # 行分割符
    line_seperator = ''
    for i in column_length_list:
        line_seperator += '+'
        for j in range(0, i+2):
            line_seperator += '-'
    line_seperator += '+\n'

    # 输入表格
    for row in row_list:
        sys.stdout.write(line_seperator)
        for i in range(0, len(row)):
            sys.stdout.write('| %s' % row[i])
            for j in range(0, column_length_list[i] - len(row[i]) + 1):
                sys.stdout.write(' ')
        if len(row) < column_count:
            for i in range(len(row), column_count):
                sys.stdout.write('|')
                for j in range(0, column_length_list[i]+2):
                    sys.stdout.write(' ')
        sys.stdout.write('|\n')
    sys.stdout.write(line_seperator)


if __name__ == '__main__':
    main()
