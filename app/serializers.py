from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class UsersListeSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_active"]

class UsersDetailsSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
