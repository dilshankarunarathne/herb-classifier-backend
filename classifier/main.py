import os
import numpy as np
from keras.models import load_model

import cv2

current_dir = os.path.dirname(os.path.abspath(__file__))
model_file_path = os.path.join(current_dir, '..', 'bin', 'classifier_sequential.h5')
model = load_model(model_file_path)

plant_classes = ['akkapana', 'iguru', 'non', 'vishnukanthi']


def recognize_plant(image):
    blob = cv2.dnn.blobFromImage(
        image,
        1.0,
        (227, 227),
        (78.4263377603, 87.7689143744, 114.895847746),
        swapRB=False
    )

    input_size = (227, 227)
    img = image.load_img(blob, target_size=input_size)
    img_array = image.img_to_array(img)

    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalize pixel values to [0, 1]

    predictions = model.predict(img_array)

    predicted_class = plant_classes[np.argmax(predictions[0])]

    # TODO rest of the implementation
    pass
