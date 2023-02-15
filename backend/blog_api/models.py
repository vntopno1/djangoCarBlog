from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django_quill.fields import QuillField
# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image', null=True, blank=True)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name

class blog(models.Model):
    POST_CHOICES = [
        ('POPULAR', 'Popular')
    ]
    category = models.ForeignKey(category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True)
    excerpt = models.CharField(max_length=255, default='')
    content = models.TextField(null=True, blank=True)
    contentTwo = RichTextUploadingField(null=True, blank=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)
    ingredients = QuillField(null=True, blank=True)
    postlabel = models.CharField(max_length=100, choices=POST_CHOICES,null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
