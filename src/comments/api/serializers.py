from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
)

from comments.models import Comment

comment_detail_url = HyperlinkedIdentityField(
    view_name='comments-api:thread',
    lookup_field='id',
)

class CommentSerializer(ModelSerializer):
    # url = comment_detail_url
    replies_count = SerializerMethodField()

    def get_replies_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0

    class Meta:
        model = Comment
        fields = [
            'id',
            'object_id',
            'content',
            'timestamp',
            'content_type_id',
            'parent_id',
            'user_id',
            'replies_count',
            # 'url'
        ]

class CommentChildSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
            'timestamp',
        ]

class CommentDetailSerializer(ModelSerializer):
    replies = SerializerMethodField()
    replies_count = SerializerMethodField()

    def get_replies(self, obj):
        if obj.is_parent:
            return CommentChildSerializer(obj.children(), many=True).data
        return None

    def get_replies_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0

    class Meta:
        model = Comment
        fields = [
            'id',
            'object_id',
            'content',
            'timestamp',
            'content_type_id',
            'parent_id',
            'replies',
            'replies_count',
            'user_id'
        ]