from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MatchPlayerViewSet

router = DefaultRouter()
router.register(
    r"match",
    MatchPlayerViewSet,
    basename="match"
)

urlpatterns = router.urls
