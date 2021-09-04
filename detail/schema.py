import graphene
from graphene.types import field
# from graphene.types import field, mutation
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from .models import Field,Crop,Polygon


class FieldType(DjangoObjectType):
    class Meta:
        model = Field
        fields = ("id","location")

class CropType(DjangoObjectType):
    class Meta:
        model = Crop
        fields = ("id","name","agricultural_Data")

class PolygonType(DjangoObjectType):
    class Meta:
        model = Polygon
        fields = ("id","location","field","crop")




class Query(graphene.ObjectType):

    all_fields = graphene.List(FieldType)
    all_Crops = graphene.List(CropType)
    all_Polygons = graphene.List(PolygonType)




    def resolve_all_fields(root, info):
        return Field.objects.all()

    def resolve_all_Crops(root, info):
        return Crop.objects.all()

    def resolve_all_Polygons(root, info):
        return Polygon.objects.all()


class InsertFieldMutation(graphene.Mutation):
    class Arguments:
        location = graphene.String(required=True)

    field = graphene.Field(FieldType)

    @classmethod
    def mutate(cls, root, info, location):
        field = Field(location=location)
        field.save()
        return InsertFieldMutation(field=field)

class UpdateFieldMutation(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

        location = graphene.String(required=True)

    field = graphene.Field(FieldType)

    @classmethod
    def mutate(cls, root, info, location, id):
        field = Field.objects.get(id=id)
        field.location = location
        field.save()

        return UpdateFieldMutation(field=field)


class DeleteFieldMutation(graphene.Mutation):

    class Arguments:
        id = graphene.ID()


    field = graphene.Field(FieldType)

    @classmethod
    def mutate(cls, root, info, id):
        field = Field.objects.get(id=id)
        field.delete()
        return


class Mutation(graphene.ObjectType):

    insert_field = InsertFieldMutation.Field()
    update_field = UpdateFieldMutation.Field()
    delete_field = DeleteFieldMutation.Field()





schema = graphene.Schema(query=Query, mutation=Mutation)

