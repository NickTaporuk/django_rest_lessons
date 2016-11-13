from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
)
from comments.api.serializers import CommentListSerializer
from comments.models import Comment
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
    user = SerializerMethodField()

    def get_user(self,obj):
        return str(obj.user.username)

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
    deleted_url = post_delete_url
    user = SerializerMethodField()
    image = SerializerMethodField()
    markdown = SerializerMethodField()
    comments = SerializerMethodField()

    def get_comments(self, obj):
        content_type = obj.get_content_type
        object_id = obj.id
        c_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentListSerializer(c_qs, many=True).data
        return comments

    def get_user(self, obj):
        return str(obj.user.username)

    def get_markdown(self, obj):
        return str(obj.get_markdown())

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

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
            'image',
            'markdown',
            'comments',
        ]
