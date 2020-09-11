from django.db import models

# Create your models here.

class UrlModel(models.Model):
	url = models.CharField(max_length=300)
	check = models.BooleanField(verbose_name='Проверяется')
	url_status = models.BooleanField(null=True, blank=True, editable=False)
	def __str__(self):
		return f"{self.url} {self.check}"
