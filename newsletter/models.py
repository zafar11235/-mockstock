from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Login Model
class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length = 120, blank = True, null = True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	# this is what will be returned as instance of the class
	# Python 3 __str__
	def __unicode__(self):
		return self.email
