from django.db import models

# Create your models here.
class List(models.Model):
    activity = models.CharField(max_length=200,blank="True")
    completed = models.BooleanField(default=False)
    

    def __str__(self):
        return self.activity