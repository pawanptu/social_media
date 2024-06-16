from django.db import models
from users.models import User

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_set')
    followee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followee_set')

    def __str__(self):
        return f"{self.follower.username} follows {self.followee.username}"
