from django.db import models

# URL model to create database to store the shortened urls
class Squrls(models.Model):
    """
    Model for squrl url database
    """
    squrl = models.SlugField(max_length=7,primary_key=True)
    long_url = models.URLField(max_length=200)
    creation_date = models.DateTimeField(auto_now=True)
    access_date = models.DateTimeField(auto_now=True)
    visits = models.IntegerField(default=0)

    def __str__(self):
        return self.input_url
