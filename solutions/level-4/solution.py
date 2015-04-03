#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Puzzle page:
    http://www.pythonchallenge.com/pc/def/linkedlist.php
Solution page:
    http://www.pythonchallenge.com/pcc/def/peak.html
"""

import re
from urllib2 import urlopen

BASE_URL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='


def request(url):
    return urlopen(url).read()


def answer(first):
    content = request(BASE_URL + first)
    for i in xrange(0, 401):
        print(content)
        m = re.search(r'([0-9]+)$', content)
        if m:
            next = m.groups()[0]
        else:
            cmd = raw_input('> ')
            if cmd == 'quit':
                break
            next = cmd
        content = request(BASE_URL + next)


if __name__ == '__main__':
    content = request('http://www.pythonchallenge.com/pc/def/linkedlist.php')
    m = re.search(r'nothing=([0-9]+)', content)
    first = m.groups()[0]
    result = answer(first)
    print(result)
