from django.db import models

# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    img = models.ImageField()
    class Meta:
        db_table ='member'


