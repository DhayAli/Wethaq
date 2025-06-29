from django.urls import path
from . import views

urlpatterns = [
    path('', views.CenterListView.as_view(), name='list-all-centers'),
]
