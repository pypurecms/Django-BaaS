from django.contrib import admin

# Register your models here.
from .models import Parent, Man, Woman, Child, Sibling

admin.site.register(Parent)
admin.site.register(Man)
admin.site.register(Woman)
admin.site.register(Child)
admin.site.register(Sibling)