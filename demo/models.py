from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(blank=True, unique=True, max_length=36)
    description=models.TextField(max_length=256, blank=True)
    price=models.DecimalField(default=0, max_digits=2, decimal_places=2)
    published=models.DateField(blank=True,null=True,default=None)
    cover=models.ImageField(upload_to='covers/', blank=True)
    is_published=models.BooleanField(default=False)
    def __str__(self):
        return self.title
    #     (0,'Unknown'), 
    #     (1,'processed'),
    #     (2,'Paid')
    # )
    # title = models.CharField(null=True,blank=True, unique=True, default='', 
    #                          choices=STATUSES ,)