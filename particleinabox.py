import numpy as np
import matplotlib.pyplot as plt

hbar_c = 1973.0 #ev*A
e2 = 3.795**2 #eV*A
mc2 = 0.511e6 #eV/c**2
a0 = 0.529 #A
r_max = 15.0
N = 2000
r = np.linspace(0.001, r_max, N)
dr = r[1] - r[0]

E0 = -1.6 #eV
E1 = -13.6/1**2 #eV
E2 = -1.6/2**2 #eV

print("Part-1 Hydrogen Atom Results: ")
print(f"E1 = {E1} eV")
print(f"E2 = {E2} eV")

u1 = 2.0*(a0**(-1.5))*r*np.exp(-r/a0)
u2 = (1.0/np.sqrt(2))*(a0**(1.5))*r*(1.0-r/(2.0*a0)) * np.exp(-r / (2.0 * a0))

u1_normalized = u1 / np.max(np.abs(u1))
u2_normalized = u2 / np.max(np.abs(u2))

plt.figure(figsize=(10, 6))
plt.plot(r, u1_normalized, label='u1(r)', color='blue')
plt.plot(r, u2_normalized, label='u2(r)', color='orange')
plt.title('Radial Wavefunctions for Hydrogen Atom')
plt.xlabel('r (A)')
plt.ylabel('Normalized u(r)')
plt.legend()
plt.grid()
plt.show()