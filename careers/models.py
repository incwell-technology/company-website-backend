from django.db import models
from django.utils.safestring import mark_safe


class Career(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, default="QA")
    short_description = models.TextField(null=False, blank=False, default="Lorem")
    job_description = models.TextField(null=False, blank=False, default="Lorem")
    skills = models.TextField(null=False, blank=False, default="Lorem")

    def __str__(self):
        return self.title


class Career_Apply(models.Model):
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, null=False, blank=False, default="Lorem")
    phone = models.CharField(max_length=500, null=False, blank=False, default="98000000")
    cv = models.FileField(upload_to="careers/static/careers/site-data/career-apply", null=False, blank=False)

    def __str__(self):
        return f'{self.full_name}'
        
    def file_tag(self):
        return mark_safe('<a href="/static/%s" target="_blank" class="btn btn-success"/>View</a>' % (self.cv.url.split('/static/')[1]))

    file_tag.short_description = 'CV/Resume'
   