from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Song)
admin.site.register(models.Tag)
admin.site.register(models.TagType)
admin.site.register(models.Attachment)