from django.urls import path
from graphene_django.views import GraphQLView
from detail.schema import schema

urlpatterns = [
    # Only a single URL to access GraphQL
    path("graphql2/", GraphQLView.as_view(graphiql=True, schema=schema)),
]