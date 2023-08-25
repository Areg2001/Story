from .models import Collection, Story
from rest_framework import serializers

class StorySerializer(serializers.ModelSerializer):
    generated_context = serializers.ReadOnlyField()
    class Meta:

        model = Story
        fields = ("st_id", "name", "user_input", "generated_context", "collection")

class StoryDetailSerializer(serializers.ModelSerializer):
    class Meta:

        model = Story
        fields = ("name", "generated_context")

class CollectionSerializer(serializers.ModelSerializer):
    stories = StoryDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Collection
        fields = ('user', "name", "stories")

class CollectionDetailSerializer(serializers.ModelSerializer):
    stories = StorySerializer(many=True, read_only=True)
    class Meta:

        model = Collection
        fields = ("name", "stories")