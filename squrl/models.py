from django.db import models
from django.template.defaultfilters import slugify

# URL model to create database to store the shortened urls
class Squrls(models.Model):
    """
    Model for squrl url database
    """
    squrl = models.SlugField(max_length=50, primary_key=True)
    target = models.URLField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    access_date = models.DateTimeField(auto_now=True)
    visits = models.IntegerField(default=0)

    def __str__(self):
        return self.target

    def save(self, *args, **kwargs):
        self.squrl = slugify(self.squrl)
        super(Squrls, self).save(*args, **kwargs)
