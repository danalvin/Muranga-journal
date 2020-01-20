from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


# Create your models here.


class Blog(models.Model):
    Title = models.CharField(max_length=120)
    picture = models.ImageField(upload_to='inage/', null=False)
    textarea = RichTextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Title
    
    @classmethod
    def blog_image(cls):
        picture = cls.objects.all()

        return picture
