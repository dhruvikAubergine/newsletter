from rest_framework import serializers
from . models import Subscriber, Blog


class SubscribeSerializer(serializers.ModelSerializer):
    """
        SubscribeSerializer used to subscribe the newsletter.
    """
    class Meta:
        model = Subscriber
        fields = ('email',)


class BlogSerializer(serializers.ModelSerializer):
    """
        BlogSerializer used to add new blog.
    """
    class Meta:
        model = Blog
        fields = ['title', 'content', 'created_at']