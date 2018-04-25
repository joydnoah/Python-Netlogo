import pandas as pd
import matplotlib.pyplot as plt

def transform_shuttle_list(shuttle_list, time, index):
    return list(map(lambda x: x[index] * 100 / time[-1], shuttle_list))

def plot_shuttles(stop_time, free_time, load_time, time):
    stop_time_shuttle = []
    free_time_shuttle = []
    load_time_shuttle = []
    stop_time_shuttle.append(transform_shuttle_list(stop_time, time, 0))
    free_time_shuttle.append(transform_shuttle_list(free_time, time, 0))
    load_time_shuttle.append(transform_shuttle_list(load_time, time, 0))
    stop_time_shuttle.append(transform_shuttle_list(stop_time, time, 1))
    free_time_shuttle.append(transform_shuttle_list(free_time, time, 1))
    load_time_shuttle.append(transform_shuttle_list(load_time, time, 1))
    stop_time_shuttle.append(transform_shuttle_list(stop_time, time, 2))
    free_time_shuttle.append(transform_shuttle_list(free_time, time, 2))
    load_time_shuttle.append(transform_shuttle_list(load_time, time, 2))

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

def plot_shuttles2(stop_time, free_time, load_time, time):
    stop_time_shuttle = list(map(lambda x: x * 100 / time[-1], stop_time))
    free_time_shuttle = list(map(lambda x: x * 100 / time[-1], free_time))
    load_time_shuttle = list(map(lambda x: x * 100 / time[-1], load_time))

    fig, ax = plt.subplots(1)

    ax.plot(time, stop_time_shuttle, 'r', label='stop')
    ax.plot(time, free_time_shuttle, 'b', label='free')
    ax.plot(time, load_time_shuttle, 'g', label='load')
    ax.set_xlabel('xcor')
    ax.set_ylabel('ycor')
    # ax[0].set_aspect('equal')
    ax.grid(True)

    fig.set_size_inches(14, 5)

    plt.legend()
    plt.show()

def simple_plot(autonomy_value, time, label, start=None, end=None, last_product=None):
    fig, ax = plt.subplots(1)
    ax.plot(time, autonomy_value, 'r', label = label)
    if start is not None:
        ax.axvline(start, color='b')
    if end is not None:
        ax.axvline(end, color='b')
    if last_product is not None:
        ax.axvline(last_product, color='g')
    ax.set_xlabel('xcor')
    ax.set_ylabel('ycor')
    ax.grid(True)

    fig.set_size_inches(14, 5)

    plt.legend()
    plt.show()