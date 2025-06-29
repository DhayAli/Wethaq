from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from drf_spectacular.utils import extend_schema


def format_properties(properties):
    """
    Format properties for swagger documentation

    Parameters:
    - properties: dict

    Returns:
    - dict

    Examples:
    --------
    >>> format_properties({'email': 'This field is required.'})
    {
        'email': {'example': 'This field is required.'}
    }
    """
    formatted_properties = {}
    for key, value in properties.items():
        if isinstance(value, dict):
            formatted_properties[key] = format_properties(value)
        else:
            formatted_properties[key] = {"example": value}
    return formatted_properties


def format_response_schema(response_schema={}):
    """
    Format response schema for swagger documentation

    Parameters:
    - response_schema: dict

    Returns:
    - dict

    Examples:
    --------
    
    >>> format_response_schema({
        200: {"data": "success"},
        400: {"email": ["This field is required."]},
        401: {"detail": "Authentication credentials were not provided."},
        403: {"detail": "You are not allowed to perform this action."},
        404: {"detail": "Not Found."},
        500: {"error": "Internal Server Error"},
    })
    {
        200: {'properties': {'data': {'example': 'success'}}},
        400: {'properties': {'email': {'example': ['This field is required.']}}},
        401: {'properties': {'detail': {'example': 'Authentication credentials were not provided.'}}},
        403: {'properties': {'detail': {'example': 'You are not allowed to perform this action.'}}},
        404: {'properties': {'detail': {'example': 'Not Found.'}}},
        500: {'properties': {'error': {'example': 'Internal Server Error'}}}
    }
    """
    formatted_response = {}
    for status_code, properties in response_schema.items():
        if status_code and properties is None:
            continue
        if status_code == 204:
            formatted_response[status_code] = {"properties": {}}
        if status_code and properties:
            if isinstance(properties, serializers.SerializerMetaclass):
                formatted_response[status_code] = properties
            else:
                formatted_response[status_code] = {
                    "properties": format_properties(properties)
                }
    return formatted_response


def swagger_response(response_schema={}, *args, **kwargs):
    default_responses = {
        200: {"data": _("success")},
        400: {"email": [_("This field is required.")]},
        401: {"detail": _("Authentication credentials were not provided.")},
        404: {"detail": _("Not Found.")},
        500: {"error": _("Internal Server Error")},
    }
    default_responses = format_response_schema({**default_responses, **response_schema})

    if 201 in default_responses and 200 in default_responses:
        del default_responses[200]

    def decorator(view):
        @extend_schema(responses={**default_responses}, *args, **kwargs)
        def wrapper(*args, **kwargs):
            return view(*args, **kwargs)

        return wrapper

    return decorator