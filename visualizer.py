import variables, sort
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def visualize(data: dict):
    N =  data['size']
    func = data['sort']

    A = list(range(1,N+1))
    random.shuffle(A)

    x = getattr(sort, variables.sortfunc[func])(A)

    fig, ax = plt.subplots() #creates a figure and subsequent subplots
    ax.set_title(variables.sortname[func])

    bar_sub = ax.bar(range(len(A)), A, align='edge')

    ax.set_xlim(0,N) #sets the maximum limit for the x-axis

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteration = [0]
    def update(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)

        iteration[0] += 1

        text.set_text("# of operations: {}".format(iteration[0]))

    anim = animation.FuncAnimation(fig, func=update, fargs=(bar_sub, iteration), frames=x, repeat=False, interval=1)

    plt.show()