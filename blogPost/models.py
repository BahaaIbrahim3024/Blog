from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver

# Create your models here.


# determine the save location for images
def upload_location(instance, filename, **kwargs):
    file_path = 'blog/{author_id}/{title}-{filename}'.format(
        author_id=str(instance.author.id),
        title=str(instance.title),
        filename=filename
    )
    return file_path


class BlogPost(models.Model):
    title = models.CharField(max_length=50, null=False, blank=True)
    body = models.TextField(max_length=5000, null=False, blank=True)
    image = models.ImageField(upload_to=upload_location, null=False, blank=True)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name='Published Date')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Updated Date')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)
    isFavorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title


@receiver(post_delete, sender=BlogPost)
# to make sure that the image is deleted when the post deleted
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


# called before the post saved or committed to the DB (for pre save)
def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username+'-'+instance.title)


pre_save.connect(pre_save_blog_post_receiver, sender=BlogPost)