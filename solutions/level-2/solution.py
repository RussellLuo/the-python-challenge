#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Puzzle page:
    http://www.pythonchallenge.com/pc/def/ocr.html
Solution page:
    http://www.pythonchallenge.com/pcc/def/equality.html
"""

from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    """Counter that remembers the order elements are first encountered."""
    pass


def answer(text):
    counter = OrderedCounter(text)
    min_count = min(counter.values())
    rare_characters = [
        key for key, value in counter.iteritems()
        if value == min_count
    ]
    return ''.join(rare_characters)


if __name__ == '__main__':
    from urllib2 import urlopen
    content = urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read()
    text = content.split('<!--')[2].split('-->')[0]
    result = answer(text)
    print(result)
