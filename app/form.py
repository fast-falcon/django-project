from django import forms
from django.contrib.auth import authenticate

from app import models
from app.models import worcker, shahr, agahi, company



class Worcker(forms.ModelForm):

    class Meta:
        model = worcker
        # 'user.username', 'user.password', 'user.first_name', 'user.last_name', 'user.email'
        fields= ['active', 'username','password','first_name','last_name','email','id1', 'sex1',
                 'marry_type1', 'birthday', 'mobile', 'phone', 'madrak1',
                 'education', 'ostan1', 'shahr1', 'exprience1',
                 'job1', 'job_field1', 'job_type1', 'address',
                 'pay', 'pers_pictuare', 'rez_picture']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.password=forms.CharField(max_length=20,widget=forms.PasswordInput)








class Company(forms.ModelForm):
    class Meta:
        model = company
        fields=('active','username','password','company_name','modir_name','email','id1','id_date','modirn',
                'member_n','compane_type','work_type','job_type',
                'job_field','ostan','shahr','address','web','logo_picture','rez_picture')

class Agahi(forms.ModelForm):
    class Meta:
        model=agahi
        fields=('company1','discriptation')
