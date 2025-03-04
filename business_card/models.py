from django.db import models


class MainInfoAbout(models.Model):
    job_title = models.CharField(max_length=40)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=16)
    email = models.EmailField()
    office_adress = models.CharField(max_length=200)
    image = models.ImageField(upload_to='main/', blank=True, null=True)


class ServiceOffer(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='services/', blank=True, null=True)


class Clients(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='clients/', blank=True, null=True)
