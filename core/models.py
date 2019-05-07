from django.utils import timezone
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User
from .utils import get_model_name, get_plural_name


# Create your models here.
class BaseModel(models.Model):
    data = JSONField(default=dict, null=False, help_text='The extra data for the object.')
    created = models.DateTimeField(editable=False, help_text='The time the object created.')
    modified = models.DateTimeField(editable=False, help_text='The time the object modified.')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                             help_text='The user who the object belongs to.')

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class BaseContent(BaseModel):
    name = models.CharField(max_length=256,
                            help_text='The title/name for the content, for example, a title for a blog post.'
                            )
    content = models.TextField(
        help_text='The description for the content, for example, the question detail or a blog post.'
    )

    class Meta:
        abstract = True

    def __str__(self):
        return "{0} {1}".format(self.id, self.name)


class Sibling(BaseModel):
    """
    Tag, many to many Human
    """
    name = models.CharField(max_length=64,
                            help_text='The title/name for the object, for example, a tag name.'
                            )
    description = models.CharField(max_length=256,
                                   help_text='The description for the object, for example, a tag description.'
                                   )

    class Meta:
        verbose_name = get_model_name('sibling')
        verbose_name_plural = get_plural_name('sibling')

    def __str__(self):
        return "{0} {1}".format(self.id, self.name)


class Parent(BaseModel):
    """
    Category, one to many Humna
    """
    name = models.CharField(max_length=64,
                            help_text='The title/name for the object, for example, a category name.')
    description = models.CharField(max_length=256,
                                   help_text='The description for the object, for example, a category description.'
                                   )

    class Meta:
        verbose_name = get_model_name('parent')
        verbose_name_plural = get_plural_name('parent')

    def __str__(self):
        return "{0} {1}".format(self.id, self.name)


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
    parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, related_name='humans', null=True,
                               help_text='''A belongs_to relation to parent object, 
                               for example, a question belongs to a category.''')
    siblings = models.ManyToManyField(Sibling, related_name='humans', blank=True,
                                      help_text='''A many_to_many relation to siblings object, 
                                      for example, a question can have many tags''')

    def __str__(self):
        return "{0} {1}".format(self.id, self.name)

    class Meta:
        verbose_name = get_model_name('human')
        verbose_name_plural = get_plural_name('human')


class Child(BaseModel):
    """
    One human can have one or many children
    """
    content = models.TextField(max_length=512,
                               help_text='''The content for the object,
                               for example, a commit content or an answer detail for the question''')
    name = models.CharField(max_length=256, blank=True, null=True,
                            help_text='''The title/name for the object, 
                            for example, a one line answer or a short answer summary.''')
    human = models.ForeignKey(Human, on_delete=models.SET_NULL, related_name='childs', null=True,
                              help_text='''A belongs_to relation to human object, 
                              for example, an answer belongs to a question.''')

    def __str__(self):
        return "{0} {1}".format(self.id, self.name)

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
    parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, related_name='avatars', null=True,
                               help_text='''A belongs_to relation to parent object, 
                               for example, a question belongs to a category.''')
    siblings = models.ManyToManyField(Sibling, related_name='avatars', blank=True,
                                      help_text='''A many_to_many relation to siblings object, 
                                      for example, a question can have many tags''')

    def __str__(self):
        return "{0} {1}".format(self.id, self.name)

    class Meta:
        verbose_name = get_model_name('avatar')
        verbose_name_plural = get_plural_name('avatar')
