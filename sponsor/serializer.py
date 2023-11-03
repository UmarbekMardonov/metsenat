from rest_framework import serializers
from .models import Sponsor


class SponsorApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ['type', 'full_name', 'phone_number', 'amount', 'office_name']


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ['type', 'full_name', 'phone_number', 'amount', 'office_name', 'status']
