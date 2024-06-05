from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()

class UserSignUpSerializer(serializers.ModelSerializer):
    password1=serializers.CharField(write_only=True)
    password2=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=('phone_number', 'email','username', 'name', 'password1', 'password2')

    def validate(self, attrs):
        password1=attrs.get('password1')
        password2=attrs.get('password2')
        if password1!=password2:
            raise serializers.ValidationError("Passwords don't match")
        return attrs

    def create(self, validated_data):
        user=User.objects.create_user(phone_number=validated_data['phone_number'], 
                                      email=validated_data['email'],
                                      username=validated_data['username'],
                                      name=validated_data['name'],
                                      password=validated_data['password1']
                                      )
        return user
    



class UserSignInSerializer(serializers.Serializer):
  phone_number=serializers.CharField()
  password=serializers.CharField()

  def validate(self, attrs):
    phone_number=attrs.get('phone_number')
    password=attrs.get('password')
    user=User.objects.filter(phone_number=phone_number).first()
    if not user or not user.check_password(password):
      raise serializers.ValidationError("Invalid credentials")
    return attrs

  def create(self, validated_data):
    user = User.objects.get(phone_number=validated_data['phone_number'])
    refresh = RefreshToken.for_user(user)
    return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
    }
