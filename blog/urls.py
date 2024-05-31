from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'post', PostViewSet)

urlpatterns = [
    # path('', PostListCreateAPIView.as_view(), name='post-list-create'),
    # path('<int:pk>', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-detail'),
    # path('create/', PostCreateAPIView.as_view()),
    # path('list/', PostListAPIView.as_view()),
    # path('retrieve/<int:pk>/', PostRetrieveAPIView.as_view()),
    # path('update/<int:pk>/', PostUpdateAPIView.as_view()),
    # path('destroy/<int:pk>/', PostDestroyAPIView.as_view()),
    # path('', PostViewSet.as_view({'get':'list','post':'create'})),
    # path('<int:pk>', PostViewSet.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'})),

    path('',include(router.urls)),
]