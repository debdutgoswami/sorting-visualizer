import matplotlib, random, os
from matplotlib import pyplot as plt, animation
try:
    from sorting_visualizer import sort, variables
except ModuleNotFoundError:
    import sort, variables

def visualize(algo: str, *args, **kwargs):
    func = algo

    N =  kwargs.get('size', 100)
    path = kwargs.get('path', os.getcwd())
    show = kwargs.get('show', True)
    save = kwargs.get('save', False)

    A = list(range(1,N+1))
    random.shuffle(A)

    generator = getattr(sort, func)(A)

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

    anim = animation.FuncAnimation(fig, func=update, fargs=(bar_sub, iteration), frames=generator, repeat=True, blit=False, interval=15, save_count=90000)

    if save:
        # setting up path
        _filename = "{}.mp4".format(variables.sortname[func])
        
        path = os.path.join(path, _filename)
        #saves the animation
        anim.save(path, writer=writer)

    if show and not save:
        plt.show() #for showing the animation on screen

    plt.close()