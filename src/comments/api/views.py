from django.db.models import Q
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView
)

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)
from posts.api.permissions import IsOwnerOrReadOnly
from posts.api.pagination import (
    PostLimitOffsetPagination,
    PostPageNumberPagination,
)
from .serializers import (
    CommentSerializer,
    CommentDetailSerializer,

)

from comments.models import Comment

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)
#
class CommentDetailAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    lookup_field = 'id'
    pagination_class = PostPageNumberPagination

class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = PostPageNumberPagination #PostLimitOffsetPagination #LimitOffsetPagination #PageNumberPagination