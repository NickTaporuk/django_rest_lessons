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
from posts.models import Post

from .pagination import (
    PostLimitOffsetPagination,
    PostPageNumberPagination,
)

from .serializers import (
    PostListSerializer,
    PostSDetailerializer,
    PostCreateUpdateSerializer
)

from .permissions import IsOwnerOrReadOnly

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSDetailerializer
    lookup_field = 'slug'

class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSDetailerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSDetailerializer
    lookup_field = 'slug'

class PostListAPIView(ListAPIView):
    # queryset = Post.objects.all()
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content', 'user__first_name', 'slug']
    pagination_class = PostPageNumberPagination #PostLimitOffsetPagination #LimitOffsetPagination #PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("q")
        # queryset_list = Post.objects.filter(user=self.request.user)
        queryset_list = Post.objects.all()
        # queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(user__icontains=query) |
                Q(user__last_name__icontains=query)
            ).distinct()
        return queryset_list


