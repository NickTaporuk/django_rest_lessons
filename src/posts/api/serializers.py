from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

from posts.models import Post

post_detail_url = HyperlinkedIdentityField(
    view_name='posts-api:detail',
    lookup_field='slug',
)

post_delete_url = HyperlinkedIdentityField(
    view_name='posts-api:delete',
    lookup_field='slug',
)

class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'publish',
        ]
class PostListSerializer(ModelSerializer):
    url = post_detail_url
    deleted_url = post_delete_url
    class Meta:
        model = Post
        fields = [
            'url',
            'deleted_url',
            'id',
            'user',
            'title',
            'slug',
            'content',
        ]
class PostSDetailerializer(ModelSerializer):
    url = post_detail_url
    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'user',
            'title',
            'slug',
            'content',
        ]
