from django.contrib import admin
from django.urls import path, include
from users.views import UserProfileAPIView, StreamSentencesView

urlpatterns = [
    path('', UserProfileAPIView.as_view(), name='user-profile-list-create'),
    path('<uuid:pk>/', UserProfileAPIView.as_view(), name='user-profile-detail'),
    path('<uuid:pk>/', UserProfileAPIView.as_view(), name='user-profile-detail'),
    path('stream', StreamSentencesView.as_view(), name='sse'),    
]
