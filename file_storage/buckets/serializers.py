from rest_framework import serializers
from . import models

class BucketSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id', 'name', 'created_at', )
        model = models.Bucket