### chap09/cmp_bf_times.py
'''
Compares the running times of our brute-force string-matching
implementations.
'''

import time
from bf_strmatch import bf_strmatch
from bf_strmatch2 import bf_strmatch2

# Grab the contents of a file as our large text string
fname = 'JustDavid.txt'
with open(fname) as f:
    t = f.read()

# Set the pattern string
p = 'has left'

start = time.process_time()
bf_strmatch(t, p)
print(f'bf_strmatch took {time.process_time() - start} secs')

start = time.process_time()
bf_strmatch2(t, p)
print(f'bf_strmatch2 took {time.process_time() - start} secs')
