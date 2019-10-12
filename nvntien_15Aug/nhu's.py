import os
import sys
file = sys.argv[-1]
key = sys.argv[-2]
case_sensitive = sys.argv[-3]


def find_line_3(case_sensitive, key, file):
    with open(file) as f:
        for num, line in enumerate(f, 1):
            if key in line:
                color_line = color_word_3(line, num, key)
                print(color_line, end='')
    f.close()


def find_line_2(key, file):
    key_lower = key.lower()
    len_key = len(key)
    with open(file) as f:
        for num, line in enumerate(f, 1):
            line_split = line.split()
            line_color = ''
            for word in line_split:
                if key_lower in word.lower():
                    pos = word.lower().find(key_lower)
                    word_color = word[pos:pos+len_key]
                    line_color = color_word_2(line, word_color)
                    line = line_color
            if line_color != '':
                line_color = '\033[1;33m{}\033[0m'.\
                  format(num) + ':' + line_color
                print(line_color, end='')
    f.close()


def color_word_2(line, match):
    match_color = '\033[30;43m{}\033[0m'.format(match)
    return line.replace(match, match_color)


def color_word_3(line, num, match):
    num_color = '\033[1;33m{}\033[0m'.format(num)
    match_color = '\033[30;43m{}\033[0m'.format(match)
    return num_color + ':' + line.replace(match, match_color)


def run():
    if case_sensitive == '--case-sensitive':
        find_line_3(case_sensitive, key, file)
    else:
        find_line_2(key, file)


run()
