from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'
NAME_REGEX = '^[a-zA-Z]*$'

class Category(models.Model):

		name = models.CharField(max_length=128, unique=True, verbose_name="category",validators=[
                                        RegexValidator(
                                        regex = USERNAME_REGEX,
                                        message = 'Username must be Alpahnumeric or contain any of the following: ".+ -" ',
                                        code='invalid_username'
                                        )])
		slug = models.SlugField(unique=True)

		def __str__(self):
		    return self.name

from django.urls import reverse

class Galerie(models.Model):

		image = models.ImageField(upload_to='images',null=True, 
		                            blank=True, 
		                            height_field="height_field", 
		                            width_field="width_field",
		                            verbose_name="profile annonce "
		                            )
		height_field = models.IntegerField(default=600, null=True)
		width_field = models.IntegerField(default=600, null=True)


class Ville(models.Model):

		name =models.CharField(max_length=128,blank=True,null=True)

		def __str__(self):
			return self.name




class Annonce(models.Model):

	nom              =models.CharField(max_length=128,blank=True,null=True,validators=[
                                        RegexValidator(
                                        regex = USERNAME_REGEX,
                                        message = 'Username must be Alpahnumeric or contain any of the following: ".+ -" ',
                                        code='invalid_username'
                                        )])
	prix             =models.CharField(max_length=200,blank=True,null=True)
	description      =models.TextField(blank=True,null=True)
	created          =models.DateTimeField(auto_now_add=True)
	caractéristiques =models.TextField(blank=True,null=True)
	lieuaproximité   =models.FileField(blank=True, upload_to='images')
	slug             =models.SlugField(unique=True)
	phone            =models.PositiveIntegerField()
	category         =models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categorys')
	image            =models.ForeignKey(Galerie,on_delete=models.CASCADE,related_name='images')
	ville            =models.ForeignKey(Ville,on_delete=models.CASCADE,related_name='villes')

	tiping = (
        ('location','Location'),
        ('vente','vente'),
       
    )

	typeannonce            =models.CharField(max_length=10,choices=tiping)



	def get_absolute_url(self):
		return reverse("detailannonce",kwargs={'slug':self.slug}) 

	def __str__(self):
		return self.nom


	class Meta:
		ordering = ['-created']

	def _get_unique_slug(self):
	    slug = slugify(self.nom)
	    unique_slug = slug
	    num = 1
	    while Annonce.objects.filter(slug=unique_slug).exists():
	        unique_slug = '{}-{}'.format(slug, num)
	        num += 1
	    return unique_slug

	def save(self, *args, **kwargs):
	    if not self.slug:
	        self.slug = self._get_unique_slug()
	    super(Annonce, self).save()


