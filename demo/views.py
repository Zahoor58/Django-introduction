from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
# import viewsets from rest_framework
from  rest_framework import viewsets
# import serializers from serializers.py
from .serializers import BookSerializer
# Create your views here.
def first(request):
    return HttpResponse('First message fro  views')
class  Another(View):
    books=Book.objects.filter(is_published=True)
    output=''
    for book in books:
        output+=f"we have {book.title}  b ooks in with {book.id}\n"
    def get(self,request):
        return HttpResponse(self.output)
def first_temp(request):
    books=Book.objects.all()
    return render(request, 'first_temp.html', {'books':books});
# serializer
class BookViewSet(viewsets.ModelViewSet):
    serializer_class= BookSerializer
    queryset=Book.objects.all()