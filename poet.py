#! /usr/bin/env python

import itertools
import sys

def main(letters, length):
    with open('words', 'r') as wl:
        wordlist = [ word.rstrip().upper() for word in wl
                    if len(word.rstrip()) == length ]
    print('\n'.join(w
          for w in (''.join(combination).upper()
          for combination in itertools.permutations(letters, length))
          if w in wordlist))
    #for combination in itertools.permutations(letters, length):
    #    w = ''.join(combination).upper()
    #    if w in wordlist:
    #        print(w)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: {} <letters> <length>".format(sys.argv[0]))
        print("Example: {} WINTER 4".format(sys.argv[0]))
        exit(1)
    letters = sys.argv[1]
    length = int(sys.argv[2])
    main(letters, length)
