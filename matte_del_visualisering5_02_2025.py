import matplotlib.pyplot as plt
import numpy as np

# Vektorerna
D = np.array([5, -3])
E = np.array([-2, 8])
sum_vector = D + E

# Skapa en figur och axlar
fig, ax = plt.subplots()

# Plotting vektorerna
ax.quiver(0, 0, D[0], D[1], angles='xy', scale_units='xy', scale=1, color="blue", label="Vektor D (5, -3)")
ax.quiver(0, 0, E[0], E[1], angles='xy', scale_units='xy', scale=1, color="red", label="Vektor E (-2, 8)")
ax.quiver(0, 0, sum_vector[0], sum_vector[1], angles='xy', scale_units='xy', scale=1, color="green", label="Summa (3, 5)")

# Skala och etiketter
ax.set_xlim(-3, 7)
ax.set_ylim(-4, 9)
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Lägg till ramar
ax.axhline(0, color='black',linewidth=1)
ax.axvline(0, color='black',linewidth=1)

# Lägg till en legend
ax.legend()

# Visa grafen
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
