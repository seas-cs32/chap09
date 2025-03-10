### chap09/ale04d.py

import matplotlib.pyplot as plt
import numpy as np

def nlog(n, k):
    return k*n*np.log(n)

def quad(n, k):
    return k*n*n

# Setting the range of n
n = np.arange(1, 27001, 1000)
#n = np.arange(???, ???, 50)

legend = []

plt.plot(n, 9000*n+15000000, linestyle='-.', color='blue', marker='s', markersize=5)
legend.append(r'$f(n) = 9000n + 15,000,000 = O(n)$')

plt.plot(n, nlog(n, 1000), linestyle='--', color='red', marker='d', markersize=5)
legend.append(r'$g(n) = 1000n\log n = O(n \log n)$')

plt.plot(n, quad(n, 0.5), linestyle='-', color='green', marker='o', markersize=5)
legend.append(r'$h(n) = 0.5n^2 = O(n^2)$')

plt.xlabel('Size of input (n)', fontsize=12)
plt.ylabel('Number of operations', fontsize=12)
plt.legend(legend, loc='best', fontsize=12);

output_fname = 'ale04-consts.png'
plt.savefig(output_fname)
print(f'Wrote plots to {output_fname}')
