from django.db import models


class MainInfoAbout(models.Model):
    job_title = models.CharField(max_length=40, verbose_name="Stanowisko")
    name = models.CharField(max_length=20, verbose_name="Imię")
    surname = models.CharField(max_length=20, verbose_name="Nazwisko")
    phone_number = models.CharField(max_length=16, verbose_name="Telefon")
    email = models.EmailField(verbose_name="E-mail")
    office_adress = models.CharField(max_length=200, verbose_name="Adres biura")
    image = models.ImageField(upload_to='main/', blank=True, null=True, verbose_name="Zdjęcie")

    class Meta:
        verbose_name = "Główne info"
        verbose_name_plural = "Główne info"



class ServiceOffer(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nazwa")
    description = models.TextField(verbose_name="Opis")

    class Meta:
        verbose_name = "Usługa"
        verbose_name_plural = "Usługi"

class Clients(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nazwa firmy/Imię klienta")
    description = models.TextField(verbose_name="Opis")
    image = models.ImageField(upload_to='clients/', blank=True, null=True, verbose_name="Zdjęcie")

    class Meta:
        verbose_name = "Klient"
        verbose_name_plural = "Klienci"

class ContactInfo(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name="Imię")
    email = models.EmailField(blank=True, verbose_name="E-mail")
    subject = models.CharField(max_length=30, blank=True, verbose_name="Temat")
    message = models.TextField(blank=True, verbose_name="Wiadomość")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Data wysłania")

    class Meta:
        verbose_name = "Wiadomość"
        verbose_name_plural = "Wiadomości"
