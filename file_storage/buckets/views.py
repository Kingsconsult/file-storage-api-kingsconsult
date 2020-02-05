from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from .models import Bucket
from . import models
from .serializers import BucketSerializer
from . import serializers

class BucketList(APIView):
    def get(self, request):
        buckets = Bucket.objects.all()
        return Response({"buckets": buckets})
