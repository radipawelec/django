from django.db import models
from django.utils import timezone

class Note(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	published_date = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

