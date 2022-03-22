import graphene
from graphene_django import DjangoObjectType
# from .schemas.child import Child
# from .schemas.parent import Parent

from ingredients.models import Category, Ingredient,Post, Author

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "ingredients")

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")

class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ("id", "title")

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ("id", "name")

class AuthorQuery(graphene.ObjectType):
    # posts = graphene.Field(PostQuery)
    id = graphene.Int()
    name = graphene.String()

    # def resolve(parent,info):
    #     return Author.objects.all()

    def resolve_posts(parent,info):
        # return PostQuery()
        # return Post.objects.all()
        return {'id':'2','title':'Heyy'}


class PostQuery(graphene.ObjectType):
    title = graphene.String()
    id = graphene.Int()
    authors = graphene.Field(AuthorQuery)
    # posts = graphene.List(PostType)

    # new_posts = graphene.List(PostType)
    # authors = graphene.List(AuthorType)

    # def resolve_authors(parent,info):
    #     return parent if parent else Author.objects.all()

    # def resolve_new_posts(parent,info):
    #     print(parent,info)
        
    #     return Post.objects.all()

class Person(graphene.ObjectType):
    full_name = graphene.String()

    def resolve_full_name(parent, info):
        # return f"{parent.first_name} {parent.last_name}"
        return parent

def get_human(name):
    return {'first_name':name,'last_name':name}



class Child(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    parent = graphene.Field(lambda:Parent)
    

class Parent(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    child= graphene.Field(lambda:Child)


class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    authors = graphene.Field(AuthorQuery,id=graphene.String())
    posts = graphene.Field(PostQuery)
    # posts = graphene.List(PostType)
    me = graphene.Field(Person)

    child = graphene.Field(Child)
    parent = graphene.Field(Parent)

    def resolve_child(root,info):
        return True
    
    def resolve_parent(root,info):
        return True

    def resolve_authors(root,info,id):
        # print(root,info)
        # return {
        #     'name':'Sunny',
        #     'id':id
        # }
        return Author.objects.get(id=id)

    def resolve_posts(root,info):
        # print(root,info)
        return {'title':'hungry'}

    
    def resolve_me(parent, info):
        # returns an object that represents a Person
        return get_human(name="Luke Skywalker")

    def resolve_all_ingredients(root, info):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)