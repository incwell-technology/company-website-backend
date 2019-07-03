from django.db import models

# Create your models here.
class Portfolio(models.Model):
    image = models.ImageField(upload_to="Portfolio/static/Portfolio/site-data/", null=False, blank=False)
    link = models.CharField(max_length=300, null=False, blank=False, default="https://www.example.com")

    def __str__(self):
        return self.link
        