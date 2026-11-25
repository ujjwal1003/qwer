import numpy as np
import matplotlib.pyplot as plt

e = 3.795
hbar = 1973
m = 0.511e6

h = hbar**2/(2*m)

N = 500
r = np.linspace(0.01, 40, N)
dr = r[1]-r[0]

for a in [3, 5, 7]:

    V = -e**2/r * np.exp(-r/a)

    H = np.diag(2*h/dr**2 + V)
    H += np.diag(-h/dr**2*np.ones(N-1), 1)
    H += np.diag(-h/dr**2*np.ones(N-1), -1)

    E, psi = np.linalg.eigh(H)

    print("Screening length =", a, "Angstrom")
    print("Ground state energy =", round(E[0], 3), "eV")

    u = psi[:, 0]
    u = u/np.sqrt(np.trapezoid(u**2, r))

    plt.plot(r, u, label="a = "+str(a))

plt.xlabel("r (Angstrom)")
plt.ylabel("u(r)")
plt.title("Screened Coulomb Potential")
plt.legend()
plt.grid()
plt.show()