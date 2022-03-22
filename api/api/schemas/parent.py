import graphene
from .child import Child

class Parent(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    child= graphene.Field(lambda:Child)
