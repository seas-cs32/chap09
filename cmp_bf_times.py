### chap09/cmp_bf_times.py
'''
Compares the running times of our brute-force string-matching
implementations.

Example usage: python3 cmp_bf_times.py JustDavid.txt "has left"
'''

import sys
import time
from bf_strmatch import bf_strmatch
from bf_strmatch2 import bf_strmatch2

def main():
    # Check for proper usage and grab the input strings
    if len(sys.argv) == 1:
        fname = input('Filename containing text: ')
        p = input('Pattern: ')
    elif len(sys.argv) == 3:
        fname = sys.argv[1]
        p = sys.argv[2]
    else:
        sys.exit("Usage: python3 cmp_bf_times.py filename pattern")

    # Grab the contents of a file as our large text string
    with open(fname) as f:
        t = f.read()

    print('\n*** TEST with `bf_strmatch` ***')
    start = time.process_time()
    bf_strmatch(t, p)
    print(f'bf_strmatch took {time.process_time() - start} secs')

    print('\n*** TEST with `bf_strmatch2` ***')
    start = time.process_time()
    bf_strmatch2(t, p)
    print(f'bf_strmatch2 took {time.process_time() - start} secs')

if __name__ == '__main__':
    main()
