from django_filters import rest_framework as filters
from .models import Case


class CaseFilter(filters.FilterSet):
    #Center filters
    center_name = filters.CharFilter('center__name', lookup_expr="icontains")
    center_location = filters.CharFilter('center__location', lookup_expr="icontains")
    
    #Detainee filters
    detainee_name = filters.CharFilter('detainee__name', lookup_expr="icontains")
    detainee_address = filters.CharFilter('detainee__address', lookup_expr="icontains")
    detainee_nationality = filters.CharFilter('detainee__nationality')
    detainee_id_type = filters.CharFilter('detainee__id_type' )
    id_number = filters.CharFilter('detainee__id_number'),
    
    class Meta:
        model = Case
        fields = [
            "charge",
            "case_number",
            "arresting_authority",
            "arresting_place",
            "arresting_date",
            "detention_agency",
            "status",
            "detainee_status",
        ]
