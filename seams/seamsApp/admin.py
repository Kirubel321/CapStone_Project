from datetime import timedelta, datetime

from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponseRedirect
from django.urls import path

from .models import Dept, Class, Student, Attendance, Course, Teacher, Assign, AssignTime, empAssignTime, AttendanceClass, StudentCourse, User, AttendanceRange, Employee, NotificationTeacher, NotificationStudent


# Register your models here.

days = {
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5,
    'Saturday': 6,
}

class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'user_name', 'ame')
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'name', 'is_active', 'is_staff', 'is_teacher', 'is_superuser','approved')
    filter = ('email', 'user_name', 'name','is_active', 'is_staff', 'is_teacher', 'is_superuser', 'approved')

    fieldsets = (
        (None, {
            "fields": (
                ('email', 'user_name', 'name')
            ),
        }),
        ('Permissions', {
            "fields": (
                ('is_active', 'is_staff', 'is_teacher',  'is_superuser', 'approved')
            ),
        }),
        ('Personal', {
            "fields": (
                ('gender', 'date_of_birth',)
            ),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('email', 'user_name', 'name', 'password1', 'password2', 'is_active', 'is_staff', 'is_teacher', 'is_superuser')
            }
        ),
    )



def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


class ClassInline(admin.TabularInline):
    model = Class
    extra = 0


class DeptAdmin(admin.ModelAdmin):
    inlines = [ClassInline]
    list_display = ('name', 'id')
    search_fields = ('name', 'id')
    ordering = ['name']


class StudentInline(admin.TabularInline):
    model = Student
    extra = 0


class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'dept', 'sem', 'section')
    search_fields = ('id', 'dept__name', 'sem', 'section')
    ordering = ['dept__name', 'sem', 'section']
    inlines = [StudentInline]


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'dept')
    search_fields = ('id', 'name', 'dept__name')
    ordering = ['dept', 'id']

class AssignTimeInline(admin.TabularInline):
    model = AssignTime
    extra = 0


class AssignAdmin(admin.ModelAdmin):
    inlines = [AssignTimeInline]
    list_display = ('class_id', 'course', 'teacher')
    search_fields = ('class_id__dept__name', 'class_id__id', 'course__name', 'teacher__name', 'course__shortname')
    ordering = ['class_id__dept__name', 'class_id__id', 'course__id']
    raw_id_fields = ['class_id', 'course', 'teacher']



# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('USN', 'user__name', 'class_id')
#     search_fields = ('USN', 'user__name', 'class_id__id', 'class_id__dept__name')
#     ordering = ['class_id__dept__name', 'class_id__id', 'USN']

# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user__name')
#     search_fields = ('id', 'user__name')
#     ordering = ['user__name','id']

# class TeacherAdmin(admin.ModelAdmin):
#     list_display = ('user__name', 'dept')
#     search_fields = ('user__name', 'dept__name')
#     ordering = ['dept__name', 'user__name']

class StudentAdmin(admin.ModelAdmin):
    list_display = ('USN', 'class_id')
    search_fields = ('USN', 'class_id__id', 'class_id__dept__name')
    ordering = ['class_id__dept__name', 'class_id__id', 'USN']



admin.site.register(User, UserAdminConfig)
admin.site.register(Dept, DeptAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Teacher)
admin.site.register(Assign, AssignAdmin)
admin.site.register(Employee)
admin.site.register(NotificationTeacher)
admin.site.register(NotificationStudent)
