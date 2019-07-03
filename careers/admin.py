from django.contrib import admin
from careers import models as careers_models

admin.site.register(careers_models.Career)
admin.site.register(careers_models.Career_Apply)
