from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances
from django.contrib.auth.models import User
from datetime import datetime
from .choices import *

# Create your models here.

#model:mt_users
class mt_users(models.Model):

#mt_users.fields
	f_user_id = models.IntegerField(default = 0, unique = True)
	f_user_name = models.CharField(max_length=100, default = "username", unique = True)
	f_verification_status = models.BooleanField(default=False)
	f_creation_time = models.DateTimeField(default = datetime.now)
	f_verification_time = models.DateTimeField(default = datetime.now)
	f_id_type = models.CharField(max_length=100, default = "idt")
	f_id_number = models.CharField(max_length=1000, default = "idn")
	f_nationality = models.CharField(max_length=100, default = "country")
	f_email_id = models.CharField(max_length=1000, default = "email", unique = False)
	f_contact_number = models.CharField(max_length=100, default = "contact")
	
#mt_users.end_fields
	
#mt_users.meta
	class Meta: 
		ordering = ['f_user_id']

#mt_users.methods
	def get_absolute_url(self):
		 return reverse('mt_users', args=[str(self.id)])

	def __str__(self):
		return str(self.f_user_id)

#model:mt_transactions
class mt_transactions(models.Model):

#mt_transactions.fields
	f_trans_id = models.IntegerField(default = 0, unique = True)
	f_user_id1 = models.IntegerField(default = 0)
	f_user_id2 = models.IntegerField(default = 0)
	f_status = models.CharField(max_length=1, default = "c")
	f_creation_time_a = models.DateTimeField(default = datetime.now)
	f_creation_time_b = models.DateTimeField(default = datetime.now)
	f_approval_time_h = models.DateTimeField(default = datetime.now)
	f_approval_time_x = models.DateTimeField(default = datetime.now)
	f_ft_type = models.CharField(choices=TRANS_TYPE_CHOICES, max_length=1, default = "x")
	f_ft_id = models.IntegerField(default = 0)
	f_ft_quantity_unit = models.CharField(choices=QUANTITY_UNIT_CHOICES, max_length=2, default = "xx")
	f_ft_quantity_number = models.IntegerField(default = 0)
	f_ft_category = models.CharField(max_length=100, default = "category")
	f_ft_description = models.CharField(max_length=1000, default = "description")
	f_pt_type = models.CharField(choices=TRANS_TYPE_CHOICES, max_length=1, default = "x")
	f_pt_id = models.IntegerField(default = 0)
	f_pt_quantity_unit = models.CharField(choices=QUANTITY_UNIT_CHOICES, max_length=2, default = "xx")
	f_pt_quantity_number = models.IntegerField(default = 0)
	f_pt_category = models.CharField(max_length=100, default = "category")
	f_pt_description = models.CharField(max_length=1000, default = "description")
	f_hash_pk = models.CharField(max_length=1000, default = "pk")
	f_hash_u1 = models.CharField(max_length=1000, default = "u1")
	f_hash_u2 = models.CharField(max_length=1000, default = "u2")
	
#mt_transactions.end_fields
	
#mt_transactions.meta
	class Meta: 
		ordering = ['f_trans_id']

#mt_transactions.methods
	def get_absolute_url(self):
		 return reverse('mt_transactions', args=[str(self.id)])

	def __str__(self):
		return str(self.f_trans_id)

#model:mt_products
class mt_products(models.Model):

#mt_products.fields
	f_product_id = models.IntegerField(default = 0, unique = True)
	f_product_name = models.CharField(max_length=100, default = "prodname")
	f_quantity_unit = models.CharField(max_length=100, default = "unit")
	f_creation_time = models.DateTimeField(default = datetime.now)
	f_product_category = models.CharField(max_length=100, default = "category")
	f_product_description = models.CharField(max_length=1000, default = "description")
	f_product_images_link = models.CharField(max_length=1000, default = "images")
	f_product_video_link = models.CharField(max_length=1000, default = "video")
	f_product_dimension_units = models.CharField(max_length=100, default = "category")
	f_product_dimension_height = models.IntegerField(default = 0)
	f_product_dimension_width = models.IntegerField(default = 0)
	f_product_dimension_depth = models.IntegerField(default = 0)
	
#mt_products.end_fields
	
#mt_products.meta
	class Meta: 
		ordering = ['f_product_id']

#mt_products.methods
	def get_absolute_url(self):
		 return reverse('mt_products', args=[str(self.id)])

	def __str__(self):
		return str(self.f_product_id)

#model:mt_services
class mt_services(models.Model):

#mt_services.fields
	f_service_id = models.IntegerField(default = 0, unique = True)
	f_service_name = models.CharField(max_length=100, default = "servname")
	f_duration_unit = models.CharField(max_length=100, default = "unit")
	f_creation_time = models.DateTimeField(default = datetime.now)
	f_service_category = models.CharField(max_length=100, default = "category")
	f_service_description = models.CharField(max_length=1000, default = "description")
	
#mt_services.end_fields
	
#mt_services.meta
	class Meta: 
		ordering = ['f_service_id']

#mt_services.methods
	def get_absolute_url(self):
		 return reverse('mt_services', args=[str(self.id)])

	def __str__(self):
		return str(self.f_service_id)

#model:mt_access
class mt_access(models.Model):

#mt_access.fields
	f_mt_name = models.CharField(max_length=100, default = "mt")
	f_access_status = models.BooleanField(default=False)
	
#mt_access.end_fields
	
#mt_access.meta
	class Meta: 
		ordering = ['f_mt_name']

#mt_access.methods
	def get_absolute_url(self):
		 return reverse('mt_access', args=[str(self.id)])

	def __str__(self):
		return str(self.f_mt_name)