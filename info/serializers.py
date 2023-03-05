from rest_framework import serializers
from .models import News, TopNews

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'short_description', 'full_description', 'image', 'created_at')

class TopNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopNews
        fields = ('title', 'short_description', 'image', 'created_at')