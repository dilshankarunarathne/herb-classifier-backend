import numpy as np
from tensorflow.keras.preprocessing import image

# Load a sample image
img_path = 'dataset/test.png'  # Replace with the actual path to your image file
input_size = (150, 150)

img = image.load_img(img_path, target_size=input_size)

img_array = image.img_to_array(img)

# Expand dimensions and normalize (similar to your training data preprocessing)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0  # Normalize pixel values to [0, 1]

# Make predictions
predictions = model.predict(img_array)

# Assuming you have a list of class labels
plant_classes = ['akkapana', 'iguru', 'non', 'vishnukanthi']  # Update with your actual class labels

predicted_class = plant_classes[np.argmax(predictions[0])]
print("Predicted Class:", predicted_class)