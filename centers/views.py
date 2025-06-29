from rest_framework import generics, status

from helpers.utils import swagger_response
from users import permissions

from .serializers import CenterSerializer
from .models import Center


class CenterListView(generics.ListAPIView):
    permission_classes = [permissions.IsPrisonDirector | permissions.IsObserver]
    queryset = Center.objects.all()
    serializer_class = CenterSerializer
    
    @swagger_response(response_schema={
        200: CenterSerializer,
        400: None,
        404: None
    })
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)