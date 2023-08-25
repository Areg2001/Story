from django.urls import path
from .views import  StoryList, CollectionList, StoryRetriveUpdateDestroy, CollectionRetriveUpdateDestroy

urlpatterns = [
    path("story/", StoryList.as_view()),
    path("collection", CollectionList.as_view()),
    path("story/<int:pk>", StoryRetriveUpdateDestroy.as_view()),
    path("collection/<int:pk>", CollectionRetriveUpdateDestroy.as_view()),
]
