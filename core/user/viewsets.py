from core.user.serializers import UserSerializer
from core.user.models import User
from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django.shortcuts import get_object_or_404

class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['updated']
    # ordering = ['-updated']

    def get_queryset(self):
        # if self.request.user.is_superuser:
        return User.objects.all()
        return User.objects.filter(id=self.request.user.id)


    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]
        obj = get_object_or_404(User, pk=lookup_field_value)
        self.check_object_permissions(self.request, obj)
        return obj
