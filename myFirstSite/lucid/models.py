from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Story(models.Model):
	storyName = models.CharField(max_length=200)
	pub_date = models.DateTimeField('Date Created')
	def __str__(self):
		return self.storyName

class Character(models.Model):
	story = models.ForeignKey(Story, on_delete=models.CASCADE)
	characterName = models.CharField(max_length=200)
	def __str__(self):
		return self.characterName

class CharacterAtt(models.Model):
	character = models.ForeignKey(Character, on_delete=models.CASCADE)
	attrib = models.CharField(max_length=200)
	def __str__(self):
		return self.attrib

class PlotPoint(models.Model):
	story = models.ForeignKey(Story, on_delete=models.CASCADE)
	point = models.CharField(max_length=200)
	def __str__(self):
		return self.point



