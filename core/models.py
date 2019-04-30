from django.utils import timezone
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User
from .utils import get_model_name, get_plural_name


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

    class Meta:
        verbose_name = get_model_name('sibling')
        verbose_name_plural = get_plural_name('sibling')


class Parent(BaseModel):
    """
    Category, one to many Humna
    """
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)

    class Meta:
        verbose_name = get_model_name('parent')
        verbose_name_plural = get_plural_name('parent')


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


    class Meta:
        verbose_name = get_model_name('human')
        verbose_name_plural = get_plural_name('human')


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


    class Meta:
        verbose_name = get_model_name('child')
        verbose_name_plural = get_plural_name('child')


class Avatar(BaseContent):
    parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, related_name='avatars', null=True)
    siblings = models.ManyToManyField(Sibling, related_name='avatars')

    def __str__(self):
        return "{0} {1}".format(self.id, self.name)


    class Meta:
        verbose_name = get_model_name('avatar')
        verbose_name_plural = get_plural_name('avatar')
