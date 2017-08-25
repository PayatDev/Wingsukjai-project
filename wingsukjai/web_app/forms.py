from django import forms
from web_app.models import runner

class NewRunnerForm(forms.ModelForm):
    class Meta():
        model = runner
        fields = ('first_name',
                'last_name',
                'age',
                'gender',
                'mobile',
                'shirt_size',
                'distance',
                'slip',
                'date_pay',
                'time_pay',
                )
        labels = {
        "first_name": "ชื่อ (ไม่ต้องใส่คำนำหน้า)",
        "last_name": "นามสกุล",
        "age": "อายุ (นับจากปีเกิด)",
        "gender":"เพศ",
        "mobile":"เบอร์มือถือ (ไม่ต้องใส่ขีด)",
        "shirt_size":"ขนาดเสื้อ",
        "distance":"ระยะที่ต้องการสมัคร",
        "slip":"หลักฐานการชำระเงิน",
        "date_pay":"วันที่ชำระเงิน dd-mm-yyyy เช่น 01-09-2560 ",
        "time_pay":"เวลาที่ชำระเงิน hh:mm เช่น 12:00 ",
        }
