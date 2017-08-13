import json
import random, string

import urllib.parse as urlparse

from django.urls import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse

from .models import Squrls

# Create your views here.
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def api(request):
    """
    This view exposes the functionality of the url shortener via an api.
    """
    if request.method == 'POST':
        # load the request body in json_data
        json_data = json.loads(request.body)
        try:
            # The json body of the POST request must have a key 'url' containing the url to be shortened
            target = json_data['url']
        except KeyError:
            # Raise a 404 error if the key does not exist
            return JsonResponse({'error': 'Please send data with key "url" and value as your target url.'})
        # Check if the url exists by parsing and finding the scheme. It is 'http' when valid.
        if urlparse.urlparse(target).scheme:
                try:
                    # Search if the input url exists in the database already.
                    # If it does, return the squrl
                    temp = Squrls.objects.get(target=target)
                    return JsonResponse({'squrl': settings.BASE_SITE + temp.squrl})
                except ObjectDoesNotExist:
                    # Generate the slug and create a new object in database
                    slug = get_slug()
                    urlobj = Squrls(target=target, squrl=slug)
                    urlobj.save()
                    return JsonResponse({'squrl': settings.BASE_SITE + slug})

        else:
            # If url does not exist, return json with error message
            return JsonResponse({'error': 'Given url to shorten does not exist'})

    # If GET is called on /api, redirect to the front-end for manual entry of url
    return HttpResponseRedirect(reverse('squrl:index'))


def db(request):

    squrl = Squrls()
    squrl.save()

    squrls = Squrls.objects.all()

    return render(request, 'db.html', {'squrls': squrls})


def redirect(request):
    pass


def get_slug():
    """
    This method generates a unique slug of length 7 using random function and returns the unique code
    """
    # We want to generate a code of length 7
    code_len = 7
    # create a string containing all uppercase alphabets, lowercase alphabets and digits. 26 + 26 + 10 = 62
    char_set = string.ascii_uppercase + string.digits + string.ascii_lowercase

    # This loop will keep running until a unique short_url is found
    while True:
        # Randomly pick 7 characters from the character set and join to form a string
        slug = ''.join(random.choice(char_set) for _ in range(code_len))
        try:
            # Check for existence in the database to maintain uniqueness
            temp = Squrls.objects.get(pk=slug)
        except:
            return slug
            