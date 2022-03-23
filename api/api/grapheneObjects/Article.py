from graphene import List, ObjectType,String,Field
from .common import resolve_all, resolve_single_document

class ArticlesDetails(ObjectType):
    pmcId = String()
    journal = String()
    title = String()
    year = String()


class Article(ObjectType):
    all_articles = Field(List(ArticlesDetails))
    article = Field(ArticlesDetails,pmcId = String())

    def resolve_all_articles(parent,info):
        return resolve_all(parent,info,'article')
    
    def resolve_article(parent,info,pmcId):
        return resolve_single_document(parent,info,'article',q="pmcId:{}".format(pmcId))