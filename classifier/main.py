import os
import io
from typing import Tuple

import numpy as np
from keras.models import load_model
from keras.preprocessing import image

import cv2

current_dir = os.path.dirname(os.path.abspath(__file__))
model_file_path = os.path.join(current_dir, '..', 'bin', 'classifier_sequential.h5')
model = load_model(model_file_path)

plant_classes = ['akkapana', 'iguru', 'non', 'vishnukanthi']


def recognize_plant(image_file) -> Tuple[str, float]:
    blob = cv2.dnn.blobFromImage(
        image_file,
        1.0,
        (227, 227),
        (78.4263377603, 87.7689143744, 114.895847746),
        swapRB=False
    )

    input_size = (150, 150)  # Resize input image to (150, 150)
    _, img_bytes = cv2.imencode('.jpg', image_file)
    img_io = io.BytesIO(img_bytes)
    img = image.load_img(img_io, target_size=input_size)
    img_array = image.img_to_array(img)

    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalize pixel values to [0, 1]

    predictions = model.predict(img_array)

    predicted_class_index = np.argmax(predictions[0])
    predicted_class = plant_classes[predicted_class_index]
    probability = float(predictions[0][predicted_class_index])

    return predicted_class, probability
