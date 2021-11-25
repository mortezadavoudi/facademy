from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image
from datetime import datetime
from slugify import slugify
User = get_user_model()

# Create your models here.
def post_image(instance, filename):
    return datetime.now().strftime("%Y/%m/") + filename

class Category(models.Model):
    title = models.CharField(max_length=200)
    url_title = models.CharField(max_length=300)

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        super(Category, self).save()


class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=True, blank=True, upload_to=post_image)
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None or len(self.slug) < 2:
            self.slug = datetime.now().strftime("%Y/%m/") + slugify(self.title)
        super(Posts, self).save()
        if self.image:
            img = Image.open(self.image)
            img.save(self.image.path, quality=95)
