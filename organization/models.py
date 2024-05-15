from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Contact(models.Model):
    telephone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
   
   
class Location(models.Model):
    addressline = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100) 
    
class Organization(models.Model):
    CATEGORY_CHOICES = [
        ('technology','Technology'),
        ('agriculture', 'Agriculture'),
        ('education','Education'),
        ('fashion', 'Fashion')
    ]
    
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="organization_as_admin")
    title = models.CharField(max_length=120, null=False)
    description = models.CharField(max_length=120, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    category = models.CharField(max_length=120, choices=CATEGORY_CHOICES)
    members = models.ManyToManyField(User, related_name='organizations_as_member', through='Membership')



class Membership(models.Model):
    ROLE_CHOICES = [
        ('member', 'Member'),
        ('manager', 'Manager'),
        ('admin', 'Admin')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    joined_at = models.DateTimeField(auto_now_add=True)