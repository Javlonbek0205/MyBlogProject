from django.db import models
from django.contrib.auth import get_user_model # yaratgan articlaarimizni (get_user_model) bilan bog'lash uchun chaqirildi
from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=150)
  summary = models.CharField(max_length=200, blank=True)
  body = RichTextField()
  photo = models.ImageField(upload_to='images/', blank = True)
  #video = models.FileField(upload_to='videos_uploaded',null=True,
  #validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
  date = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
)
  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('article_detail', args=[str(self.id)])

class Comment(models.Model): #--> comment uchun model yaratildi
  article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
  comment = models.TextField()
  author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE
    )


  def __str__(self):
    return self.comment

  def get_absolute_url(self):
    return reverse('article_detail')
