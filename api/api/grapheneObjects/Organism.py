from graphene import ObjectType,String,Field, List

from .common import FieldDetails, resolve_all,resolve_single_document, PublishedArticleDetails


class OrganismDetails(ObjectType):
    biosampleId = String()
    breed = Field(FieldDetails)
    organism = Field(FieldDetails)
    sex = Field(FieldDetails)
    publishedArticles = Field(List(PublishedArticleDetails))   

class Organism(ObjectType):
    all_organisms = Field(List(OrganismDetails))
    organism = Field(OrganismDetails,biosampleId=String())

    def resolve_all_organisms(parent,info):
        return resolve_all(parent,info,'organism')
    
    def resolve_organism(parent,info,biosampleId):
        res = resolve_single_document(parent,info,'organism',q="biosampleId:{}".format(biosampleId))
        # print(json.dumps(res,indent=4))
        return res
