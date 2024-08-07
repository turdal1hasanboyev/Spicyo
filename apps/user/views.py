from django.shortcuts import render, redirect

from apps.user.models import About, User
from apps.contact.models import Contact
from apps.common.models import SubEmail
from apps.recipe.models import Recipe
from apps.blog.models import Blog


def about(request):
    url = request.META.get('HTTP_REFERER')

    about = About.objects.get(id=1)

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

    return render(request, 'about.html', {"about": about})

def home(request):
    url = request.META.get('HTTP_REFERER')

    client = User.objects.get(id=1)
    recipes = Recipe.objects.all().order_by("id")[:5]
    about = About.objects.get(id=1)
    blogs = Blog.objects.all().order_by("-id")[:3]

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

    context = {
        'client': client,
        'recipes': recipes,
        'about': about,
        'blogs': blogs,
    }

    return render(request, 'index.html', context)
