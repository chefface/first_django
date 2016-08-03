from django.db import models

# Create your models here.
class State(models.Model):
	abbreviation = models.CharField(max_length=2, null=True, blank=True)
	name = models.CharField(max_length=100, null=True, blank=True)


	def __unicode__(self):
		return '%s' % self.name



class StateCapital(models.Model):
	state = models.OneToOneField("app.State", null=True)
	name = models.CharField(max_length=100, null=True, blank=True)
	latitude = models.FloatField(null=True, blank=True)
	longitude = models.FloatField(null=True, blank=True)
	capital_population = models.IntegerField(null=True, blank=True)

	def __unicode__(self):
		return self.name


class City(models.Model):
	state = models.ForeignKey("app.State", null=True)
	name = models.CharField(max_length=100, null=True, blank=True)
	county = models.CharField(max_length=100, null=True, blank=True)
	latitude = models.FloatField(null=True, blank=True,)
	longitude = models.FloatField(null=True, blank=True,)
	zipcode = models.IntegerField(null=True, blank=True,)

	def __unicode__(self):
		return '%s' % self.name
