import os
from skimage import data, io, filters
import matplotlib.pyplot as plt

def load_data(data_directory):
    directories = [d for d in os.listdir(data_directory)
                   if os.path.isdir(os.path.join(data_directory, d))]
    labels = []
    images = []
    for d in directories:
        label_directory = os.path.join(data_directory, d)
        file_names = [os.path.join(label_directory, f)
                      for f in os.listdir(label_directory)
                      if f.endswith(".ppm")]
        for f in file_names:
            images.append(io.imread(f))
            labels.append(int(d))
    return images, labels

ROOT_PATH = '/'
train_data_directory = os.path.join(ROOT_PATH, "TrafficSigns/Training")

images, labels = load_data("TrafficSigns\Training")
plt.hist(labels, 62)
plt.show()