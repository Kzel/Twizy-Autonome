import keras
import numpy as np
from PIL import Image
from keras.layers import Dense, Flatten, Input
from keras.applications.resnet50 import ResNet50
from keras.models import Model
import os
import matplotlib.pyplot as plt

model = keras.models.load_model("model_final.h5")
test_imgs = os.listdir("test/stop/enhanced")

for img in test_imgs:
    im = Image.open("test/left/enhanced/" + img)
    im = im.resize((224, 224))
    im = np.asarray(im)
    im = im.reshape((1, im.shape[0], im.shape[1], im.shape[2]))
    prob = model.predict(im)
    print(prob)
    print(np.argmax(prob))
    print("---------")