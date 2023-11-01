from django.urls import path
from .views import ImageClassification

urlpatterns = [
    path('predict/', ImageClassification.as_view(), name='predict_image'),
]
