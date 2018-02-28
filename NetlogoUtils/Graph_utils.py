import pandas as pd
import matplotlib.pyplot as plt

def plot_something(stop_time, free_time, load_time, time):
    stop_time_shuttle = []
    free_time_shuttle = []
    load_time_shuttle = []
    stop_time_shuttle.append(list(map(lambda x: x[0] * 100 / time[-1], stop_time)))
    free_time_shuttle.append(list(map(lambda x: x[0] * 100 / time[-1], free_time)))
    load_time_shuttle.append(list(map(lambda x: x[0] * 100 / time[-1], load_time)))
    stop_time_shuttle.append(list(map(lambda x: x[1] * 100 / time[-1], stop_time)))
    free_time_shuttle.append(list(map(lambda x: x[1] * 100 / time[-1], free_time)))
    load_time_shuttle.append(list(map(lambda x: x[1] * 100 / time[-1], load_time)))
    stop_time_shuttle.append(list(map(lambda x: x[2] * 100 / time[-1], stop_time)))
    free_time_shuttle.append(list(map(lambda x: x[2] * 100 / time[-1], free_time)))
    load_time_shuttle.append(list(map(lambda x: x[2] * 100 / time[-1], load_time)))

    fig, ax = plt.subplots(1, 3)

    ax[0].plot(time, stop_time_shuttle[0], 'r', label = 'stop')
    ax[0].plot(time, free_time_shuttle[0], 'b', label = 'free')
    ax[0].plot(time, load_time_shuttle[0], 'g', label = 'load')
    ax[0].set_xlabel('xcor')
    ax[0].set_ylabel('ycor')
    # ax[0].set_aspect('equal')
    ax[0].grid(True)

    ax[1].plot(time, stop_time_shuttle[1], 'r', label='stop')
    ax[1].plot(time, free_time_shuttle[1], 'b', label='free')
    ax[1].plot(time, load_time_shuttle[1], 'g', label='load')
    ax[1].set_xlabel('xcor')
    ax[1].set_ylabel('ycor')
    # ax[1].set_aspect('equal')
    ax[1].grid(True)

    ax[2].plot(time, stop_time_shuttle[2], 'r', label='stop')
    ax[2].plot(time, free_time_shuttle[2], 'b', label='free')
    ax[2].plot(time, load_time_shuttle[2], 'g', label='load')
    ax[2].set_xlabel('xcor')
    ax[2].set_ylabel('ycor')
    # ax[2].set_aspect('equal')
    ax[2].grid(True)

    fig.set_size_inches(14, 5)

    plt.legend()
    plt.show()