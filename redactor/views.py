from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
import json


@csrf_exempt
@require_POST
@login_required
def upload(request):
    for f in request.FILES.getlist('file'):
        destination = open('media/test.png', 'wb+')
        for chunk in f.chunks():
            destination.write(chunk)
        destination.close()

    response = {"error": "Just an error"}
    images = [
        {'filelink': '/media/test.png'},
    ]
    return HttpResponse(json.dumps(images), mimetype='application/json')

