from django.urls import path
from . import views

urlpatterns = [
    path('cases/create/', views.CreateCaseView.as_view(), name='create-case'),
    path('cases/', views.ListCasesView.as_view(), name='list-all-cases'),
    path('cases/<int:pk>/', views.RetrieveCaseView.as_view(), name='retrieve-case'),
    path('cases/<int:pk>/update/', views.UpdateCaseView.as_view(), name='update-case'),
    path('cases/<int:pk>/delete/', views.DeleteCaseView.as_view(), name='delete-case'),
    
    
    path('detainees/create/', views.CreateDetaineeView.as_view(), name='create-detainee'),
    path('detainees/', views.ListDetaineesView.as_view(), name='list-all-detainees'),
]
