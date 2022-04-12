from django.db import models

# Create your models here.
class Choice(models.Model):
    color_choice = models.CharField(max_length=1000, null=False, blank=False)
    age = models.CharField(max_length=1000, null=False, blank=False)

    def __str__(self):
        return self.color_choice