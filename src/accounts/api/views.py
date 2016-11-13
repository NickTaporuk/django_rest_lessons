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
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)

from posts.api.permissions import IsOwnerOrReadOnly
from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from posts.api.permissions import IsOwnerOrReadOnly
from posts.api.pagination import (
    PostLimitOffsetPagination,
    PostPageNumberPagination,
)
from .serializers import (
    UserCreateSerializer,
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)
from django.contrib.auth import get_user_model
User = get_user_model()

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    