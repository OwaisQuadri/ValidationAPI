from django.urls import path
from .views import LockStatus,SetLockStatus

urlpatterns = [
    path('<str:lock_name>/', LockStatus.as_view()),
    path('', SetLockStatus.as_view())
]