from django.contrib import admin
from company_manager import models as company_manager_models

admin.site.register(company_manager_models.Company)
