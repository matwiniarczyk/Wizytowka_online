from django.contrib import admin
from .models import MainInfoAbout, ServiceOffer, Clients, ContactInfo

# Register your models here.

admin.site.register(MainInfoAbout)
admin.site.register(ServiceOffer)
admin.site.register(Clients)
admin.site.register(ContactInfo)