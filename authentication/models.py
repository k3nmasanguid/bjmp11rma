from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('You must provide an email address')

        user = self.model(
            email = self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,password):
        user = self.create_user(email=self.normalize_email(email),password=password)
        user.is_admin = True
        user.is_staff = True 
        user.is_superuser = True 
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    APPLICATION_STATUS = (
        ('Complete', 'Complete'),
        ('For Submission', 'For Submission'),
        ('Pending', 'Pending'),
    )

    email = models.EmailField(verbose_name='Email', max_length=100, unique=True)
    date_joined = models.DateTimeField(verbose_name='Date joined', auto_now_add = True)
    last_login = models.DateTimeField(verbose_name='Last login', auto_now = True)

    status = models.CharField('Application Status', max_length=20, default='Pending' ,choices=APPLICATION_STATUS)

    batch = models.ManyToManyField(to='rma.Quota')

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserAccountManager()

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email


