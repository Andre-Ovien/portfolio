from django.contrib import admin
from .models import ContactForm, About, ContactList, Photo, Service, ServiceDetails, Project, ProjectDetail, Faq

# Register your models here.

admin.site.register(ContactForm)
admin.site.register(About)
admin.site.register(ContactList)
admin.site.register(Photo)
admin.site.register(Service)
admin.site.register(ServiceDetails)
admin.site.register(Project)
admin.site.register(ProjectDetail)
admin.site.register(Faq)