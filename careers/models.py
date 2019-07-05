from django.db import models

# Create your models here.

class Career(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, default="QA")
    short_description = models.TextField(null=False, blank=False, default="Lorem")
    job_description = models.TextField(null=False, blank=False, default="Lorem")
    skills = models.TextField(null=False, blank=False, default="Lorem")

    def __str__(self):
        return self.title


class Career_Apply(models.Model):
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=False, blank=False, default="Lorem")
    last_name = models.CharField(max_length=200, null=False, blank=False, default="Lorem")
    phone = models.CharField(max_length=500, null=False, blank=False, default="98000000")
    cv = models.FileField(upload_to="careers/static/careers/site-data/career-apply", null=False, blank=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
        