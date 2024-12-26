from rest_framework import serializers
from .models import Article
from sort.serializers import CategoryListSerializer, TagSerializer
from user.serializers import SuperUserListSerializer

class ArticleListSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, allow_null=False)
    address = serializers.SlugField(max_length=255, unique=True, allow_null=False)
    meta = serializers.TextField(max_length=400, allow_null=False)
    thumbnail = serializers.ImageField()
    likes_count = serializers.IntegerField()
    views_count = serializers.IntegerField()



class ArticleSerializer(serializers.ModelSerializer):
    categories = CategoryListSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    author = SuperUserListSerializer(read_only=True)
    class Meta:
        model = Article
        fields = ['title', 'address', 'meta',
                  'thumbnail', 'categories', 'tags',
                  'body', 'read_time', 'created_at',
                  'last_modified', 'author', 'open_conv',
                  'likes_count', 'views_count']
    