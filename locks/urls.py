from django.urls import path
from .views import LockStatus, LockStatusDetail, LogsAPIView

urlpatterns = [
    path('', LockStatus.as_view()),
    path('logs/',LogsAPIView.as_view()),
    path('<str:lock_name>/', LockStatusDetail.as_view()),
]