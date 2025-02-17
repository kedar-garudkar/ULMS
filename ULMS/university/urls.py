from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView
from university.authentication.auth_views import RegisterView, LoginView, LogoutView#, PasswordResetRequestView, PasswordResetConfirmView

# 📌 Create Router
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'professors', ProfessorViewSet)
router.register(r'offices', OfficeViewSet)
router.register(r'students', StudentViewSet)
router.register(r'student_profiles', StudentProfileViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'course_schedule', CourseScheduleViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'libraries', LibraryViewSet)
router.register(r'books', BookViewSet)
router.register(r'borrowed_books', BorrowedBookViewSet)
router.register(r'book_reservations', BookReservationViewSet)
router.register(r'fines', FineViewSet)
router.register(r'library_memberships', LibraryMembershipViewSet)
router.register(r'notifications', NotificationViewSet)

# 📌 Define URL Patterns
urlpatterns = [
    path('api/', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('password-reset/', PasswordResetRequestView.as_view(), name='password_reset'),
    # path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
