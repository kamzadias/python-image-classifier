from django.db import models

# Create your models here.

class ImageClassification(models.Model):
    imageLink = models.CharField(max_length=200, null=False, blank=False)
    result = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f'{self.imageLink} - {self.result}'