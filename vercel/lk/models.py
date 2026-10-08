# Observer (مراقب)
# PrisonDirector (مدير السجن)
# User - will be linked to center table


# AR
# الاسم
# نوع الهوية
# الجنسية
# تاريخ الميلاد
# رقم الهوية
# التهمة
# جهة القبض
# مكان القبض
# تاريخ القبض
# العنوان
# رقم الجوال
# رقم القضية
# جهة التوقيف

# EN


# Name
# Type of ID
# Nationality
# Date of Birth
# ID Number
# Charge
# Arresting Authority
# Arresting Place
# Arrest Date
# Address
# Mobile Number
# Case Number
# Detention Agency


CASE_STATUS_CHOICES = [
    ('under_investigation', 'Under Investigation'), # قيد التحقيق
    ('in_court', 'In Court'), # في القضاء
    ('judgment_issued', 'Judgment Issued'), # تم اصدار القضية
    ('in_prison', 'In Prison'), # في السجن
    ('released', 'Released'), #تم اطلاق صراحة 
]

class IDTypes(models.TextChoices):
    CIVIL_REGISTRY = 'civil_registry', 'Civil Registry' # سجل مدني
    RESIDENT_ID = 'resident_id', 'Resident ID' # هوية مقيم
    VIOLATOR_REFUGEE_ID = 'violator_refugee_id', 'Violator Refugee ID' # هوية مخالف لاجئ
    REPLACEMENT_CARD = 'replacement_card', 'Replacement Card' # بطاقة بديلة

from django.db import models

class Center(models.Model):
    name = models.CharField(max_length=100) # اسم المركز

class Detainee(models.Model):
    name = models.CharField(max_length=100) # اسم المتهم
    nationality = models.CharField(max_length=100) # الجنسية
    id_type = models.CharField(max_length=100, choices=IDTypes.choices) # نوع الهوية
    id_number = models.CharField(max_length=100) # رقم الهوية
    date_of_birth = models.DateField() # تاريخ الميلاد
    address = models.CharField(max_length=100) # العنوان

class Case(models.Model):
    detainee = models.ForeignKey(Detainee, on_delete=models.CASCADE) # المتهم
    center = models.ForeignKey(Center, on_delete=models.CASCADE) # المركز
    
    charge = models.CharField(max_length=100) # التهمة
    case_number = models.CharField(max_length=100) # رقم القضية
    
    arresting_authority = models.CharField(max_length=100) # جهة القبض
    arresting_place = models.CharField(max_length=100) # مكان القبض
    arresting_date = models.DateField() # تاريخ القبض
    detention_agency = models.CharField(max_length=100) #جهة التوقيف
    
    # after this only prison director can edit
    
    status = models.CharField(max_length=100, choices=CASE_STATUS_CHOICES, default='under_investigation') # حالة القضية
    detainee_status = models.CharField(max_length=100) # حالة المتهم
    
    judgment_date = models.DateField(help_text="The date of the judgment.", null=True, blank=True) # تاريخ القضية
    sentence_duration = models.DurationField(help_text="The duration of the sentence.", null=True, blank=True) # مدة الحجز
    sentence_start_date = models.DateField(help_text="The start date of the sentence.", null=True, blank=True) # تاريخ بدء الحجز
    sentence_end_date = models.DateField(help_text="The end date of the sentence.", null=True, blank=True) # تاريخ نهاية الحجز
    
    prison_arrival_date = models.DateField(help_text="The date the detainee arrived at the prison.", null=True, blank=True)  # تاريخ الوصول إلى السجن
    release_date = models.DateField(help_text="The release date of the detainee.", null=True, blank=True)  # تاريخ الإفراج

# Add Detainee by المركز
# Add Case by المركز
# Edit Case by prison director

# see all detainee (prison director | observer)
# see all detainee in his center only (center user)
# see all cases (prison director | observer)
# see all cases in his center only (center user)

# sell all centers (prison director | observer)






