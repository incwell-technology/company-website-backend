from django.contrib import admin
from team import models as team_models

admin.site.register(team_models.Team_Members)
