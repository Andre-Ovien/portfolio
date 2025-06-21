from django.shortcuts import render
from .models import ContactForm, About, Service, ServiceDetails, Project, ProjectDetail, Photo, ContactList, Faq
from django.views.generic import ListView, DetailView


# Create your views here.

def home(request):
    home = Photo.objects.all()[0]
    context ={
        'home': home
    }
    return render(request,'index/index.html', context)

def about(request):
    about = About.objects.all()[0]
    context={
        'about': about
    }
    return render(request,'index/about.html',context)

def resume(request):
    context={

    }
    return render(request,'index/resume.html',context)


class Service(ListView):
    model = Service
    template_name = "index/service.html"
    context_object_name = "services"


class ServiceDetails(DetailView):
    model = ServiceDetails
    template_name = "index/service-details.html"
    context_object_name = "detail"


class Project(ListView):
    model = Project
    template_name = "index/portfolio.html"
    context_object_name = "project"


class ProjectDetail(DetailView):
    model = ProjectDetail
    template_name = "index/portfolio-details.html"
    context_object_name = "details"



def contact(request):
    contactlist = ContactList.objects.all()[0]
    q_and_a = Faq.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        form = ContactForm(name=name, email=email, subject=subject, message=message)
        form.save()

    context={
        'contact': contactlist,
        'questions': q_and_a
    }
    return render(request,'index/contact.html',context)