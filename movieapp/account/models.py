from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to="account", blank=True)
    location = models.CharField(max_length=100, null=True)

@receiver(post_save, sender=User) # receiver yeni bir user oluşturulurken çalışır ve oluşturulan user'ın profile'ını oluşturur.
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User) # user üzerinden save edilirken çalışır ve profile'ını günceller.
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
