from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Company(models.Model):
    # company table
    com_name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=15)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.com_name


class Position(models.Model):
    # company position table
    pos_name = models.CharField(max_length=256)
    permissions = models.BigIntegerField(default=1)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pos_name


class User(AbstractUser):
    # user table
    sex = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    # username = models.CharField(max_length=128, unique=True)
    # password = models.CharField(max_length=256)
    # email = models.EmailField(unique=True)
    com_name = models.CharField(Company, max_length=255)
    type = models.CharField(Position, max_length=256)
    gender = models.CharField(max_length=32, choices=sex, default='M')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['c_time']


