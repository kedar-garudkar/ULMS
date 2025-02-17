from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
# from django.contrib.auth.tokens import default_token_generator
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes, force_str
# from django.core.mail import send_mail
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from university.authentication.auth_serializers import RegisterSerializer, LoginSerializer

User = get_user_model()

# ==========================
# User Registration API View
# ==========================
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

# ==========================
# User Login API View
# ==========================
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # print('Login successfully')
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    
# ==========================
# User Logout API View
# ==========================
class LogoutView(APIView):
    authentication_classes = []  # ✅ Disable authentication requirement for this endpoint
    permission_classes = []  # ✅ No permissions required

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")  # ✅ Extract refresh token
            if not refresh_token:
                return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()  # ✅ Blacklist the refresh token

            return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

# ==========================
# Password Reset Request API
# ==========================
# class PasswordResetRequestView(generics.GenericAPIView):
#     def post(self, request):
#         email = request.data.get('email')
#         user = User.objects.filter(email=email).first()
#         if user:
#             token = default_token_generator.make_token(user)
#             uid = urlsafe_base64_encode(force_bytes(user.pk))
#             reset_link = f"http://yourfrontend.com/reset-password/{uid}/{token}/"
#             send_mail(
#                 "Password Reset Request",
#                 f"Click the link to reset your password: {reset_link}",
#                 "noreply@yourdomain.com",
#                 [email],
#                 fail_silently=False,
#             )
#         return Response({"message": "If this email exists, a password reset link has been sent."}, status=200)

# ==========================
# Password Reset Confirm API
# ==========================
# class PasswordResetConfirmView(generics.GenericAPIView):
#     def post(self, request, uidb64, token):
#         try:
#             uid = force_str(urlsafe_base64_decode(uidb64))
#             user = User.objects.get(pk=uid)
#             if default_token_generator.check_token(user, token):
#                 user.set_password(request.data['new_password'])
#                 user.save()
#                 return Response({"message": "Password reset successful"}, status=200)
#         except:
#             return Response({"error": "Invalid or expired token"}, status=400)
