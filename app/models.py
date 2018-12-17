from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

from django.db import models

class marry(models.Model):
    marry_choose = (
        ("مجرد", "مجرد"),
        ("متاهل", "متاهل")
    )
    name = models.CharField(choices=marry_choose ,max_length=20)

    def __str__(self):
        return self.name


class sex(models.Model):
    sex_choose = (
        ("مرد", "مرد"),
        ("زن", "زن")
    )
    name = models.CharField(choices=sex_choose,max_length=10)

    def __str__(self):
        return self.name


class madrak(models.Model):
    madrak_choose = (
        ("زیر دیپلم", "زیر دیپلم"),
        ("دیپلم", "دیپلم"),
        ("فوق دیپلم", "فوق دیپلم"),
        ("لیسانس", "لیسانس"),
        ("فوق لیسانس", "فوق لیسانس"),
        ("دکترا", "دکترا")
    )
    name = models.CharField(choices=madrak_choose,max_length=20)

    def __str__(self):
        return self.name


class education(models.Model):
    education_choose = (
        ("کامپیوتر", "کامپیوتر"),
        ("حسابداری", "حسابداری"),
        ("برق", "برق"),
        ("ادبیات", "ادبیات"),
        ("سایر", "سایر")
    )
    name = models.CharField(choices=education_choose, max_length=20)

    def __str__(self):
        return self.name


class ostan(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class shahr(models.Model):
    ostan = models.ForeignKey(ostan, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class job(models.Model):
    job_choose = (
        ("مدیر", "مدیر"),
        ("کارمند", "کارمند"),
        ("کارگر", "کارگر"),
        ("مدرس", "مدرس")
    )
    name = models.CharField(choices=job_choose, max_length=20)

    def __str__(self):
        return self.name


class job_type(models.Model):
    choose = (
        ("نیمه وقت", "نیمه وقت"),
        ("تمام وقت", "تمام وقت"),
        ("پروژه ای", "پروژه ای")
    )
    name = models.CharField(choices=choose,max_length=30)

    def __str__(self):
        return self.name


class job_field(models.Model):
    choose = (
        ("سابداری", "حسابداری"),
        ("برنامه نویسی", "برنلمه نویسی")
    )
    name = models.CharField(choices=choose,max_length=30)

    def __str__(self):
        return self.name


class compane_type(models.Model):
    choose = (
        ("مسیولیت محدود", "مسیولیت محدود"),
        ("سهامی خاص", "سهامی خاص"),
        ("سهامی عام", "سهامی عام"),
        ("سایر", "سایر")
    )
    name = models.CharField(choices=choose,max_length=30)

    def __str__(self):
        return self.name


class worktype(models.Model):
    choose = (
        ("تولیدی", "تولیدی"),
        ("خدماتی", "خدماتی"),
        ("بازرگانی", "بازرگانی"),
        ("دولتی", "دولتی")
    )
    name = models.CharField(choices=choose,max_length=20)

    def __str__(self):
        return self.name


class worcker(models.Model):
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=10)
    email = models.EmailField()
    date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=False)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    id1 = models.CharField(max_length=10, blank=True)
    sex1 = models.ForeignKey(sex,on_delete=models.CASCADE)
    marry_type1 = models.ForeignKey(marry, on_delete=models.CASCADE)
    birthday = models.IntegerField()
    mobile = models.CharField(max_length=11)
    phone = models.CharField(max_length=11)
    madrak1 = models.ForeignKey(madrak, on_delete=models.CASCADE)
    education = models.ForeignKey(education, on_delete=models.CASCADE)
    ostan1 = models.ForeignKey(ostan, on_delete=models.CASCADE)
    shahr1 = models.ForeignKey(shahr, on_delete=models.CASCADE)
    exprience1 = models.IntegerField()
    job1 = models.ForeignKey(job, on_delete=models.CASCADE)
    job_type1 = models.ForeignKey(job_type, on_delete=models.CASCADE)
    job_field1 = models.ForeignKey(job_field, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    pay = models.IntegerField()
    pers_pictuare = models.FileField(upload_to="static/user_pers",blank=True,null=True)
    rez_picture = models.FileField(blank=True, null=True, upload_to="static/user_rez")

    def __str__(self):
        return (self.first_name + " " + self.last_name)


class company(models.Model):
    active = models.BooleanField(default=False)
    username=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=10)
    email=models.EmailField()
    date=models.DateField(auto_now_add=True)
    company_name=models.CharField(max_length=20)
    modir_name=models.CharField(max_length=20)
    id1=models.CharField(max_length=10)
    id_date=models.DateField()
    modirn=models.IntegerField()
    member_n=models.IntegerField()
    compane_type=models.ForeignKey(compane_type,on_delete=models.CASCADE)
    work_type=models.ForeignKey(worktype,on_delete=models.CASCADE)
    job_type=models.ForeignKey(job_type,on_delete=models.CASCADE)
    job_field=models.ForeignKey(job_field,on_delete=models.CASCADE)
    ostan=models.ForeignKey(ostan,on_delete=models.CASCADE)
    shahr=models.ForeignKey(shahr,on_delete=models.CASCADE)
    address=models.CharField(max_length=50)
    web=models.URLField(blank=True)
    logo_picture=models.FileField(upload_to="static/company_logo" )
    rez_picture=models.FileField(upload_to="static/company_rez")
    def __str__(self):
        return self.company_name


class agahi(models.Model):
    active=models.BooleanField(default=False)
    date=models.DateField(auto_now_add=True)
    time=models.DateTimeField(auto_now_add=True)
    company1=models.ForeignKey(company,on_delete=models.CASCADE,related_name='company')
    discriptation=models.CharField(max_length=250)