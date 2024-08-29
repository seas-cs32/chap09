### chap09/cmp_strmatch.py
'''
Compares the brute-force and Rabin-Karp string-matching
algorithms across a range of input text and pattern sizes.
'''
import sys
import time
from bf_strmatch import bf_strmatch
from rk_strmatch import rk_strmatch

def compare_times(t, p):
    print(f'For p = {len(p)} bytes, t = {len(t)} bytes')

    start = time.process_time()
    bf_strmatch(t, p)
    print(f'bf_strmatch took {time.process_time() - start} secs')

    start = time.process_time()
    rk_strmatch(t, p)
    print(f'rk_strmatch took {time.process_time() - start} secs')

    print('')

def run_experiment(p_orig, t_orig):
    '''Call this routine with a reasonable search pattern that
       won't ever match in the text.'''
    # As setup, create p_big through repetition to be about
    # a quarter the size of the text input.
    p_big = p_orig
    while len(p_big) < len(t_orig) // 4:
        p_big += p_big

    # Number of tests to run, where each test is twice
    # as big as the last.
    times_to_double = 7

    print('### Test: len(p) << len(t)')
    t = t_orig
    p = p_orig
    for i in range(times_to_double):
        compare_times(t, p)
        t += t
        p += p

    print('### Test: len(p) < len(t)')
    t = t_orig
    p = p_big
    for i in range(times_to_double):
        compare_times(t, p)
        t += t
        p += p

def main():
    # Check for proper usage and grab the input strings
    if len(sys.argv) != 1:
        sys.exit("Usage: python3 cmp_strmatch.py")

    # Currently hardwired to grab the text from JustDavid.txt
    with open('JustDavid.txt') as f:
        t_orig = f.read()

    # A reasonable search pattern that won't ever match
    p_orig = 'David laughed softty'

    run_experiment(p_orig, t_orig)

if __name__ == '__main__':
    main()
