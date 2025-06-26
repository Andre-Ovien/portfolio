from django.shortcuts import render, redirect
from .models import ContactForm, About, Service, ServiceDetails, Project, ProjectDetail, Photo, ContactList, Faq, Testimonials
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.core.mail import send_mail
from .forms import UserForm

# Create your views here.

def home(request):
    home = Photo.objects.all()[0]
    context ={
        'home': home
    }
    return render(request,'index/index.html', context)

def about(request):
    about = About.objects.all()[0]
    testimonial = Testimonials.objects.all()
    context={
        'about': about,
        'data': testimonial
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

    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

           
            send_mail(
                subject=f"Contact Form: {subject}",
                message=f"Name: {name}\nEmail: {email}\n\n{message}",
                from_email=None,
                recipient_list=['ovienemmanuel99@gmail.com'],  
            )

            
            send_mail(
                subject=' Got your message — thanks for reaching out!',
                message=f"""
Hi {name},

Thank you for getting in touch! I’ve received your message and will get back to you as soon as possible — usually within 24 hours.

I really appreciate your interest and look forward to learning more about how I can help you bring your project to life.

In the meantime, feel free to explore my portfolio or reach out again if there's anything urgent.

Talk soon💚,
Andre
                """,
                from_email=None,
                recipient_list=[email],
            )

            messages.success(request, "Your message was sent successfully!")
            return redirect('home')  
    context={
        'contact': contactlist,
        'questions': q_and_a
    }
    return render(request,'index/contact.html',context)