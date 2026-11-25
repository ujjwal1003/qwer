import numpy as np
import matplotlib.pyplot as plt

a = 1.0
N = 200
dx = 2*a/(N+1)
x = np.linspace(-a+dx, a-dx, N)

H = np.diag(np.full(N, 2/dx**2))
H += np.diag(np.full(N-1, -1/dx**2), 1)
H += np.diag(np.full(N-1, -1/dx**2), -1)

E, psi = np.linalg.eigh(H)

print("n   Analytical   Numerical")
for n in range(1, 4):
    exact = n**2*np.pi**2/(4*a**2)
    print(n, round(exact, 5), round(E[n-1], 5))

for n in range(3):
    y = psi[:, n]
    y = y / np.sqrt(np.sum(y**2)*dx)
    plt.plot(x, y, label=f"n={n+1}")

plt.xlabel("Position x")
plt.ylabel("Wavefunction")
plt.title("Particle in a Box: Finite Difference")
plt.legend()
plt.grid()
plt.show()