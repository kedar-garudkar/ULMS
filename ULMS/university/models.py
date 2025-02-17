from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.


# 👥 User Roles Table
class UserRole(models.Model):
    ROLE_CHOICES = [
        ('Student', 'Student'),
        ('Professor', 'Professor'),
        ('Librarian', 'Librarian'),
        ('Admin', 'Admin'),
    ]
    role_name = models.CharField(max_length=20, choices=ROLE_CHOICES, unique=True)

    def __str__(self):
        return self.role_name

# # 👤 Custom User Model
# class User(AbstractUser):
#     role = models.ForeignKey(UserRole, on_delete=models.SET_NULL, null=True)
#     email = models.EmailField(unique=True)

#     def __str__(self):
#         return self.username

class User(AbstractUser):
    role = models.ForeignKey('UserRole', on_delete=models.SET_NULL, null=True, blank=True)
    
    # Add unique related_name values to avoid conflicts with Django's auth system
    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

    def __str__(self):
        return self.username

# 🏛️ Departments Table
class Department(models.Model):
    department_name = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name

# 🏫 Professors Table
class Professor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

# 🏢 Offices Table (One-to-One with Professors)
class Office(models.Model):
    professor = models.OneToOneField(Professor, on_delete=models.CASCADE)
    office_number = models.CharField(max_length=20, unique=True)
    building = models.CharField(max_length=100)

    def __str__(self):
        return f"Office {self.office_number} - {self.professor.name}"

# 🎓 Students Table
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

# 📄 StudentProfiles Table (One-to-One with Students)
class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"Profile of {self.student.name}"

# 📚 Courses Table
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.course_name

# 📅 Course Schedule Table
class CourseSchedule(models.Model):
    DAYS = [
        ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday'),
    ]
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10, choices=DAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.course.course_name} on {self.day_of_week}"

# 🎓📚 Enrollments Table (Many-to-Many)
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.course_name}"

# 📊 Grades Table
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.student.name} - {self.course.course_name}: {self.grade}"

# ✅ Attendance Table
class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.student.name} - {self.course.course_name} - {self.status}"

# 📖 Library Table
class Library(models.Model):
    library_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.library_name

# 📕 Books Table
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# 🎓📖 BorrowedBooks Table (Many-to-Many)
class BorrowedBook(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.name} borrowed {self.book.title}"

# 🏷️ Book Reservations Table
class BookReservation(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reservation_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.student.name} reserved {self.book.title}"

# 💰 Fines Table
class Fine(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Fine for {self.student.name}: {self.amount}"

# 💳 Library Membership Table
class LibraryMembership(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Library Membership for {self.student.name}"

# 🔔 Notifications Table
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}"
