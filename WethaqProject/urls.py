"""
URL configuration for WethaqProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from .views import observer_dashboard,general_search
from .views import observer_dashboard, general_search, search_within_center
from .views import observer_dashboard, general_search, search_within_center, notifications
from .views import observer_dashboard, general_search, search_within_center, notifications, view_files_by_center
from .views import observer_dashboard, general_search, search_within_center, notifications, view_files_by_center, filter_files_by_status
from .views import observer_dashboard, general_search, search_within_center, notifications, view_files_by_center, filter_files_by_status, view_previous_records
from .views import upload_document
from .views import upload_confirmation
from .views import add_new_file
from .views import search_center_files
from .views import view_all_files
from .views import home
from .views import observer_file_details
from .views import observer_dashboard, center_dashboard, prison_dashboard
from .views import view_prison_files
from.views import add_new_detainess,add_new_case
#from django.contrib.auth import views as auth_views




from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('observer/dashboard/', observer_dashboard, name='observer_dashboard'),
    path('center/dashboard/', center_dashboard, name='center_dashboard'),
    path('prison/dashboard/', prison_dashboard, name='prison_dashboard'),
    path('prison/view_prison_files/', view_prison_files, name='view_prison_files'),
    path('observer/general-search/', general_search, name='general_search'),
    path('observer/search-within-center/', search_within_center, name='search_within_center'),
    path('observer/notifications/', notifications, name='notifications'),
    path('observer/view-files-by-center/', view_files_by_center, name='view_files_by_center'),
    path('observer/filter-files-by-status/', filter_files_by_status, name='filter_files_by_status'),
    path('observer/view-previous-records\/', view_previous_records, name='view_previous_records'),
    path('prison/upload-document/', upload_document, name='upload_document'),
    path('prison/upload-confirmation/', upload_confirmation, name='upload_confirmation'),
    path('centers/add-new-file/', add_new_file, name='add_new_file'),
    path('centers/search-center-files/', search_center_files, name='search_center_files'),
    path('centers/view-all-files/', view_all_files, name='view_all_files'),
    path('', home, name='home'),
    path('observer/observer_file_details/', observer_file_details, name='observer_file_details'),
    #path('prison/view_prison_files/', view_prison_files, name='view_prison_files'),
    #path('home/', home, name='home'),  # الصفحة الرئيسية
    path('centers/add-new-detainess/',add_new_detainess, name='add_new_detainess'),  # صفحة إضافة موقوف
    path('centers/add-new-case/',add_new_case, name='add_new_case'),  # صفحة إضافة قضية
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    path('api/users/', include('users.urls')),
    path('api/centers/', include('centers.urls')),
    path('api/', include('cases.urls')),

]