from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.core.mail import send_mail
from .models import Tag, Project


def home(request):
    project_list = Project.objects.all().order_by('id')

    paginator = Paginator(project_list, 16)
    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)

    tags = Tag.objects.all()

    return render(request, "home.html", {
        "projects": projects,
        "tags": tags
    })


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # TEMP: print in terminal
        print("NEW MESSAGE")
        print("Name:", name)
        print("Email:", email)
        print("Message:", message)

        return render(request, "contact.html", {"success": True})

    return render(request, "contact.html")


def project(request, id):
    project = get_object_or_404(Project, pk=id)

    previous_project = Project.objects.filter(id__lt=project.id).order_by('-id').first()
    next_project = Project.objects.filter(id__gt=project.id).order_by('id').first()

    return render(request, "project.html", {
        "project": project,
        "previous_project": previous_project,
        "next_project": next_project
    })

def about_me(request):
    return render(request, "about_me.html")