#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Puzzle page:
    http://www.pythonchallenge.com/pc/def/map.html
Solution page:
    http://www.pythonchallenge.com/pcc/def/ocr.html
"""

import string


def answer(text):
    table = string.maketrans('abcdefghijklmnopqrstuvwxyz',
                             'cdefghijklmnopqrstuvwxyzab')
    return text.translate(table)


if __name__ == '__main__':
    import sys
    text = sys.stdin.read()
    result = answer(text)
    print(result)
