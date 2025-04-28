import matplotlib.pyplot as plt

""" ## Följt med i koden från boken
import time
def get_time():
    time_now_unformated = time.strftime("%b%d-%H-%p-%M")
    return time_now_unformated
#print(plt.style.available)

time_string = get_time()

x_values=range(1, 1001)
y_values = [x**2 for x in x_values]



fig, ax = plt.subplots()

ax.scatter(x_values, y_values, s=10)

plt.style.use("seaborn-v0_8-pastel")

#ax.plot(input_values, squares, linewidth=3)
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squared of Value", fontsize=14)

ax.axis([0,1100, 0, 1_100_000])
ax.ticklabel_format(style="plain")



ax.tick_params(labelsize=14)

plt.savefig(f"{time_string}_squares_plot.png", bbox_inches='tight')

plt.show()
"""

# 15.1, 15.2 Cubes plot some cube numbers:

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)



plt.show()
