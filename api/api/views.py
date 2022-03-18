from django.http import HttpResponse, JsonResponse
from elasticsearch import Elasticsearch
def ping(request):
    return HttpResponse('pong')

def search_with_es(request):
    es = Elasticsearch()
    print(es)

    query = {
        "query":{
            "match":{
                "title":"Apple"
            }
        }
    }

    data = es.search(index='elastic_demo',_source=['id','content'],body=query)
    return JsonResponse(data)
