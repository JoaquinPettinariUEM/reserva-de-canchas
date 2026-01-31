from rest_framework import generics
from .models import Court
from .serializers import CourtSerializer, CourtCreateSerializer
from core.permissions import CanCreateCourt, IsCourtOwnerOrAdmin


class CourtListCreate(generics.ListCreateAPIView):

    def get_serializer_class(self):  # type: ignore
        if self.request.method == "POST":
            return CourtCreateSerializer
        return CourtSerializer

    def get_queryset(self): # pyright: ignore[reportIncompatibleMethodOverride]
        user = self.request.user

        if user.is_superuser:
            return Court.objects.all()

        if user.is_authenticated and getattr(user, "is_club_owner", False):
            return Court.objects.filter(owner=user)

        return Court.objects.none()

    def get_permissions(self):
        if self.request.method == "POST":
            return [CanCreateCourt()]
        return [IsCourtOwnerOrAdmin()]

    def perform_create(self, serializer):
      user = self.request.user
      if user.is_superuser:
          serializer.save()
      else:
          serializer.save(owner=user)



class CourtDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer
    permission_classes = [IsCourtOwnerOrAdmin]
