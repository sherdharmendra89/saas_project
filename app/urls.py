# from django.urls import path
from .views import *
# # # from .views import UserRegistrationView, UserLoginView, UserProfileView, ChangePasswordView, SendPasswordResetEmailView, UserPasswordResetView
# # urlpatterns = [
# #     path('', test),
# #     # path('register/', UserRegistrationView.as_view()),
# #     # path('login/', UserLoginView.as_view()),
# #     # path('profile/', UserProfileView.as_view()),
# #     # path('changepassword/', ChangePasswordView.as_view()),

    
# #     # path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
# #     # path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
# # ]

# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', test),
    path('register/user/', views.UserRegistrationView.as_view(), name='user-registration'),
    path('register/company/', views.CompanyRegistrationView.as_view(), name='company-registration'),
    path('register/employee/', views.EmployeeRegistrationView.as_view(), name='employee-registration'),
    path("login/", views.UserLoginAPIView.as_view(), name="login-account"),
    
]

