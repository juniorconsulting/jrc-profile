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
    phone_nr = models.CharField(max_length=40, blank=True, null=True)
    bio_text = models.TextField(blank=True, null=True)
    fun_fact = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, default=False)
    title = models.CharField(max_length=40, choices=TITLE_CHOICES, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name