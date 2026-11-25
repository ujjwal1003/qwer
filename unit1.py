import numpy as np
import matplotlib.pyplot as plt

N = 200
theta = np.linspace(0.001, np.pi-0.001, N)
h = theta[1] - theta[0]

H = np.zeros((N, N))

for i in range(N):
    H[i, i] = 2/h**2
    if i > 0:
        H[i, i-1] = -1/h**2
    if i < N-1:
        H[i, i+1] = -1/h**2

m = 0
for i in range(N):
    H[i, i] += m**2 / np.sin(theta[i])**2

E, psi = np.linalg.eigh(H)

plt.plot(theta, psi[:, 0]**2, label="l=0")
plt.plot(theta, psi[:, 1]**2, label="l=1")
plt.plot(theta, psi[:, 2]**2, label="l=2")

plt.xlabel("Theta (radians)")
plt.ylabel("Probability density")
plt.title("Angular Eigenfunctions: Finite Difference")
plt.legend()
plt.grid()
plt.show()