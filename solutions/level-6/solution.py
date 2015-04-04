#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Puzzle page:
    http://www.pythonchallenge.com/pc/def/channel.html
Solution page:
    http://www.pythonchallenge.com/pcc/def/oxygen.html
"""

import re
from zipfile import ZipFile


def answer(zip_filename):
    txt_file = '%s.txt'
    zip = ZipFile(zip_filename, 'r')
    pattern = re.compile(r'(\d+)$')
    comments = []

    next = '90052'
    while True:
        next_filename = txt_file % next
        content = zip.read(next_filename)
        print(content)

        comment = zip.getinfo(next_filename).comment
        comments.append(comment)

        m = pattern.search(content)
        if m:
            next = m.group(1)
        else:
            break

    return ''.join(comments)


if __name__ == '__main__':
    import os
    from urllib2 import urlopen

    cur_path = os.path.dirname(__file__)
    zip_filename = os.path.join(cur_path, 'channel.zip')
    if not os.path.exists(zip_filename):
        content = urlopen('http://www.pythonchallenge.com/pc/def/channel.zip').read()
        with open(zip_filename, 'w') as zip:
            zip.write(content)

    result = answer(zip_filename)
    print(result)
