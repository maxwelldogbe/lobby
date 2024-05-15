import uuid
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    PERSONNEL = 'personnel'
    INVESTOR = 'investor'
    CATEGORY_CHOICES = [
        ('investor', 'Investor'),
        ('personnel', 'Personnel'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    telephone = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)


    def __str__(self):
        return self.user.username
    
class EmailConfirmation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    confirmation_token = models.UUIDField(default=uuid.uuid4, editable=False)
    
    
    
class Company(models.Model):
    ROLE_CHOICES =[
        ('manager' , 'Manager'),
        ('assistant manager' , 'Assistant Manager'),
        ('project manager' , 'Project Manager')
    ]  
    
    name = models.CharField(max_length=50)
    date_started = models.DateField(null=True)
    date_ended = models.DateField(null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


class Personnel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    field = models.CharField(max_length=100, null=True)
    skills= models.CharField(max_length=100)
    

class Investor(models.Model):
    INDUSTRY_CHOICES =[
        ('technology','Technology'),
        ('agriculture', 'Agriculture'),
        ('education','Education'),
        ('fashion', 'Fashion')
    ]
        
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio = models.CharField(max_length=300, null=True)
    industry = models.CharField(max_length=100, choices=INDUSTRY_CHOICES)