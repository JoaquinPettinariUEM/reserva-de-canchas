from django.urls import path
from .views import CourtListCreate, CourtDetail

urlpatterns = [
    path("", CourtListCreate.as_view(), name="courts"),
    path("<int:pk>/", CourtDetail.as_view(), name="courts-detail"),
]
