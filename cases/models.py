from django.db import models
from centers.models import Center

class CASE_STATUS_CHOICES(models.TextChoices):
    UNDER_INVESTIGATION = 'under_investigation', 'Under Investigation' # قيد التحقيق
    IN_COURT = 'in_court', 'In Court' # في القضاء
    JUDGMENT_ISSUED = 'judgment_issued', 'Judgment Issued' # تم اصدار القضية
    IN_PRISON = 'in_prison', 'In Prison' # في السجن
    RELEASED = 'released', 'Released' #تم اطلاق صراحة 

class IDTypes(models.TextChoices):
    CIVIL_REGISTRY = 'civil_registry', 'Civil Registry' # سجل مدني
    RESIDENT_ID = 'resident_id', 'Resident ID' # هوية مقيم
    VIOLATOR_REFUGEE_ID = 'violator_refugee_id', 'Violator Refugee ID' # هوية مخالف لاجئ
    REPLACEMENT_CARD = 'replacement_card', 'Replacement Card' # بطاقة بديلة

class DETAINEE_STATUSES(models.TextChoices):
    DETAINED = 'detained', 'Detained (Under Investigation)'
    UNDER_REVIEW = 'under_review', 'Under Review (In Court)'
    SENTENCED = 'sentenced', 'Sentenced (Judgment Issued)'
    IMPRISONED = 'imprisoned', 'Imprisoned (Transferred to Prison)'
    RELEASED = 'released', 'Released (From Custody)'


class Detainee(models.Model):
    name = models.CharField(max_length=100) # اسم المتهم
    nationality = models.CharField(max_length=100) # الجنسية
    id_type = models.CharField(max_length=100, choices=IDTypes.choices) # نوع الهوية
    id_number = models.CharField(max_length=100) # رقم الهوية
    date_of_birth = models.DateField() # تاريخ الميلاد
    address = models.CharField(max_length=100) # العنوان
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('id_type', 'id_number')  # Ensure unique combination of id_type and id_number
    def __str__(self):
        return f"{self.name} - {self.nationality}"

class Case(models.Model):
    detainee = models.ForeignKey(Detainee, on_delete=models.CASCADE, related_name='cases') # المتهم
    center = models.ForeignKey(Center, on_delete=models.CASCADE, related_name='cases') # المركز
    
    charge = models.CharField(max_length=100) # التهمة
    case_number = models.CharField(max_length=100) # رقم القضية
    
    arresting_authority = models.CharField(max_length=100) # جهة القبض
    arresting_place = models.CharField(max_length=100) # مكان القبض
    arresting_date = models.DateField() # تاريخ القبض
    detention_agency = models.CharField(max_length=100) #جهة التوقيف
    
    # after this only prison director can edit
    
    status = models.CharField(max_length=100, choices=CASE_STATUS_CHOICES.choices, default='under_investigation') # حالة القضية
    detainee_status = models.CharField(max_length=100, choices=DETAINEE_STATUSES.choices, default='detained') # حالة المتهم
    
    judgment_date = models.DateField(help_text="The date of the judgment.", null=True, blank=True) # تاريخ القضية
    sentence_duration = models.CharField(max_length=100, help_text="The duration of the sentence.", null=True, blank=True) # مدة الحجز
    sentence_start_date = models.DateField(help_text="The start date of the sentence.", null=True, blank=True) # تاريخ بدء الحجز
    sentence_end_date = models.DateField(help_text="The end date of the sentence.", null=True, blank=True) # تاريخ نهاية الحجز
    
    prison_arrival_date = models.DateField(help_text="The date the detainee arrived at the prison.", null=True, blank=True)  # تاريخ الوصول إلى السجن
    release_date = models.DateField(help_text="The release date of the detainee.", null=True, blank=True)  # تاريخ الإفراج
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Notification(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for Case {self.case.id}"