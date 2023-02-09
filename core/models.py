from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    update_on = models.DateTimeField(auto_now=True)

    class Meta: 
        ordering = ['-created_on']

    def __str__(self) -> str:
        return self.title[:50]
    
    def get_absolute_url(self):
        return reverse ('post_detail', args=[str(self.id)])
    

class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

        