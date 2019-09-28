from django.db import models

# Create your models here.

class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    
class Company(SingletonModel):
    company_name = models.CharField(max_length=99)
    phone = models.CharField(max_length=300, null=False, blank=False)
    location = models.CharField(max_length=300, null=False, blank=False)
    email = models.CharField(max_length=300, null=False, blank=False)
    video = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return f'{self.company_name}'

