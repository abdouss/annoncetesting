from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Category(models.Model):

		name = models.CharField(max_length=128, unique=True, verbose_name="category")
		slug = models.SlugField(unique=True)

		def __str__(self):
		    return self.name


class Galerie(models.Model):

		image = models.ImageField(null=True, 
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

	nom              =models.CharField(max_length=128,blank=True,null=True)
	prix             =models.CharField(max_length=200,blank=True,null=True)
	description      =models.TextField(blank=True,null=True)
	created          =models.DateTimeField(auto_now_add=True)
	caractéristiques =models.TextField(blank=True,null=True)
	lieuaproximité   =models.FileField()
	slug             =models.SlugField(unique=True)
	category         =models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categorys')
	image            =models.ForeignKey(Galerie,on_delete=models.CASCADE,related_name='images')
	ville            =models.ForeignKey(Ville,on_delete=models.CASCADE,related_name='villes')

	tiping = (
        ('Location'),
        ('vente'),
       
    )

	type = models.CharField(max_length=10,choices=tiping)



	def get_absolute_url(self):
		return reverse("annoncedetail",kwargs={'slug':self.slug}) 

	def __str__(self):
		return self.title


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


