
from django.contrib import admin
from django.urls import path
from . import views
from  .views import Another
urlpatterns = [
    path('firstfunction/',views.first),
    path('another/',Another.as_view()),
] 