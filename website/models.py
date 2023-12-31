from django.db import models

# Create your models here.
class Record(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=12)
    picture_URL = models.ImageField(upload_to='images')
    city=models.CharField(max_length=10)
    phone=models.CharField(max_length=10)
    country=models.CharField(max_length=10)
    hobby=models.CharField(max_length=100)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")

