from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator



class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,
    validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True) 
    class Meta:
        model = User