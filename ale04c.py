### chap09/ale04c.py

import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sps

def mylog(n, k, legend):
    legend.append(r'$O(\log n)$')
    return k*np.log(n)

def lin(n, k, legend):
    legend.append('O(n)')
    return k*n

def nlog(n, k, legend):
    legend.append(r'$O(n \log n)$')
    return k*n*np.log(n)

def quad(n, k, legend):
    legend.append('$O(n^2)$')
    return k*n**2

def cub(n, k, legend):
    legend.append('$O(n^3)$')
    return k*n**3

def exp(n, k, legend):
    legend.append('$O(2^n)$')
    return k*2**n

def fac(n, k, legend):
    legend.append('O(n!)')
    return k*sps.factorial(n)

n = np.arange(1, 7)

# To make the graphs readable, the first plot contains the slow-growing
# functions and the second the fast-growing ones.  We plot linear growth
# in both as a baseline.

legend = []
plt.xlabel('Size of input (n)', fontsize=12)
plt.ylabel('Number of operations', fontsize=12)

plt.plot(n, quad(n, 1, legend), linestyle='-.', linewidth=2, color='blue', marker='o', markersize=5)
plt.plot(n, nlog(n, 1, legend), linestyle='--', linewidth=2, color='green', marker='*', markersize=5)
plt.plot(n, mylog(n, 1, legend), linestyle=':', linewidth=2, color='black', marker='d', markersize=5)
plt.plot(n, lin(n, 1, legend), linestyle='-', linewidth=2, color='red', marker='s', markersize=5)

plt.legend(legend, loc='upper left', fontsize=15);

output_fname = 'ale04-slowgrowth.png'
plt.savefig(output_fname)
print(f'Wrote plots to {output_fname}')

plt.clf()

legend = []
plt.xlabel('Size of input (n)', fontsize=12)
plt.ylabel('Number of operations', fontsize=12)

plt.plot(n, fac(n, 1, legend), linestyle='-.', linewidth=2, color='blue', marker='o', markersize=5)
plt.plot(n, exp(n, 1, legend), linestyle='--', linewidth=2, color='green', marker='*', markersize=5)
plt.plot(n, cub(n, 1, legend), linestyle=':', linewidth=2, color='black', marker='d', markersize=5)
plt.plot(n, lin(n, 1, legend), linestyle='-', linewidth=2, color='red', marker='s', markersize=5)

plt.legend(legend, loc='upper left', fontsize=15);

output_fname = 'ale04-fastgrowth.png'
plt.savefig(output_fname)
print(f'Wrote plots to {output_fname}')
