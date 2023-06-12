from django.db import models

from author.decorators import with_author
from app_post.models import Post
from app_user.models import CustomUser


@with_author
class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.text[:10]}... by {CustomUser.objects.get(id=self.author_id)} created {self.creation_date} ({Post.objects.get(id=self.post_id)})'
