from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
	use_in_migrations = True

	def _create_user(self, email, password, **extra_fields):
		if not email:
			raise ValueError('Email missing')

		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_new_user(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_staff', True)

		if extra_fields.get('is_superuser') is not True:
			raise ValueError('It is not super user')

		return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(_('Email address'), unique=True)
	first_name = models.CharField(_('First name'), max_length=30, blank=True)
	last_name = models.CharField(_('Last name'), max_length=30, blank=True)
	is_active = models.BooleanField(_('Active'), default=True)
	is_staff = models.BooleanField(_('Is Staff'), default=False)

	objects = UserManager()
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	class Meta:
		verbose_name = _('user')
		verbose_name_plural = _('users')
		