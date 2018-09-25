from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.utils.text import slugify


USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'
NAME_REGEX = '^[a-zA-Z]*$'



from django.urls import reverse

class Galerie(models.Model):

		image = models.ImageField(null=True, 
		                            blank=True,default='img/default.png',
		                            height_field="height_field", 
		                            width_field="width_field",
		                            verbose_name="profile annonce "
		                            )
		height_field = models.IntegerField(default=600, null=True)
		width_field = models.IntegerField(default=600, null=True)





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
	lieuaproximité   =models.FileField(blank=True)
	slug             =models.SlugField(unique=True)
	phone            =models.PositiveIntegerField()
	image            =models.ForeignKey(Galerie,on_delete=models.CASCADE,related_name='images',null=True)

	tiping           =(('lo','Location'),('ve','vente'),)

	typeannonce      =models.CharField(max_length=10,choices=tiping)
	choiceville      =(('ca',"casablance"),("r","rabat"),)
	ville            =models.CharField(max_length=200,choices=choiceville)
	cat  = (('app','appartement'),('vi','villa'),)

	categorie        =models.CharField(max_length=200,choices=cat)
       



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


