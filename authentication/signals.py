from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from authentication.models import Profile, Investor, Personnel

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Profile)
def create_specific_profile(sender, instance, created, **kwargs):
    if created:
        if instance.category == Profile.INVESTOR:
            Investor.objects.create(user=instance.user)
        elif instance.category == Profile.PERSONNEL:
            Personnel.objects.create(user=instance.user)
