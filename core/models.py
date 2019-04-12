from django.utils import timezone
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User


# Create your models here.
class BaseModel(models.Model):
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Tag(BaseModel):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)


class Category(BaseModel):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)


class Comment(BaseModel):
    content = models.TextField(max_length=512)


class BaseContent(BaseModel):
    name = models.CharField(max_length=256)
    extra = JSONField()

    class Meta:
        abstract = True


class Post(BaseContent):
    """
    Content Types:
        - post
        - url
        - image
        - video
        - file
    """
    content = models.TextField()

