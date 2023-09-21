import os
import numpy as np
from tensorflow.keras.preprocessing import image

current_dir = os.path.dirname(os.path.abspath(__file__))
model_file_path = os.path.join(current_dir, '..', 'bin', 'classifier_sequential.h5')
model = None # TODO 

img_path = 'test.png'
input_size = (150, 150)

img = image.load_img(img_path, target_size=input_size)

img_array = image.img_to_array(img)

# Expand dimensions and normalize (similar to your training data preprocessing)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0  # Normalize pixel values to [0, 1]

predictions = model.predict(img_array)

# Assuming you have a list of class labels
plant_classes = ['akkapana', 'iguru', 'non', 'vishnukanthi']  # Update with your actual class labels

predicted_class = plant_classes[np.argmax(predictions[0])]
print("Predicted Class:", predicted_class)
