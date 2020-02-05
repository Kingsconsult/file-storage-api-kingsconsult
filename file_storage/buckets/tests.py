from django.test import TestCase
from .models import Bucket
from . import views
from rest_framework import status
from rest_framework.test import APIClient



# Create your tests here.

class ModelTestCase(TestCase):
    def setUp(self):
        self.bucket_name = "KK_bucket"
        self.bucket = Bucket(name=self.bucket_name)
        
    def test_to_create_bucket(self):
        old_bucket_count = Bucket.objects.count()
        self.bucket.save()
        new_bucket_count = Bucket.objects.count()
        self.assertNotEqual(old_bucket_count, new_bucket_count)
        
class VIewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.bucket_data = {'name': 'kk_bucket'}
        self.response = self.client.post(views.BucketList(), self.bucket_data, format="json")
    
    
    def test_stuff_view_get_all(self):
        response = self.client.get('/buckets/')
        self.assertEqual(response.status_code, 200)
        