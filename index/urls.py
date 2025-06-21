from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('resume/',views.resume,name="resume"),
    path('service/',views.Service.as_view(),name="service"),
    path('service-details/<pk>/',views.ServiceDetails.as_view(),name="service-details"),
    path('portfolio/',views.Project.as_view(),name="portfolio"),
    path('portfolio-details/<pk>',views.ProjectDetail.as_view(),name="portfolio-details"),
    path('contact/',views.contact,name="contact")
]
