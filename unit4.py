import numpy as np
import matplotlib.pyplot as plt

m = 940
hbar = 197.3
k = 100

h = hbar**2/(2*m)

N = 500
r_max = 10

r = np.linspace(0, r_max, N+2)[1:-1]
dr = r[1] - r[0]

b_values = [0, 10, 30]

for b in b_values:

    V = 0.5*k*r**2 + (b/3)*r**3

    H = np.diag(2*h/dr**2 + V)
    H += np.diag(-h/dr**2*np.ones(N-1), 1)
    H += np.diag(-h/dr**2*np.ones(N-1), -1)

    E, psi = np.linalg.eigh(H)

    u = psi[:, 0]
    u = u/np.sqrt(np.trapezoid(u**2, r))

    print("b =", b, "MeV fm^-3")
    print("Ground state energy =", round(E[0], 3), "MeV")

    plt.plot(r, u, label="b = "+str(b))

plt.xlabel("r (fm)")
plt.ylabel("Wave function u(r)")
plt.title("Anharmonic Oscillator Ground State")
plt.legend()
plt.grid()
plt.show()