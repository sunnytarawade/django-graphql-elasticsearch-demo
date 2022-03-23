from django.http import HttpResponse, JsonResponse
from elasticsearch import Elasticsearch
def ping(request):
    return HttpResponse('pong')
