from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.

class Tuple(models.Model):
      string_field=models.CharField(max_length=200)
      numeric_value=models.IntegerField()
      def __str__(self):
          return self.string_field
