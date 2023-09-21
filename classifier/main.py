import os
import cv2
import numpy as np
from tensorflow.keras.preprocessing import image


def recognize_plant(image):
    blob = cv2.dnn.blobFromImage(
        image,
        1.0,
        (227, 227),
        (78.4263377603, 87.7689143744, 114.895847746),
        swapRB=False
    )

    # TODO 
