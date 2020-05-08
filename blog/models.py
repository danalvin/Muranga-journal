from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    slug = models.SlugField(unique=True, max_length=100, null=True)
    created = models.DateTimeField(auto_now_add = True, verbose_name = ('Created'), null=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def get_post_count(self):
        """ Returns amount of posts of this category """
        post_count = Blog.objects.filter(category = self).count()
        return(post_count)

    def get_absolute_url(self):
        return reverse('blog:post_list_by_category', args=[self.slug,])

    
    def __str__(self):
        return self.title
    
class Blog(models.Model):

    STATUS_CHOICES = (
        ('draft', ('Draft')),
        ('published', ('Published')),
    )


    Title = models.CharField(max_length=120)
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.DO_NOTHING, null=True)
    image = models.ImageField(upload_to='image/blog/', null=False)
    textarea = RichTextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name = ('Status'))
    publishedDate = models.DateTimeField(blank=True, null=True) 
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

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog-details', kwargs={'slug': self.slug})