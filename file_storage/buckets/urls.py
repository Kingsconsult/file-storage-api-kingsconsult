from django.urls import path

from .views import BucketList

app_name = "buckets"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('buckets/', BucketList.as_view()),
]