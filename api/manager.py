from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password, name, is_superuser = False, is_staff = False):
        email = self.normalize_email(email=email)
        user = self.model(
            email = email,
            name = name,
            is_superuser = is_superuser,
            is_staff = is_staff
        )
        
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password, name="name", is_superuser=True, is_staff=True)
        user.save()
        return user