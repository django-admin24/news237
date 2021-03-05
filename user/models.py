from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from news.models import Post
from django.urls import reverse


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    about = models.TextField()

    @property
    def post_authors(self):
        return self.post_set.all()

    def __str__(self):
        return f'{self.user.username} Profile'


    # def get_absolute_url(self):
    #     return reverse('user:profile', kwargs={'user': self.user.username})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
