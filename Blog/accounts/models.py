from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User, dispatch_uid="create_profile")
def update_profile(sender, instance, **kwargs):
    if kwargs["created"]:
        Profile.objects.create(user=instance)


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, verbose_name="Логин пользователя")
    username = models.CharField(max_length=128, blank=True, default='Test', verbose_name='Имя пользователя')
    surname = models.CharField(max_length=128, blank=True, default='', verbose_name='Фамилия пользователя')
    

    def __str__(self):
        return self.user

    class Meta():
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
