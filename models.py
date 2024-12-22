from django.db import models
from django.contrib.auth.models import User

class Host(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # Other host-related fields...

    def __str__(self):
        return self.name

class Feedback(models.Model):
    host = models.ForeignKey(Host, related_name='feedbacks', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='feedbacks', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.username} for {self.host.name}"
