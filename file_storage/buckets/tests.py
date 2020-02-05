from django.test import TestCase
from .models import Bucket
from . import views



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