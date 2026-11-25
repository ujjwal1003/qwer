import numpy as np
import matplotlib.pyplot as plt

a = 1.0
V0 = 10.0
L = 5.0
N = 201

x = np.linspace(-L, L, N)
dx = x[1] - x[0]

V = np.zeros(N)
V[np.abs(x) < a] = -V0

H = np.zeros((N-2, N-2))

for i in range(N-2):
    H[i, i] = 2/dx**2 + V[i+1]
    if i > 0:
        H[i, i-1] = -1/dx**2
    if i < N-3:
        H[i, i+1] = -1/dx**2

E, psi = np.linalg.eigh(H)
bound = np.where((E > -V0) & (E < 0))[0]

print("Bound-state energies:")
print(E[bound])

plt.plot(x, V, 'k', label="Potential")

for j in bound[:3]:
    y = np.zeros(N)
    y[1:-1] = psi[:, j]
    y /= np.sqrt(np.sum(y**2)*dx)
    plt.plot(x, E[j] + y, label=f"E={E[j]:.3f}")

plt.xlabel("Position x")
plt.ylabel("Energy / Wavefunction")
plt.title("Finite Difference Method")
plt.legend()
plt.grid()
plt.show()