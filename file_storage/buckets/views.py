from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.http import Http404



# Create your views here.
from .models import Bucket
from . import models
from .serializers import BucketSerializer

class BucketList(APIView):
    def get(self, request, format=None):
        buckets = Bucket.objects.all()
        serializer = BucketSerializer(buckets, many=True)
        return Response(serializer.data)


class CreateBucket(APIView):
    def post(self, request, format="json"):
        serializer = BucketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BucketDetail(APIView):
    def get(self, request, pk):
        bucket = get_object_or_404(Bucket, pk=pk)
        data = BucketSerializer(bucket).data
        return Response(data)
    
    def get_object(self, pk):
        try:
            return Bucket.objects.get(pk=pk)
        except Bucket.DoesNotExist:
            raise Http404
        
    def put(self, request, pk, format="json"):
        Bucket = self.get_object(pk)
        serializer = BucketSerializer(Bucket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format="json"):
        Bucket = self.get_object(pk)
        Bucket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)