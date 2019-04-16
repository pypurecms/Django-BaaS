from django.utils import timezone
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User


# Create your models here.
class BaseModel(models.Model):
    data = JSONField()
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class BaseContent(BaseModel):
    name = models.CharField(max_length=256)
    content = models.TextField()

    class Meta:
        abstract = True


class Sibling(BaseModel):
    """
    Tag, many to many Person
    """
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)


class Parent(BaseModel):
    """
    Category, one to many Person
    """
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)





class Man(BaseContent):
    """
    Post, the core model to store data.
    Content Types:
        - post
        - url
        - image
        - video
        - file
    """
    parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True)
    siblings = models.ManyToManyField(Sibling, related_name='mans')

class Child(BaseModel):
    """
    Comment, many to one Person
    """
    content = models.TextField(max_length=512)
    name = models.CharField(max_length=256)
    man = models.ForeignKey(Man, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = "{}".format(self.user.id)
            if self.content:
                self.name += " - {}".format(self.content[:16])
        super().save(*args, **kwargs)

class Woman(BaseContent):
    """
    Very similar to Father/Post, A page instead
    """
    Man = models.ForeignKey(Man, on_delete=models.CASCADE)