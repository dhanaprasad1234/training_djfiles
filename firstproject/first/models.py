from django.db import models

# Create your models here.
class Second(models.Model):
    Title=models.CharField(max_length=89)
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=89)
    description=models.TextField('Message')

    def __str__(self):
        return self.Title

