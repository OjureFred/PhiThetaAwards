from rest_framework import serializers
from .models import AwardsAPI
class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardsAPI
        fields = ('id','title', 'description', 'developer', 'url_link')