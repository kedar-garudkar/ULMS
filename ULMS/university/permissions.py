from rest_framework import permissions

# ==========================
# IsAdminOrReadOnly Permission
# ==========================
class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Allows full access to admins and read-only access to others.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True  # Allow GET requests for all
        return request.user.is_staff  # Allow only admins to modify

# ==========================
# IsProfessor Permission
# ==========================
class IsProfessor(permissions.BasePermission):
    """
    Allows access only to users who are professors.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'Professor'

# ==========================
# IsStudent Permission
# ==========================
class IsStudent(permissions.BasePermission):
    """
    Allows access only to students.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'Student'

# ==========================
# IsLibrarian Permission
# ==========================
class IsLibrarian(permissions.BasePermission):
    """
    Allows access only to users who are Librarians.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'Librarian'