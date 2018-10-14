from django.db import models

# Create your models here.

class NewsUsers(models.Model):
    email = models.EmailField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email
"""
    class Meta:
        verbose_name = 'NewsUser'
        verbose_name_plural = 'NewsUsers'

 """
