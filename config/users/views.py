from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status, generics
from .models import User
from .serializers import UserSerializer
from core.permissions import IsAdmin, IsSelfOrAdmin

class UserList(APIView):
    def get_permissions(self):
        if self.request.method == "GET":
            return [IsAdmin()]
        return [AllowAny()]

    def get(self, request):
        users = User.objects.all()
        return Response(UserSerializer(users, many=True).data)

    def post(self, request):
        data = request.data.copy()

        if not request.user.is_authenticated or not request.user.is_superuser:
            data["is_club_owner"] = False
        data["password"] = self.validate_password(data["password"])

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def validate_password(self, value: str) -> str:
        return make_password(value)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSelfOrAdmin]
    queryset = User.objects.all()
    serializer_class = UserSerializer

