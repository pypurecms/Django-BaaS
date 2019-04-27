from django.utils import timezone
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User


# Create your models here.
class BaseModel(models.Model):
    data = JSONField(default=dict, null=False)
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
    Tag, many to many Human
    """
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)


class Parent(BaseModel):
    """
    Category, one to many Humna
    """
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)


class Human(BaseContent):
    """
    Post, the core model to store data.
    Content Types:
        - post
        - url
        - image
        - video
        - file
    """
    parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, related_name='humans', null=True)
    siblings = models.ManyToManyField(Sibling, related_name='humans')

    def __str__(self):
        return "{0} {1}".format(self.id, self.name)


class Child(BaseModel):
    """
    One human can have one or many children
    """
    content = models.TextField(max_length=512)
    name = models.CharField(max_length=256)
    human = models.ForeignKey(Human, on_delete=models.SET_NULL, related_name='childs', null=True)

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = "{}".format(self.user.id)
            if self.content:
                self.name += " - {}".format(self.content[:16])
        super().save(*args, **kwargs)


class Avatar(BaseContent):
    """
    Each Avatar belongs to a human
    """
    human = models.OneToOneField(Human, on_delete=models.CASCADE, related_name='avatar')
