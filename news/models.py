
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
#from ckeditor.fields import RichTextField
#from taggit.managers import TaggableManager
from django.utils.text import slugify
from phone_field import PhoneField


def default_time():
    return timezone.now() + timezone.timedelta(+14)


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    short_title = models.CharField(max_length=500)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images')
    body = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        return super(Category, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

    class Meta:
       verbose_name = 'Category'
       verbose_name_plural = verbose_name

    @property
    def posts_for_frontpage(self):
        return self.categorypost.order_by('-modified')
    

    def get_absolute_url(self):
        return reverse('news:category-detail', kwargs={'slug': self.slug})


STATUS = (
    ('Draft', 'Draft'),
    ('Publish', 'Publish'),
)


class Post(models.Model):
    author = models.ForeignKey("user.Profile", on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    category = models.ForeignKey(Category, related_name="categorypost", on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images')
    body = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=7, choices=STATUS, default='Draft')
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        return super(Post, self).save(*args, **kwargs)

    class Meta:
       verbose_name = 'Post'
       verbose_name_plural = verbose_name
       

    def __str__(self):
        return self.title
        

    class Meta:
        ordering = ('-modified',)

    # def get_post_side(self):
    #     return self.post.order_by('-modified')


    def get_absolute_url(self):
        return reverse('news:post_detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    comment_body = models.TextField()
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    email = models.EmailField()
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)


    class Meta:
      verbose_name = 'Comment'
      verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('news:post_detail', kwargs={'slug': self.slug})


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email



class ContactEnty(models.Model):
    name = models.CharField(max_length=300)
    subject = models.CharField(max_length=300)
    email = models.EmailField()
    phone = phone = models.CharField(max_length=12)
    message = models.TextField(blank=True, null=False)


    def __str__(self):
        return self.name
    
