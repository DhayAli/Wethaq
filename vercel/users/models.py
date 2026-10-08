from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

class USER_ROLE_CHOICES(models.TextChoices):
    OBSERVER = 'observer', 'Observer'
    PRISON_DIRECTOR = 'prison_director', 'Prison Director'
    USER = 'user', 'User'

class User(AbstractUser):
    role = models.CharField(max_length=20, choices=USER_ROLE_CHOICES.choices, default=USER_ROLE_CHOICES.USER)
    
    @property
    def is_observer(self):
        return self.role == USER_ROLE_CHOICES.OBSERVER
    
    @property
    def is_prison_director(self):
        return self.role == USER_ROLE_CHOICES.PRISON_DIRECTOR
    
    @property
    def is_regular_user(self):
        return self.role == USER_ROLE_CHOICES.USER

class RegularUserManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(role='user')

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('role', 'user')
        return super().create_user(username, password, **extra_fields)

class ObserverManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(role='observer')

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('role', 'observer')
        return super().create_user(username, password, **extra_fields)

class PrisonDirectorManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(role='prison_director')

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('role', 'prison_director')
        return super().create_user(username, password, **extra_fields)

class RegularUser(User):
    objects = RegularUserManager()
    
    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        self.role = 'user'
        super().save(*args, **kwargs)

class Observer(User):
    objects = ObserverManager()
    
    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        self.role = 'observer'
        super().save(*args, **kwargs)

class PrisonDirector(User):
    objects = PrisonDirectorManager()
    
    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        self.role = 'prison_director'
        super().save(*args, **kwargs)