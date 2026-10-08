from django.shortcuts import render
from django.shortcuts import render
from cases.models import Detainee, Case, CASE_STATUS_CHOICES, DETAINEE_STATUSES

def general_search(request):
    return render(request, 'observer/general_search.html')
def search_within_center(request):
    return render(request, 'observer/search_within_center.html')
def notifications(request):
    return render(request, 'observer/notifications.html')
def view_files_by_center(request):
    return render(request, 'observer/view_files_by_center.html')
def filter_files_by_status(request):
    return render(request, 'observer/filter_files_by_status.html')
def view_previous_records(request):
    return render(request, 'observer/view_previous_records.html')
from django.shortcuts import render

def upload_document(request):
    return render(request, 'prison/upload_document.html')

def upload_confirmation(request):
    return render(request, 'prison/upload_confirmation.html')
def add_new_file(request):
    return render(request, 'centers/add_new_file.html')
def search_center_files(request):
    return render(request, 'centers/search_center_files.html')
def view_all_files(request):
    return render(request, 'centers/view_all_files.html')
def auto_suggest_detainee_id(request):
    return render(request, 'centers/auto_suggest_detainee_id.html')
def home(request):
    return render(request, 'home.html')
def observer_file_details(request):
    return render(request, 'observer/file_details.html')
def observer_dashboard(request):
    return render(request, 'observer/observer_dashboard.html')
def center_dashboard(request):
    return render(request, 'centers/center_dashboard.html')
#def prison_dashboard(request):
   # return render(request, 'prison/prison_dashboard.html')
def view_prison_files(request):
    return render(request, 'prison/view_prison_files.html')
def add_new_detainess(request):
    return render(request, 'centers/add_new_detainess.html')  # عرض صفحة إضافة موقوف الجديده
def add_new_case(request):
    return render(request, 'centers/add_new_case.html')  # عرض صفحة إضافة قضية الجديدة

def prison_dashboard(request):
    # حساب عدد المعتقلين الكلي
    total_detainees = Detainee.objects.count()
    
    # حساب عدد القضايا بناءً على حالة القضية
    cases_under_investigation = Case.objects.filter(status=CASE_STATUS_CHOICES.UNDER_INVESTIGATION).count()
    cases_in_court = Case.objects.filter(status=CASE_STATUS_CHOICES.IN_COURT).count()
    cases_judgment_issued = Case.objects.filter(status=CASE_STATUS_CHOICES.JUDGMENT_ISSUED).count()
    cases_in_prison = Case.objects.filter(status=CASE_STATUS_CHOICES.IN_PRISON).count()
    cases_released = Case.objects.filter(status=CASE_STATUS_CHOICES.RELEASED).count()
    
    # حساب عدد المعتقلين الموجودين في السجن حاليًا
    detainees_in_prison = Detainee.objects.filter(
        cases__status=CASE_STATUS_CHOICES.IN_PRISON
    ).distinct().count()
    
    # تمرير البيانات إلى القالب
    context = {
        "total_detainees": total_detainees,
        "cases_under_investigation": cases_under_investigation,
        "cases_in_court": cases_in_court,
        "cases_judgment_issued": cases_judgment_issued,
        "cases_in_prison": cases_in_prison,
        "cases_released": cases_released,
        "detainees_in_prison": detainees_in_prison,
    }
    
    return render(request, "prison/prison_dashboard.html", context)