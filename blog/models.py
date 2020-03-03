from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title
    
class Blog(models.Model):
    Title = models.CharField(max_length=120)
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.DO_NOTHING, null=True)
    image = models.ImageField(upload_to='image/blog/', null=False)
    textarea = RichTextField()
    published_date = models.DateTimeField(blank=True, null=True) 
    slug = models.SlugField(unique=True, max_length=100, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Title
    
    @classmethod
    def blog_image(cls):
        image = cls.objects.all()

        return image

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Blog, self).save(*args, **kwargs)