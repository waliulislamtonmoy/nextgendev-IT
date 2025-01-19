from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from App_Account.views import (
    UserRegisterView,
    SendOtpView,VeryfyOtpView,
    ResetPasswordView,
    UserProfileView,
    UserProfileUpdateView
)
urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("register/",UserRegisterView.as_view(),name='user_registration'),
    path("send-otp/",SendOtpView.as_view(),name="send-otp"),
    path("verify-otp/",VeryfyOtpView.as_view(),name="verify-otp"),
    path("reset-password/",ResetPasswordView.as_view(),name="reset-password"),
    path("user-profile/",UserProfileView.as_view(),name="user-profile"),
    path("update-profile/",UserProfileUpdateView.as_view(),name="update-profile"),
]
