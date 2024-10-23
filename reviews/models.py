from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Review(models.Model) :
    movie_title = models.CharField(max_length=225)
    review_content = models.TextField()
    rating =models.PositiveSmallIntegerField() #ENsure 1-5 validation later
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie_title} - {self.user.username}"