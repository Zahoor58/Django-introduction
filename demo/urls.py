
from django.contrib import admin
from django.urls import path, include
from . import views
from  .views import Another,BookViewSet
from  rest_framework import  routers
router=routers.DefaultRouter()
router.register('books',BookViewSet)

urlpatterns = [
    path('firstfunction/',views.first),
    path('first_temp/',views.first_temp),
    path('another/',Another.as_view()),
    path('', include(router.urls))
] 