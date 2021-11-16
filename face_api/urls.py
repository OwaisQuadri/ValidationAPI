from django.urls import path
from .views import FaceAPIView, DeleteFaceAPIView

urlpatterns = [
    path('',FaceAPIView.as_view()),
    path('delete/<str:name>/', DeleteFaceAPIView.as_view())
]