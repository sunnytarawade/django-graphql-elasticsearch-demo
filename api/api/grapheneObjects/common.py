from graphene import ObjectType,String
from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=[{"host": "es"}])

def resolve_all(parent,info,index_name,**kwargs):
    # print(index_name)
    res = [x['_source'] for x in es.search(index = index_name,filter_path = ['hits.hits._source'],body = {
            'size' : 10000,
            'query': {
                'match_all' : {}
            }
        })['hits']['hits']]
    # print(json.dumps(res,indent=4))
    return res

def resolve_single_document(parent,info,index_name,q, **kwargs):
    res =  es.search(index = index_name,q=q)['hits']['hits'][0]['_source']
    return res
    

class FieldDetails(ObjectType):
    text = String()
    ontologyTerms = String()

class PublishedArticleDetails(ObjectType):
    articleId = String()
    journal = String()
    title = String()
    year = String()
