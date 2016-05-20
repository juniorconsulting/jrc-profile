from django.db import models


class Profile(models.Model):
    CONSULTANT = 'CONSULTANT'
    PARTNER = 'PARTNER'
    TITLE_CHOICES = (
        (CONSULTANT, 'Consultant'),
        (PARTNER, 'Partner')
    )
    auth_id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_nr = models.CharField(max_length=40, blank=True)
    bio_text = models.TextField(blank=True)
    fun_fact = models.TextField(blank=True)
    active = models.BooleanField(blank=True)
    title = models.CharField(max_length=40, choices=TITLE_CHOICES, blank=True)
    image = models.ImageField(blank=True)
