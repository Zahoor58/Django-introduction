from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
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