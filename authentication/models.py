from django.contrib.auth.models import User
from django.db import models
import uuid

class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    telephone = models.CharField(max_length=100)
    CATEGORY_CHOICES = [
        ('investor', 'Investor'),
        ('personnel', 'Personnel'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)


    def __str__(self):
        return self.user.username
    
class EmailConfirmation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    confirmation_token = models.UUIDField(default=uuid.uuid4, editable=False)