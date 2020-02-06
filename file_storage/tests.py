from django.test import TestCase
from buckets.models import Bucket
# from . import views

from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from buckets import dummydb



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
    
    
    def test_view_all_buckets(self):
        response = self.client.get('/buckets/')
        self.assertEqual(response.status_code, 200)
        
    def test_create_bucket(self):
        response = self.client.post('/bucket/', {'name': 'kings'}, format='json')
        self.assertEqual(response.status_code, 201)
        
class ViewTestCaseWithPK(TestCase):
    client = APIClient()

    def setUp(self):
        Bucket.objects.create(**dummydb.bucket_data())
    
    def test_view_bucket_detail(self):      
        response = self.client.get('/bucket/1/')
        self.assertEqual(response.status_code, 200)


class ViewUpdateTest(TestCase):
    client = APIClient()

    def setUp(self):
        Bucket.objects.create(**dummydb.bucket_data())
    
    # def test_update_bucket(self):
    #     response = self.client.get('/buckets/')
    #     data = response.json()
    #     data[0]['id'] = 1
    #     data[0]['name'] = "new name"
    #     data[0]['created_at'] = "2020-02-05T22:58:25.274000Z"
    #     replace = self.client.put('/bucket/1/', data=data[0],  format='json')
    #     self.assertEqual(replace.status_code, 200)
        
    def test_delete(self):
        response = self.client.delete('/bucket/1/')
        self.assertEqual(response.status_code, 204)
        
        
        