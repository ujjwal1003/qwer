import numpy as np
import matplotlib.pyplot as plt

m = 940e6
hbar = 1973

D = 0.755501
alpha = 1.44
r0 = 0.131349

h = hbar**2/(2*m)

N = 600
r_max = 2

r = np.linspace(0, r_max, N+2)[1:-1]
dr = r[1] - r[0]

rp = r - r0

V = D*(np.exp(-2*alpha*rp) - np.exp(-alpha*rp))

H = np.diag(2*h/dr**2 + V)
H += np.diag(-h/dr**2*np.ones(N-1), 1)
H += np.diag(-h/dr**2*np.ones(N-1), -1)

E, psi = np.linalg.eigh(H)

u = psi[:, 0]
u = u/np.sqrt(np.trapezoid(u**2, r))

print("Lowest vibrational energy =", round(E[0], 6), "eV")
print("Lowest vibrational energy =", round(E[0]/1e6, 9), "MeV")

plt.plot(r, u)
plt.xlabel("Internuclear distance r (Angstrom)")
plt.ylabel("Wave function u(r)")
plt.title("Morse Potential: Ground State Wave Function")
plt.grid()
plt.show()