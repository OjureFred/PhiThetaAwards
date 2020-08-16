from rest_framework import serializers
from .models import AwardsAPI
class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardsAPI
        fields = ('title', 'description', 'developer', 'url_link')