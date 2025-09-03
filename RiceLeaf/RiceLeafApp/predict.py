import numpy as np
from keras.preprocessing import image
from tensorflow.keras.models import load_model

from os import getcwd
import cv2 as cv
import imutils


def process(path):

    imagetest = cv.imread(path)
    # test_image = image.img_to_array(test_image)
    # test_image = np.expand_dims(test_image, axis=0)
    classifier = load_model(getcwd() + '\\trained_model_disease.h5')

    gray = cv.cvtColor(imagetest, cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray, (5, 5), 0)

    thresh = cv.threshold(gray, 45, 255, cv.THRESH_BINARY)[1]
    thresh = cv.erode(thresh, None, iterations=2)
    thresh = cv.dilate(thresh, None, iterations=2)
    cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key=cv.contourArea)

    extLeft = tuple(c[c[:, :, 0].argmin()][0])
    extRight = tuple(c[c[:, :, 0].argmax()][0])
    extTop = tuple(c[c[:, :, 1].argmin()][0])
    extBot = tuple(c[c[:, :, 1].argmax()][0])

    new_image = imagetest[extTop[1]:extBot[1], extLeft[0]:extRight[0]]

    image = cv.resize(new_image, dsize=(150, 150), interpolation=cv.INTER_CUBIC)
    image = image / 255.

    image = image.reshape((1, 150, 150, 3))

    result = classifier.predict(image)

    # training_set.class_indices
    print(result[0][0])
    print(result[0][1])
    print(result[0][2])
    # print(result[0][3])
    index=result[0].tolist().index(max(result[0]))
    print("Result index: ",index)

    return rice_diseases[int(index)]


rice_diseases = [
    {
        "name": "Bacterial Leaf Blight",
        "precautions": [
            "Use resistant varieties like IR64.",
            "Avoid excessive nitrogen fertilizer.",
            "Ensure proper water management.",
            "Maintain field hygiene by removing infected debris."
        ],
        "remedies": [
            "Apply copper-based fungicides or streptomycin sprays.",
            "Seed treatment with hot water (54°C for 10 minutes).",
            "Foliar spray of zinc sulfate (0.5%)."
        ]
    },
    {
        "name": "Healthy",
        "precautions": [
            "Use certified, disease-free seeds.",
            "Practice crop rotation with non-host crops.",
            "Ensure balanced fertilization with appropriate nutrients.",
            "Maintain proper drainage and avoid waterlogging.",
            "Use biological agents like Trichoderma to boost plant immunity.",
            "Monitor fields regularly for early signs of pests and diseases."
        ],
        "remedies": [
            "Apply organic compost to enrich soil health.",
            "Use biological control agents for pests.",
            "Implement integrated pest management (IPM) practices."
        ]
    },
    {
        "name": "Leaf Scald",
        "precautions": [
            "Use disease-free seeds and resistant varieties.",
            "Avoid dense planting to improve air circulation.",
            "Reduce nitrogen applications.",
            "Avoid over-irrigation."
        ],
        "remedies": [
            "Spray carbendazim (0.1%) or propiconazole (0.1%).",
            "Maintain low water levels in the early crop stage."
        ]
    },
    {
        "name": "Neck Blast",
        "precautions": [
            "Plant blast-resistant varieties like Pooja or IR64.",
            "Avoid late planting.",
            "Apply potash fertilizers.",
            "Use alternate wetting and drying (AWD) method."
        ],
        "remedies": [
            "Use fungicides like tricyclazole (0.6g/L) or isoprothiolane (1ml/L).",
            "Seed treatment with carbendazim before sowing."
        ]
    },
    {
        "name": "Tungro",
        "precautions": [
            "Plant resistant varieties like IR20 or IR50.",
            "Control leafhopper populations.",
            "Practice synchronized planting in large areas."
        ],
        "remedies": [
            "Apply systemic insecticides like imidacloprid or fipronil.",
            "Spray phosphoric acid-based fertilizers.",
            "Rogue infected plants early."
        ]
    }
]






