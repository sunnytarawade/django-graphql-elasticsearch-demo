from graphene import Schema
from .grapheneObjects.Organism import Organism
from .grapheneObjects.Article import Article

class Query(Organism,Article):
    pass
        
schema = Schema(query=Query)