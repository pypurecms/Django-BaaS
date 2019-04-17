from django.contrib import admin

# Register your models here.
from .models import Parent, Human, Avatar, Child, Sibling

admin.site.register(Parent)
admin.site.register(Human)
admin.site.register(Avatar)
admin.site.register(Child)
admin.site.register(Sibling)