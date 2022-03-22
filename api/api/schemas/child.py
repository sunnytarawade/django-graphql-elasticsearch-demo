import graphene
from .parent import Parent

class Child(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    parent = graphene.Field(lambda:Parent)