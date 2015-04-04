#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Puzzle page:
    http://www.pythonchallenge.com/pc/def/peak.html
Solution page:
    http://www.pythonchallenge.com/pcc/def/channel.html
"""

import pickle


def answer(content):
    data = pickle.loads(content)
    for line in data:
        print(''.join(c * n for c, n in line))


if __name__ == '__main__':
    from urllib2 import urlopen
    content = urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read()
    answer(content)
