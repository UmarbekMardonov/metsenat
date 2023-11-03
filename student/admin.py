from django.contrib import admin

from .models import Student, StudentSponsor, University


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'university_name', 'required_amount', 'payed_amount')


@admin.register(StudentSponsor)
class StuSpoAdmin(admin.ModelAdmin):
    list_display = ('id', 'sponsor_user', 'student_user', 'amount')


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

