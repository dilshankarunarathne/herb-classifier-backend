import cv2


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

    # TODO rest of the implementation
    pass
