import requests

import os
from django.shortcuts import render
from django.http import HttpResponse

from .models import Squrls

# Create your views here.
def index(request):
    return render(request, 'index.html')


# Create your views here.
def api(request):
    pass


def db(request):

    squrl = Squrls()
    squrl.save()

    squrls = Squrls.objects.all()

    return render(request, 'db.html', {'squrls': squrls})


def redirect(request):
    pass
