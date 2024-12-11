from rest_framework import viewsets, filters
from .models import Reja
from .serializers import RejaSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class RejaViewSet(viewsets.ModelViewSet):
    queryset = Reja.objects.all()
    serializer_class = RejaSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['sana', 'sarlavha']
    ordering = ['sana']

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'bajarildi',
                openapi.IN_QUERY,
                description="Filter by completion status (true or false)",
                type=openapi.TYPE_BOOLEAN
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        bajarildi = self.request.query_params.get('bajarildi')
        if bajarildi is not None:
            if bajarildi == 'true':
                bajarildi = True
            elif bajarildi == 'false':
                bajarildi = False
            queryset = queryset.filter(bajarildi=bajarildi)
        return queryset
