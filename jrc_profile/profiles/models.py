from django.db import models


class Profile(models.Model):
    auth_id = models.BigIntegerField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_nr = models.CharField(max_length=40)
    bio_text = models.TextField()
    fun_fact = models.TextField()
    active = models.BooleanField()
