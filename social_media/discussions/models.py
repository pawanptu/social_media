from django.db import models
from users.models import User

class Hashtag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Discussion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    hashtags = models.ManyToManyField(Hashtag, related_name='discussions')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:20]
