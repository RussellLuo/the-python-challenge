#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Puzzle page:
    http://www.pythonchallenge.com/pc/def/equality.html
Solution page:
    http://www.pythonchallenge.com/pcc/def/linkedlist.php
"""

import re


def answer(text):
    pattern = r'(?:^|[^A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?:[^A-Z]|$)'
    matches = re.findall(pattern, text)
    return ''.join(matches)


if __name__ == '__main__':
    from urllib2 import urlopen
    content = urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read()
    text = content.split('<!--')[1].split('-->')[0]
    result = answer(text)
    print(result)
