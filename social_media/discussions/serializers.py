from rest_framework import serializers
from .models import Discussion, Hashtag

class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ['id', 'name']

class DiscussionSerializer(serializers.ModelSerializer):
    hashtags = HashtagSerializer(many=True, read_only=True)

    class Meta:
        model = Discussion
        fields = ['id', 'user', 'text', 'image', 'hashtags', 'created_at']

    def create(self, validated_data):
        hashtags_data = validated_data.pop('hashtags')
        discussion = Discussion.objects.create(**validated_data)
        for hashtag_data in hashtags_data:
            hashtag, created = Hashtag.objects.get_or_create(name=hashtag_data['name'])
            discussion.hashtags.add(hashtag)
        return discussion
