from rest_framework import serializers
from .models import News, TopNews, Music, Actions

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'short_description', 'full_description', 'image', 'created_at')

class ActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actions
        fields = ('id', 'title', 'short_description', 'full_description', 'image', 'created_at')

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'short_description', 'full_description', 'image', 'created_at')

class TopNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopNews
        fields = ('short_description', 'image', 'created_at')