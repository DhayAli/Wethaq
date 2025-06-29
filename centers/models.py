from django.db import models

# Create your models here.
class Center(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class CenterUser(models.Model):
    user = models.OneToOneField('users.RegularUser', on_delete=models.CASCADE, related_name='center')
    center = models.ForeignKey(Center, on_delete=models.CASCADE, related_name='users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
