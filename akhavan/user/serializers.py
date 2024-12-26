from rest_framework import serializers
from .models import CUser

class SuperUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CUser
        fields = [
            "email", "first_name", "last_name"
            ]