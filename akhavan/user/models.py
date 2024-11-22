from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField

class CUserManager(BaseUserManager):
	def create_user(self, phone_num, first_name, last_name, password=None):
		if not password:
			raise ValueError("PLEASE ENTER AN PASSWORD")
		if not phone_num:
			raise ValueError("Users must have an PHONE NUMBER")
		if not first_name:
			raise ValueError("Users must have a first name")
		if not last_name:
			raise ValueError("Users must have a last name")

		user = self.model(
			phone_num=phone_num,
			first_name=first_name,
			last_name=last_name
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, phone_num, first_name, last_name, password=None):
		user = self.create_user(
			password=password,
			phone_num=phone_num,
			first_name=first_name,
			last_name=last_name
		)
		user.is_staff = True
		user.is_admin = True
		user.save(using=self._db)
		return user

class CUser(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True, max_length=255)
	phone_num = PhoneNumberField(unique=True, blank=False, null=False)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)

	objects = CUserManager()

	USERNAME_FIELD = "phone_num"
	REQUIRED_FIELDS = ['first_name', 'last_name']

	def __str__(self) -> str:
		return str(self.phone_num)
	def has_perm(self, perm, obj=None):
		if self.is_admin:
			return True
		return super().has_perm(perm, obj)

	def has_module_perms(self, app_label):
		if self.is_admin:
			return True
		return super().has_module_perms(app_label)
	
	class Meta:
		ordering = ('-id',)


class Address(models.Model):
	user = models.ForeignKey(CUser, on_delete=models.CASCADE)
	title = models.CharField(max_length=255, blank=True)
	description = models.TextField(max_length=500)
	number = models.CharField(max_length=5)
	code = models.CharField(max_length=20)

	objects = CUserManager()

	def __str__(self):
		if self.title:
			return self.title
		return self.description