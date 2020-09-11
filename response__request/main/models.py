from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.user.username
  
@receiver(post_save, sender=User)
def new_user(sender, instance, created, **kwargs):
  if created:
     Profile.objects.create(user=instance)
     instance.profile.save()

class UrlModel(models.Model):
	url = models.CharField(max_length=300)
	check = models.BooleanField(verbose_name='Проверяется')
	url_status = models.BooleanField(null=True, blank=True, editable=False)
	def __str__(self):
		return f"{self.url} {self.check}"
class IntervalChecksModel(models.Model):
	interval_second = models.IntegerField()