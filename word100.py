# load words from stdin
# get words consist of only alphabet
# translate to number
# show ones add up to 100

import fileinput
import re

prog = re.compile('^[a-z]+$')

for line in fileinput.input():
    word = line.strip()
    if prog.match(word):
        if sum(map(lambda x: ord(x)-ord('a')+1, word)) == 100:
            print word

