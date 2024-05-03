from django.db import models
from django.contrib.auth.models import User
    
class Company(models.Model):
    name = models.CharField(max_length=50)
    date_started = models.DateField(null=True)
    date_ended = models.DateField(null=True)
    ROLE_CHOICES =[
        ('manager' , 'Manager'),
        ('assistant manager' , 'Assistant Manager'),
        ('project manager' , 'Project Manager')
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

class PersonnelProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    field = models.CharField(max_length=100, null=True)
    skills= models.CharField(max_length=100)
    

class InvestorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    INDUSTRY_CHOICES =[
        ('technology','Technology'),
        ('agriculture', 'Agriculture'),
        ('education','Education'),
        ('fashion', 'Fashion')
    ]
    industry = models.CharField(max_length=100, choices=INDUSTRY_CHOICES)