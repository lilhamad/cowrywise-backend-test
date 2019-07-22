from django.urls import path, include
from . import  views
from rest_framework import routers
import user


router = routers.DefaultRouter()
router.register('groups', views.GroupView)
router.register('users', views.UserView)

urlpatterns = [
    path('', include(router.urls))
]
