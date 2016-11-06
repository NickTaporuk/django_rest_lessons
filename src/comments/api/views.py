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
    # filter_backends = [SearchFilter, OrderingFilter]
    # search_fields = ['content', 'user__first_name']
    pagination_class = PostPageNumberPagination #PostLimitOffsetPagination #LimitOffsetPagination #PageNumberPagination

    # def get_queryset(self, *args, **kwargs):
    #     query = self.request.GET.get("q")
    #     # queryset_list = Post.objects.filter(user=self.request.user)
    #     queryset_list = Comment.objects.all()
    #     # queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
    #     if query:
    #         queryset_list = queryset_list.filter(
    #             Q(content__icontains=query) |
    #             Q(user__icontains=query) |
    #             Q(user__first_name__icontains=query) |
    #             Q(user__last_name__icontains=query)
    #         ).distinct()
    #     return queryset_list
#
#
