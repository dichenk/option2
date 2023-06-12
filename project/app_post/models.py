from django.db import models

from author.decorators import with_author
from app_user.models import CustomUser


@with_author
class Post(models.Model):
    headline = models.CharField(max_length=199)
    text = models.TextField()
    image = models.ImageField(upload_to='images/', default='images/awesome_python.jpg', blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f'post {self.headline} created {self.creation_date} by {CustomUser.objects.get(id=self.author_id)}'