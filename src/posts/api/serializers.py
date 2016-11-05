from rest_framework.serializers import ModelSerializer

from posts.models import Post
class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'publish',
        ]
class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'title',
            'slug',
            'content',
        ]
class PostSDetailerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'title',
            'slug',
            'content',
        ]
