from django.contrib import admin
from .models import *
# Register your models here.



# Register Models in Admin Panel
admin.site.register(User)
admin.site.register(UserRole)
admin.site.register(Department)
admin.site.register(Professor)
admin.site.register(Office)
admin.site.register(Student)
admin.site.register(StudentProfile)
admin.site.register(Course)
admin.site.register(CourseSchedule)
admin.site.register(Enrollment)
admin.site.register(Grade)
admin.site.register(Attendance)
admin.site.register(Library)
admin.site.register(Book)
admin.site.register(BorrowedBook)
admin.site.register(BookReservation)
admin.site.register(Fine)
admin.site.register(LibraryMembership)
admin.site.register(Notification)
