from django.db import models

class Blog(models.Model):
    writer = models.ForeignKey('user.CustomUser', related_name='blog_writer', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:50]
