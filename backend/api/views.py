from django.shortcuts import render
from django.db import models
from .models import Story, Collection
from .serializers import CollectionSerializer, StorySerializer, StoryDetailSerializer, CollectionDetailSerializer
from rest_framework import generics, permissions
from .second import start_chat, construct_prompt


class StoryList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = StorySerializer
   
    def get_queryset(self):
        return Story.objects.all()
    
    def perform_create(self, serializer):
        user_input = self.request.data.get('user_input')
        user_input = construct_prompt(user_input)
        start = start_chat(user_input)
        serializer.save(generated_context=start)
    
class StoryRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StoryDetailSerializer
    queryset = Story.objects.all()

class CollectionList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CollectionSerializer

    def get_queryset(self):
        user = self.request.user
        return Collection.objects.filter(user=user.user_id)

class CollectionRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CollectionDetailSerializer

    def get_queryset(self):
        user = self.request.user
        return Collection.objects.filter(user=user.user_id)
