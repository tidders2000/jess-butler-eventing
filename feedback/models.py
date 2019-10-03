from django.db import models


# Create your models here.
class Feedback (models.Model):
    horseName = models.CharField(max_length=254, default='')
    owner = models.CharField(max_length=254, default='')
    horse_image = models.ImageField(upload_to='media/reviews')
    review = models.TextField()
    
    
    def __str__(self):
        return self.horseName 


