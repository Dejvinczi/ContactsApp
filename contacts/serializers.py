from django.conf import settings

from rest_framework import serializers

from authentication.models import CustomUser
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ("name", "first_name", "last_name", "phone")
