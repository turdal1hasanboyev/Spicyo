from django.shortcuts import render, redirect

from apps.recipe.models import Recipe
from apps.common.models import SubEmail
from apps.contact.models import Contact


def recipe(request):
    url = request.META.get('HTTP_REFERER')

    recipes = Recipe.objects.all().order_by("id")[:5]

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        phone = request.POST.get('phone')

        contact = Contact(name=name, email=email, message=message, phone=phone)

        contact.save()

        return redirect(url)
    
    if request.method == "POST":
        subemail = request.POST.get('subemail')

        SubEmail.objects.create(
            subemail=subemail,
        )

        return redirect(url)

    return render(request, 'recipe.html', {"recipes": recipes})
