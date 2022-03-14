from django.contrib import admin
from testapp.models import Student
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'rollno', 'name', 'age']


admin.site.register(Student, StudentAdmin)
