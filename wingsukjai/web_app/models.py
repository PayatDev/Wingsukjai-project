from django.db import models
from datetime import datetime

# Create your models here.
class runner(models.Model):

    first_name = models.CharField(max_length=60)

    last_name = models.CharField(max_length=60)

    age = models.IntegerField()

    GENDER = (
        ('M', 'ชาย'),
        ('F', 'หญิง'),
    )
    gender = models.CharField(max_length=1, choices=GENDER)

    mobile = models.CharField(max_length=10)

    SHIRT_SIZES = (
        ('S', 'S ขนาดรอบอก 38 นิ้ว'),
        ('M', 'M ขนาดรอบอก 40 นิ้ว'),
        ('L', 'L ขนาดรอบอก 42 นิ้ว'),
        ('XL', 'XL ขนาดรอบอก 44 นิ้ว'),
    )
    shirt_size = models.CharField(max_length=2, choices=SHIRT_SIZES)

    DISTANCE = (
        ('24', '24 km'),
        ('12', '12 km'),
        ('5', '5 km'),
    )
    distance = models.CharField(max_length=2, choices=DISTANCE)

    slip = models.FileField(upload_to='slip/%Y/%m/%d/')

    date_pay = models.CharField(max_length=10)
    time_pay = models.CharField(max_length=5)

    STATUS = (
        ('รอตรวจสอบ', 'Pending'),
        ('ลงทะเบียนสำเร็จ', 'Approved'),
        ('มีปัญหา', 'Problem'),
    )
    status = models.CharField(max_length=20, choices=STATUS, default='รอตรวจสอบ')

    def __str__(self):
        return self.first_name + " " + self.last_name
