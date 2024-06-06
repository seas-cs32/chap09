### chap09/ale01.py

# Example of bitwise OR on a sequence of bits
i = 0b1100
j = 0b1010
print(f'i     = {bin(i)}')
print(f'j     = {bin(j)}')
print( '--------------')
print(f'i | j = {bin(i | j)}')
print()

# Example of bitwise EXCLUSIVE-OR on a sequence of bits
i = 0b1100
j = 0b1010
print(f'i     = {bin(i)}')
print(f'j     = {bin(j)}')
print( '--------------')
print(f'i ^ j = 0b{(i ^ j):04b}')
print()

# The two components of an add for each digit column
i = 0b1100
j = 0b1010
print(f'i     = {bin(i)}')
print(f'j     = {bin(j)}')
print( '--------------')
print(f'sum   = 0b{(i ^ j):04b}')
print(f'carry = 0b{(i & j):04b}')
print()

# Perform addition without using the `+` operator
def add(a, b):
    # adds two 8-bit numbers
    assert a >= 0 and a < 256
    assert b >= 0 and b < 256

    # turn input integers into binary strings with leading 0s
    a = f'{a:08b}'
    b = f'{b:08b}'

    # setup for the addition
    c = ''        # the answer, eventually
    carry_in = 0  # the initial carry in

    # add without the `+` operator, which starts at the rightmost bit!
    for i in range(7, -1, -1):
        # get the integer value of the next bits to add
        a_i = int(a[i])
        b_i = int(b[i])

        # do the sum and carry logic
        sum = carry_in ^ a_i ^ b_i
        carry = (carry_in & a_i) | (carry_in & b_i) | (a_i & b_i)

        # concatenate this sum to our growing answer
        c = str(sum) + c    # string concatentation!

        # setup for next bit location
        carry_in = carry

    return int(c, base=2)

# Test the `add` function
a = 3
b = 6
c = add(a, b)
print(f'{a} + {b} = {c}')
assert c == a + b, "`add` failed"

a = 38
b = 69
c = add(a, b)
print(f'{a} + {b} = {c}')
assert c == a + b, "`add` failed"
