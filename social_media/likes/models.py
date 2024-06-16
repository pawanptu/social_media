from django.db import models
from users.models import User
from discussions.models import Discussion
from comments.models import Comment

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, null=True, blank=True, related_name='likes')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True, related_name='likes')

    def __str__(self):
        return f"{self.user.username} likes {self.discussion or self.comment}"
