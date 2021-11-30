from django.urls import path
from .views import LockStatus, LockStatusDetail

urlpatterns = [
    path('<str:lock_name>/', LockStatusDetail.as_view()),
    path('', LockStatus.as_view())
]