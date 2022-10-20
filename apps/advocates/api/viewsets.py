from unittest import result

from apps.advocates.models import Advocate
from core.pagination import CustomPagination
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import AdvocateSerializer


class AdvocateViewSet(viewsets.ModelViewSet):
    serializer_class = AdvocateSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Advocate.objects.all()
        username = self.request.query_params.get('username')
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset
    
