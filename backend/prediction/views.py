from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from prediction.apps import PredictionConfig
import pandas as pd
from myapp.permissions import IsCustomer
from rest_framework.permissions import IsAuthenticated


# Create your views here.
# Class based view to predict based on IRIS model
class IRIS_Model_Predict(APIView):
    permission_classes = [IsCustomer, IsAuthenticated]
    def post(self, request, format=None):
        data = request.data
        keys = []
        values = []
        for key in data:
            keys.append(key)
            values.append(data[key])
        X = pd.Series(values).to_numpy().reshape(1, -1)
        loaded_mlmodel = PredictionConfig.mlmodel
        y_pred = loaded_mlmodel.predict(X)
        y_pred = pd.Series(y_pred)
        target_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
        y_pred = y_pred.map(target_map).to_numpy()
        response_dict = {"Prediced Iris Species": y_pred[0]}
        return Response(response_dict, status=200)