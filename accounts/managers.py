from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, phone_number, username,name, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("Phone number is required")

        if not username:
            raise ValueError("Username is required")
        if not name:
            raise ValueError("Name is required")

        extra_fields['email']=self.normalize_email(extra_fields['email'])
        user=self.model(phone_number=phone_number,
                        username=username,
                        name=name,
                        **extra_fields
                        )
        user.set_password(password)
        user.save(using=self.db)
        return user


    def create_superuser(self, phone_number,username,name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(("Superuser must have is_staff=True"))
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(("Superuser must have is_superuser=True"))
        
        return  self.create_user(phone_number,username,name, password, **extra_fields)
