from django.db import models



class Category(models.Model):
    name=models.CharField(max_length=255)
def __str__(self):
        return self.name
class Post(models.Model):
   
    nomi=models.CharField(max_length=255)
    rasm=models.TextField(max_length=1000)
    narxi=models.IntegerField(default=30)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    


def __str__(self):
        return self.name
