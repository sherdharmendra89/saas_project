# from rest_framework import serializers
# from .models import User

# class UserRegistrationSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
#     class Meta:
#         model = User
#         fields = ['email', 'name', 'password', 'password2', 'tc']

#         extra_kwargs={
#             'password':{'write_only':True}
#         }

#     def validate(self, data):
#         passwrod = data.get('password')
#         passwrod2 = data.get('password2')
#         if passwrod != passwrod2:
#             raise serializers.ValidationError("Password and Confirm Password doesn't match")
#         return data
    
#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)
    

# class UserLoginSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField()
#     class Meta:
#         model = User
#         fields = ['email', 'password']

# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'email', 'name']

    
# class ChangePasswordSerializer(serializers.Serializer):
#     password = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)
#     password2 = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)

#     def validate(self, attrs):
#         password = attrs.get('password')
#         password2 = attrs.get('password2')
#         user = self.context.get('user')

#         if password != password2:
#             raise serializers.ValidationError("Password and Confirm Password do not match.")
#         user.set_password(password)
#         user.save()
#         return attrs


#     def save(self):
#         user = self.context.get('user')
#         password = self.validated_data['password']
        
#         return user


# from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
# from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from app.utils import Util


# class SendPasswordResetEmailSerializer(serializers.Serializer):
#     email = serializers.EmailField(max_length=255)

#     class Meta:
#         fields = ['email']

#     def validate(self, attrs):
#         email = attrs.get('email')
#         if User.objects.filter(email=email).exists():
#             user = User.objects.get(email=email)
#             uid = urlsafe_base64_encode(force_bytes(user.id))
#             print('Encoded UID', uid)
#             token = PasswordResetTokenGenerator().make_token(user)
#             print('Password Reset Token', token)
#             link = 'http://localhost:3000/api/user/reset/'+uid+'/'+token
#             print('Password Reset Link', link)
           
#             # Send Email

#             body = 'Click following link to reset your password' + link
#             data = {
#                    'subject': "Reset Your Password",
#                    'body': body,
#                    'to_email':user.email
#             }
#             Util.send_email(data)
#             return attrs
#         else:
#             raise serializers.ValidationError('You are not a Registered User')


# class UserPasswordResetSerializer(serializers.Serializer):
#     password = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)
#     password2 = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)

#     class Meta:
#         fields = ['password', 'password2']

#     def validate(self, attrs):
#         try:
#             password = attrs.get('password')
#             password2 = attrs.get('password2')
#             uid = self.context.get('uid')
#             token = self.context.get('token')
#             if password != password2:
#                 raise serializers.ValidationError("Password and Confirm Password doesn't match")
#             id = smart_str(urlsafe_base64_decode(uid))
#             user = User.objects.get(id=id)
#             if PasswordResetTokenGenerator().check_token(user, token):
#                 raise serializers.ValidationError('Token is not Valid or Expired')
#             user.set_password(password)
#             user.save()
#             return attrs
#         except DjangoUnicodeDecodeError as identifier:
#             PasswordResetTokenGenerator().check_token(user, token)
#             raise serializers.ValidationError('Token is not Valid or Expired')


# serializers.py
# serializers.py

from rest_framework import serializers
from .models import User, CustomGroup, CustomPermission
from company.models import Company
from employee.models import Employee

class CustomGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomGroup
        fields = '__all__'

class CustomPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomPermission
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password"]

from django.contrib.auth import authenticate

class UserLoginSerializer(serializers.Serializer):
    """
    Serializer class to authenticate users with username and password.
    """

    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    user = serializers.SerializerMethodField(read_only=True)

    

    def validate(self, data):
        user = authenticate(**data)
        print(user.username,"....")
        print(user.content_object.__class__.__name__,"....")

        if user and user.is_active:
            return user
        
        raise serializers.ValidationError("Incorrect Credentials")        
    
    def get_user(self, obj): 
        print(obj,"...")
        return CustomUserSerializer(obj).data