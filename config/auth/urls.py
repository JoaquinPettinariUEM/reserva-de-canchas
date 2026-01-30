from django.urls import path
from .views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("", CustomTokenObtainPairView.as_view(), name="token"),
]
