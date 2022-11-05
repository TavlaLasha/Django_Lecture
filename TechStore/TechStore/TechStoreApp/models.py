from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    pass


class TestModel(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.TextField(null=True)
    age = models.IntegerField()
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def UserAge(self):
        return "{} with age: {}".format(self.name, self.age)
