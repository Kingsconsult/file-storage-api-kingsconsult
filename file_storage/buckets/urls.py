from django.urls import path

from .views import BucketList, CreateBucket, BucketDetail

app_name = "buckets"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('buckets/', BucketList.as_view(), name="buck"),
    path('bucket/', CreateBucket.as_view(), name="bucket"),
    path("bucket/<int:pk>/", BucketDetail.as_view(), name="bucket_detail")
]