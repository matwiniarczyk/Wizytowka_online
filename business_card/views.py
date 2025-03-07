from django.core.mail import EmailMessage

from django.shortcuts import render, redirect

from business_card.forms import ContactMessageForm
from business_card.models import MainInfoAbout, ServiceOffer
from wizytowka_config import settings


# Create your views here.

def home_view(request):
    form = ContactMessageForm(request.POST or None) # OR NONE ZAPOBIEGA WALIDACJI PRZY GET

    ola_info = MainInfoAbout.objects.first()
    image_url = ola_info.image.url if ola_info and ola_info.image else None
    offers = ServiceOffer.objects.all()


    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()

            user_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']

            email = EmailMessage(
                subject=subject,
                body=f"Od: {name} <{user_email}>\n\n{message}",
                from_email=settings.EMAIL_HOST_USER,
                # MUSZE PODAĆ SWOJEGO MAILA BO SMTP NIE POZWALA NA DOWOLNE USTAWIENIE from_email, BO WYMAGA TO AUTORYZACJI
                to=[settings.EMAIL_HOST_USER],
                reply_to=[user_email],
            )

            email.send(fail_silently=False)

            return redirect("success")
        else:
            # UŻYWAM ZNOWU RENDER ZAMIAST REDIRECT, ŻEBY NIE STRACIĆ DANYCH W FORMULARZU
            return render(request, 'base.html', {
                'form': form,
                'ola_info': ola_info,
                'image_url': image_url,
                'offers': offers,
            })

    return render(request, 'base.html', {
        'form': form,
        'ola_info': ola_info,
        'image_url': image_url,
        'offers': offers,
    })


def success_view(request):
    return render(request, 'success.html')
