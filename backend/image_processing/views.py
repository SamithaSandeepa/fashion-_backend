from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from keras.preprocessing.image import img_to_array, load_img
import numpy as np
from keras.models import load_model
import os
from io import BytesIO


# Load model function
def get_model():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MLMODEL_FOLDER = os.path.join(BASE_DIR, 'image_processing/model/')
    MLMODEL_FILE = os.path.join(MLMODEL_FOLDER, "fashion_mnist_model.h5")
    return load_model(MLMODEL_FILE)

class ImageClassification(APIView):


    class_labels = {
        0: "T-shirt/top",
        1: "Trouser",
        2: "Pullover",
        3: "Dress",
        4: "Coat",
        5: "Sandal",
        6: "Shirt",
        7: "Sneaker",
        8: "Bag",
        9: "Ankle boot"
    }


    def post(self, request):
        # Load the model
        model = get_model()

        # Load image from POST request and preprocess
        uploaded_file = request.FILES['image']
        image_stream = BytesIO(uploaded_file.read())
        image = load_img(image_stream, target_size=(28, 28), color_mode='grayscale')
        image = img_to_array(image)
        image = image.reshape(1, 28, 28, 1)
        image = image.astype('float32')
        image = image / 255.0

        # Get model prediction
        prediction = model.predict(image)

        predicted_class = np.argmax(prediction[0])
        

        # Here, you can convert class index to class name if needed.
        label = self.class_labels[predicted_class]
        return Response({"predicted_class": label}, status=status.HTTP_200_OK)

