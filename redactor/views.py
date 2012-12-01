from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.conf import settings
import json


@csrf_exempt
@require_POST
@login_required
def upload(request):
    images = []
    for f in request.FILES.getlist('file'):

        name = 'media/%s' % f.name
        destination = open(name, 'wb+')
        for chunk in f.chunks():
            destination.write(chunk)
        destination.close()
        images.append({'filelink': '/%s' % name})

    response = {"error": "Just an error"}
    return HttpResponse(json.dumps(images), mimetype='application/json')

