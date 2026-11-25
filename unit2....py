# Finite square well potential

import numpy as np
import matplotlib.pyplot as plt

N = 300
L = 5
a = 1
V0 = 20

x = np.linspace(-L, L, N)
dx = x[1] - x[0]

V = np.zeros(N)
V[np.abs(x) < a] = -V0

H = np.diag(1/dx**2 + V[1:-1])
H += np.diag(-0.5/dx**2*np.ones(N-3), 1)
H += np.diag(-0.5/dx**2*np.ones(N-3), -1)

E, psi = np.linalg.eigh(H)

plt.plot(x, V, 'k', label='Potential')

for i in range(4):
    if E[i] < 0:
        wave = np.zeros(N)
        wave[1:-1] = psi[:, i]
        plt.plot(x, E[i] + 2*wave/np.max(np.abs(wave)),
                 label='State '+str(i))

plt.xlabel('Position')
plt.ylabel('Energy')
plt.title('Finite Well')
plt.legend()
plt.grid()
plt.show()

print("Energy eigenvalues:")
print(E[E < 0])