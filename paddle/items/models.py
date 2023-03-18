from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
	name = models.CharField(max_length=255)


	class Mete:
		ordering = ('name',)
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name


class Item(models.Model):
	category=models.ForeignKey(Category, related_name='items',on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	price = models.DecimalField(max_digits=9, decimal_places=2)
	image = models.ImageField(upload_to='item_images',blank=True,null=True)
	is_sold = models.BooleanField(default=False)
	created_by = models.ForeignKey(User, related_name='items',on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name





# Create your models here.
