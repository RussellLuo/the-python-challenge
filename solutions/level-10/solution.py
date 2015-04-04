#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Puzzle page:
    http://www.pythonchallenge.com/pc/return/bull.html
Solution page:
    http://www.pythonchallenge.com/pcc/return/5808.html

Tip:
    Challenge 10 shows a picture of a bull. In text below it says
`len(a[30]) = ?`. When the picture is clicked a new page shows this text
`a = [1, 11, 21, 1211, 111221, `. This is a known sequence called the
`Look and Say Sequence`. Basically the first is 1. You say "there is one 1"
and write it down as 11. Then the next would be saying "two ones", and
write it down as 21. Then one 2 one 1 = 1211, and so on and so on.
    Now the first text is asking for the 30th element in the sequence so
the program must be able to count the number of numbers in the sequence
and compute the next sequence, and continue until it reaches the 30th
iteration. Then as the text says, the length of that will be the name
of the next challenge.
"""


def look_and_say(prev):
    """Regex version."""
    import re
    next = ''.join(
        '%s%s' % (len(m.group(0)), m.group(1))
        for m in re.finditer(r'(\d)\1*', prev)
    )
    return next


def look_and_say_1(prev):
    """Groupby version."""
    from itertools import groupby
    next = ''.join(
        '%s%s' % (len(list(g)), k)
        for k, g in groupby(prev)
    )
    return next


def answer(index):
    next = '1'
    for i in xrange(0, index):
        next = look_and_say(next)
    return next


if __name__ == '__main__':
    while True:
        cmd = raw_input('> ')
        if cmd.isdigit():
            index = int(cmd)
            result = answer(index)
            print(result)
        elif cmd.startswith('len:'):
            index = int(cmd[4:])
            result = answer(index)
            print(len(result))
        elif cmd == 'quit':
            break
        else:
            print('''
[n]     -- show the n-th (0-based) element of the Look and Say Sequence.
len:[n] -- show the length of the n-th element.
quit    -- quit.
help    -- show this message.
            ''')
