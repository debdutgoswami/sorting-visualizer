import variables, sort
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def visualize(data: dict):
    N =  data['size']
    func = data['sort']

    A = list(range(1,N+1))
    random.shuffle(A)

    generator = getattr(sort, variables.sortfunc[func])(A)

    fig, ax = plt.subplots() #creates a figure and subsequent subplots
    ax.set_title(variables.sortname[func])

    bar_sub = ax.bar(range(len(A)), A, align='edge')

    ax.set_xlim(0,N) #sets the maximum limit for the x-axis

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    # Set up formatting for the movie files
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=60, metadata=dict(artist='Debdut Goswami'), bitrate=1800)

    iteration = [0]
    def update(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)

        iteration[0] += 1

        text.set_text("# of operations: {}".format(iteration[0]))

    #print(len(list(generator)))
    anim = animation.FuncAnimation(fig, func=update, fargs=(bar_sub, iteration), frames=generator, repeat=True, blit=False, interval=15, save_count=90000)

    #saves the animation
    anim.save("{}.mp4".format(variables.sortname[func]), writer=writer)

    #plt.show() #for showing the animation on screen 