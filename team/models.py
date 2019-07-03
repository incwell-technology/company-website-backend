from django.db import models

# Create your models here.

class Team_Members(models.Model):
    full_name = models.CharField(max_length=200, null=False, blank=False, default="John")
    designation = models.CharField(max_length=200, null=False, blank=False, default="Software Engineer")
    image = models.ImageField(upload_to="team/static/team/site-data/team", null=False, blank=False)

    def __str__(self):
        return self.full_name
