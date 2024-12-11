from rest_framework import viewsets, filters
from .models import Reja
from .serializers import RejaSerializer

class RejaViewSet(viewsets.ModelViewSet):
    queryset = Reja.objects.all()
    serializer_class = RejaSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['sana', 'sarlavha']
    ordering = ['sana']

    def get_queryset(self):
        queryset = super().get_queryset()
        bajarildi = self.request.query_params.get('bajarildi')
        if bajarildi is not None:
            queryset = queryset.filter(bajarildi=bajarildi)
        return queryset
