from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Blog(models.Model):
    name=models.CharField(max_length=40)
    description=models.TextField()
    image=models.ImageField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.name





