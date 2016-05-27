from __future__ import unicode_literals

from django.db import models
from django.db.models import Q

#Managers (table level classes)
class SongManager(models.Manager):
	def search(self, q):
		return self.get_queryset().filter((
						Q(title__icontains=q) |
						Q(author__icontains=q) |
						Q(first_line__icontains=q) |
						Q(key_lyric__icontains=q)
					))


# Create your models here.
class Song(models.Model):
	title = models.CharField(db_index=True, max_length=300)
	author = models.CharField(db_index=True, max_length=200, blank=True)
	scripture = models.CharField(db_index=True, max_length=100, blank=True)
	first_line = models.CharField(db_index=True, max_length=300, blank=True)
	key_lyric = models.CharField(db_index=True, max_length=300, blank=True)
	notes = models.CharField(db_index=True, max_length=300, blank=True)
	tags = models.ManyToManyField('Tag', blank=True)
	quarantined = models.BooleanField(default=False)
	objects = SongManager()
	def __str__(self):
		return self.title

class Tag(models.Model):
	name = models.CharField(max_length=50)
	type = models.ForeignKey('TagType')
	def __str__(self):
		return self.name

class TagType(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name

class Attachment(models.Model):
	name = models.CharField(max_length=50)
	location = models.URLField()
	song = models.ForeignKey('Song',on_delete=models.CASCADE)
	def __str__(self):
			return self.name


