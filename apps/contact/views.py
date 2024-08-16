from django.shortcuts import render, redirect

from apps.contact.models import Contact
from apps.common.models import SubEmail


def contact(request):
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        phone = request.POST.get('phone')

        Contact.objects.create(
            name=name,
            email=email,
            message=message,
            phone=phone,
        )

        return redirect(url)
    
    if request.method == "POST":
        sub_email = request.POST.get('subemail')

        SubEmail.objects.create(
            sub_email=sub_email,
        )

        return redirect(url)
    
    return render(request, 'contact.html')
