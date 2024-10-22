from django.db import models
from django.utils import timezone

class Application(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    date_applied = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, default='pending')
    tenth_marks = models.FloatField()
    twelfth_marks = models.FloatField()
    graduation_marks = models.FloatField()

    profile_picture = models.ImageField(upload_to='uploads/', null=True, blank=True)
    document = models.FileField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return self.name
