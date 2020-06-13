from django.db import models
from django.conf import settings

# Create your models here.
class Location(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
	place = models.CharField(max_length=200)
	map_url = models.CharField(max_length=300)

	def __str__(self):
		return self.location