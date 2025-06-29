from django.db.models import Q

from rest_framework import generics, status, filters as drf_filters
from rest_framework.response import Response

from django_filters import rest_framework as filters

from users import permissions
from helpers.utils import swagger_response

from .models import Case, Detainee, Notification
from .serializers import CaseSerializer, CreateCaseSerializer, DetaineeSerializer, NotificationSerializer
from .filters import CaseFilter

class CreateDetaineeView(generics.CreateAPIView):
    permission_classes = [permissions.IsPrisonDirector | permissions.IsCenterUser]
    serializer_class = DetaineeSerializer
    
    @swagger_response(response_schema={
        201: DetaineeSerializer,
        404: None
    })
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class ListDetaineesView(generics.ListAPIView):
    permission_classes = [permissions.IsPrisonDirector | permissions.IsObserver | permissions.IsCenterUser]
    serializer_class = DetaineeSerializer
    
    def get_queryset(self):
        if self.request.user.is_regular_user:
            return Detainee.objects.filter(Q(cases__center__users__user=self.request.user) | Q(cases__isnull=True)).distinct()

        return Detainee.objects.all()
    
    @swagger_response(response_schema={
        200: DetaineeSerializer,
        400: None,
        404: None
    })
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class CreateCaseView(generics.CreateAPIView):
    permission_classes = [permissions.IsPrisonDirector | permissions.IsCenterUser]
    serializer_class = CreateCaseSerializer
    
    @swagger_response(response_schema={
        201: CaseSerializer,
        404: None
    })
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class ListCasesView(generics.ListAPIView):
    permission_classes = [permissions.IsPrisonDirector | permissions.IsObserver | permissions.IsCenterUser]
    serializer_class = CaseSerializer
    filter_backends = (filters.DjangoFilterBackend, drf_filters.SearchFilter)
    filterset_class = CaseFilter
    search_fields = [
        "charge",
        "case_number",
        "arresting_authority",
        "arresting_place",
        "detention_agency",
        "status",
        "detainee_status",
        
        "center__name",
        "center__location",
        
        "detainee__name",
        "detainee__address",
        "detainee__nationality",
        "detainee__id_number"
    ]
    
    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Case.objects.none()
        if self.request.user and self.request.user.is_regular_user:
            return Case.objects.filter(center__users__user=self.request.user)
        return Case.objects.all()
    
    @swagger_response(response_schema={
        200: CaseSerializer,
        400: None,
        404: None
    })
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class RetrieveCaseView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsPrisonDirector | permissions.IsObserver | permissions.IsCenterUser]
    serializer_class = CaseSerializer
    
    def get_queryset(self):
        if self.request.user.is_regular_user:
            return Case.objects.filter(center__users__user=self.request.user)
        return Case.objects.all()
    
    @swagger_response(response_schema={
        200: CaseSerializer,
        400: None,
        404: None
    })
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
# التعديل على القضية فقط مدير السجن
class UpdateCaseView(generics.UpdateAPIView):
    permission_classes = [permissions.IsPrisonDirector]
    serializer_class = CaseSerializer
    queryset = Case.objects.all()
    http_method_names = ['patch']
    
    @swagger_response(response_schema={
        200: CaseSerializer,
        400: None,
        404: None
    })
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

class DeleteCaseView(generics.DestroyAPIView):
    permission_classes = [permissions.IsPrisonDirector]
    queryset = Case.objects.all()
    
    @swagger_response(response_schema={
        200: {'detail': 'Case deleted successfully.'},
        400: None,
        404: None
    })
    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return Response({'detail': 'Case deleted successfully.'}, status=status.HTTP_200_OK)

class ListNotificationsView(generics.ListAPIView):
    permission_classes = [permissions.IsObserver]
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    
    @swagger_response(response_schema={
        200: NotificationSerializer,
        400: None,
        404: None
    })
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class MarkNotificationAsReadView(generics.UpdateAPIView):
    permission_classes = [permissions.IsObserver]
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    http_method_names = ['patch']
    
    def perform_update(self, serializer):
        serializer.save(is_read=True)
    
    @swagger_response(response_schema={
        200: NotificationSerializer,
    })
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)