from django.contrib import admin
from careers import models as careers_models

admin.site.register(careers_models.Career)

class Career_ApplyAdmin(admin.ModelAdmin):
    field = '__all__'
    readonly_fields = ['file_tag']

admin.site.register(careers_models.Career_Apply,Career_ApplyAdmin)
