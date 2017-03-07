from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    """
        create a new user

        @param username:  the name for the new user
        @param password:  the password for the new user. if none is provided a random password is generated
        @param person:    the corresponding person object for this user
    """
    def create_user(self,email,firstname,lastname,password):
        """
               Creates and saves a User with the given email, date of
               birth and password.
               """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            firstname=firstname,
            lastname=lastname
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,firstname, lastname, password=None):

        user = self.create_user(
            email,
            password=password,
            firstname=firstname,
            lastname=lastname
        )

        user.is_admin = True


        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    """
    Custom user class.
    """
    email = models.EmailField('email address', unique=True, db_index=True)
    firstname = models.CharField('first name',max_length=20)
    lastname = models.CharField('last name',max_length=20)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)



    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin





