from django.db import models

# Create your models here.

class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()


class About(models.Model):
    description = models.TextField()
    header = models.CharField(max_length=50)
    description2 = models.TextField()
    birthday = models.DateField()
    website = models.URLField()
    phone = models.IntegerField()
    age = models.IntegerField()
    degree = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to="About")
    description3 = models.TextField()

    def __str__(self):
        return self.header


class ContactList(models.Model):
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.email


class Photo(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="Photo")


class Service(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.title


class ServiceDetails(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description1 = models.TextField()
    image = models.ImageField(upload_to="Service")
    header = models.CharField(max_length=100)
    description2 = models.TextField()
    point1 = models.CharField(max_length=100)
    point2 = models.CharField(max_length=100)
    point3 = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.service.title
    

class Project(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to="Project")

    def __str__(self):
        return self.title
    

class ProjectDetail(models.Model):
    detail = models.ForeignKey(Project, on_delete=models.CASCADE)
    intro = models.CharField(max_length=200)
    image1 = models.ImageField(upload_to="Project-Detail")
    image2 = models.ImageField(upload_to="Project-Detail")
    image3 = models.ImageField(upload_to="Project-Detail")
    image4 = models.ImageField(upload_to="Project-Detail")
    category = models.CharField(max_length=30)
    client = models.CharField(max_length=20)
    link = models.URLField()
    date = models.DateField()
    header = models.CharField(max_length=50)
    text = models.TextField()
    
    def __str__(self):
        return self.detail.title


class Faq(models.Model):
    question = models.CharField(max_length=100, blank=False)
    answer = models.TextField(blank=False)

    def __str__(self):
        return self.question