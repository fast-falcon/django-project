from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from app.models import marry, sex, madrak, education, ostan, shahr, job, job_type, job_field, compane_type, worktype, \
    worcker, company, agahi


@admin.register(agahi)
class adminagahi(ModelAdmin):
    list_display = ('company1','discriptation','active','date','time')

@admin.register(marry)
class Marryadmin(ModelAdmin):
    list_display=('name',)

@admin.register(sex)
class sexadmin(ModelAdmin):
    list_display=('name',)

@admin.register(madrak)
class madrakadmin(ModelAdmin):
    list_display=('name',)

@admin.register(education)
class eduadmin(ModelAdmin):
    list_display=('name',)

@admin.register(ostan)
class ostanadmin(ModelAdmin):
    list_display=('name',)

@admin.register(shahr)
class shahradmin(ModelAdmin):
    list_display=('name',)

@admin.register(job)
class jobadmin(ModelAdmin):
    list_display=('name',)

@admin.register(job_type)
class job_typeadmin(ModelAdmin):
    list_display=('name',)

@admin.register(job_field)
class job_fieldadmin(ModelAdmin):
    list_display=('name',)

@admin.register(compane_type)
class company_typeadmin(ModelAdmin):
    list_display=('name',)


@admin.register(worktype)
class worktypeadmin(ModelAdmin):
    list_display=('name',)

@admin.register(worcker)
class worckeradmin(ModelAdmin):
    list_display=('username','password','email','date','active','first_name')

@admin.register(company)
class companyadmin(ModelAdmin):
    list_display=('username',)

