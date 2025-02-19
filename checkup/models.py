from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Staff(models.Model):
    user = models.CharField(max_length=64)

class Checkup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    doctor = models.TextField(max_length=64)
    status_checkup = (
    ('TUNGGU','Masih menunggu'),
    ('KELUAR','Mengeluarkan diri'),
    ('PERIKSA','Pemeriksaan'),
    ('OBAT', 'Menunggu obat'),
    ('SELESAI','Selesai berobat') 
    )
    status_checkup_type = models.CharField(max_length=50,blank=True,null=True,choices=status_checkup)
    recommendations = models.TextField(max_length=255)
    paid = models.BooleanField(default=False)
