# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, ChangePasswordSerializer, SendPasswordResetEmailSerializer
# from rest_framework import status
# from django.contrib.auth import authenticate

# from sendemail import send_registraion_email

# # for generation token

# from rest_framework_simplejwt.tokens import RefreshToken

# def get_tokens_for_user(user):
#     refresh = RefreshToken.for_user(user)

#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }

# class UserRegistrationView(APIView):

#     def post(self, request):
#         serializers = UserRegistrationSerializer(data=request.data)
#         if serializers.is_valid(raise_exception=True):
#             user = serializers.save()
#             token = get_tokens_for_user(user)
#             # send_registraion_email(user.email)
#             return Response({"token": token, "msg": "registration successful"}, status=status.HTTP_201_CREATED)
#         return Response({"errormsg": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)
    
# class UserLoginView(APIView):
#     def post(self, request):
#         serializers = UserLoginSerializer(data=request.data)
#         if serializers.is_valid(raise_exception=True):
#             email = serializers.data.get('email')
#             password = serializers.data.get('password')
#             user = authenticate(email=email, password=password)
#             if user is not None:
#                 token = get_tokens_for_user(user)
#                 return Response({'token': token, "msg": "User Login Successfull"}, status=status.HTTP_200_OK)
#             else:
#                 return Response({"nontype_error": "Email and Password are wrong"}, status=status.HTTP_400_BAD_REQUEST)

# from .models import User
# from rest_framework.permissions import IsAuthenticated
# from .serializers import UserPasswordResetSerializer


# class UserProfileView(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self, request, format=None):
#         serializers = UserProfileSerializer(request.user)
#         return Response(serializers.data, status=status.HTTP_200_OK)
    

# class ChangePasswordView(APIView):
#     permission_classes = [IsAuthenticated]
#     def post(self, request, format=None):
#         serializers = ChangePasswordSerializer(data=request.data, context={'user':request.user})
#         if serializers.is_valid(raise_exception=True):
#             return Response({'msg': "Password has been changed successfully"}, status=status.HTTP_202_ACCEPTED)
#         else:
#             return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


# class SendPasswordResetEmailView(APIView):
#   def post(self, request, format=None):
#     serializer = SendPasswordResetEmailSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     return Response({'msg':'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)

# class UserPasswordResetView(APIView):
#     def post(self, request, uid, token, format=None):
#         serializers = UserPasswordResetSerializer(data=request.data, context={'uid': uid, 'token':token})
#         if serializers.is_valid(raise_exception=True):
#             return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK) 
def test(self):
    pass

# views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from .models import User
from company.models import Company
from .serializers import UserSerializer, CompanySerializer



# views.py
from rest_framework import generics, status
from .models import User
from company.models import Company
from employee.models import Employee
from .serializers import UserSerializer, CompanySerializer, EmployeeSerializer
from .permissions import IsSuperUser, IsCompanyUser, IsEmployeeUser

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUser]

class CompanyRegistrationView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsSuperUser]

class EmployeeRegistrationView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsCompanyUser]



from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
# from account.utils import JWTAuthentication

from . import serializers
from django.shortcuts import render

User = get_user_model()

class UserLoginAPIView(GenericAPIView):
    """
    An endpoint to authenticate existing users using their email and password.
    """
    # authentication_classes = (JWTAuthentication,)
    permission_classes = (AllowAny,)
    serializer_class = serializers.UserLoginSerializer
    

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh":str(token), "access":str(token.access_token)}
        
        

        if user:
            device_ip = request.META.get('REMOTE_ADDR')
            # import pdb;pdb.set_trace()
            user.last_login_ip = device_ip
            user.save()
            
            return Response(data, status=status.HTTP_200_OK)

