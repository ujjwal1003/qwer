import numpy as np
import matplotlib.pyplot as plt

e = 3.795
hbar = 1973
m = 0.511e6

h = hbar**2/(2*m)

N = 500
r = np.linspace(0.01, 40, N)
dr = r[1]-r[0]

V = -e**2/r

H = np.diag(2*h/dr**2 + V)
H += np.diag(-h/dr**2*np.ones(N-1), 1)
H += np.diag(-h/dr**2*np.ones(N-1), -1)

E, psi = np.linalg.eigh(H)

print("Ground state energy =", E[0], "eV")
print("First excited energy =", E[1], "eV")

print("Analytical energies: -13.6 eV, -3.4 eV")

u1 = psi[:,0]
u2 = psi[:,1]

u1 = u1/np.sqrt(np.trapezoid(u1**2, r))
u2 = u2/np.sqrt(np.trapezoid(u2**2, r))

plt.plot(r,u1,label="Ground state")
plt.plot(r,u2,label="First excited state")

plt.xlabel("r (Angstrom)")
plt.ylabel("u(r)")
plt.title("Hydrogen Atom")
plt.legend()
plt.grid()
plt.show()