import matplotlib.pyplot as plt
from random_walk import RandomWalk
# Make random walk
def make_random_walk():
    # Make a random Walk
    rw = RandomWalk(50_000)
    rw.fill_walk()
    
    # Plot the point in the walk
    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(10,6), dpi=128)
    point_numbers = range(rw.numpoints)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    ax.set_aspect("equal")
    
    # Emphasize the first and last point
    ax.scatter(0,0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
        
    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    


while True:
    make_random_walk()
    keep_running = input("Make an other walk (y/n): ")
    if keep_running == "n":
        break
