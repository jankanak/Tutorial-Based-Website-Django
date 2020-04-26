from django.contrib import admin
from .models import Tutorial,TutorialCategory,TutorialSeries
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

#sometimes it is also needed to not all every fields is showing on the admin database .it is also needed to
#inherit specific portion of your field to the admnin site

class TutorialAdmin(admin.ModelAdmin):
    fieldsets=[
        ("Title/date",{'fields':["tutorial_title","tutorial_published"]}),
        ("URL",{"fields":["tutorial_slug"]}),
        ("Series",{"fields":["tutorial_series"]}),
        ("content",{"fields":["tutorial_content"]})
    ]

    formfield_overrides={
        models.TextField:{'widget': TinyMCE() }
        }



admin.site.register(TutorialCategory)
admin.site.register(TutorialSeries)
admin.site.register(Tutorial,TutorialAdmin)