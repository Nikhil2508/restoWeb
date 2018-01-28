from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib import messages
from django.db.models.signals import post_save
# Create your models here.


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

class ProductManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self, *args, **kwargs):
        return self.get_queryset().active()

    def get_related(self, instance):
        products_one = self.get_queryset().filter(categories__in=instance.categories.all())
        products_two = self.get_queryset().filter(default=instance.default)
        qs = (products_one | products_two).exclude(id=instance.id).distinct()
        return qs

class Products(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    active = models.BooleanField(default=True)
    categories = models.ManyToManyField('Category', blank=True)
    default = models.ForeignKey('Category',related_name='default_category',null=True,blank=True)

    objects = ProductManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail",kwargs={"pk":self.pk})

    def get_image_url(self):
        img = self.productimage_set.first()
        if img:
            return img.image.url
        return img

class Variation(models.Model):
    product = models.ForeignKey(Products)
    title = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    sale_price = models.DecimalField(null=True, blank=True, max_digits=20, decimal_places=2)
    active = models.BooleanField(default=True)
    inventory = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.title

    def get_price(self):
        if self.sale_price is not None:
            return self.sale_price
        else:
            return self.price

    def get_absolute_url(self):
        return self.product.get_absolute_url()

    def add_to_cart(self):
        return "%s?item=%s&qty=1" %(reverse("cart"), self.id)

    def remove_from_cart(self):
        return "%s?item=%s&qty=1&delete=True" %(reverse("cart"), self.id)

    def get_title(self):
        return "%s - %s" %(self.product.title, self.title)

def product_post_saved_receiver(sender, instance, *args, **kwargs):
    product = instance
    variation = product.variation_set.all()
    if variation.count() == 0:
        new_variation = Variation()
        new_variation.product = product
        new_variation.price = product.price
        new_variation.title = "Default"
        new_variation.save()



post_save.connect(product_post_saved_receiver, sender=Products)



class ProductImage(models.Model):
    product = models.ForeignKey(Products)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.product.title



class Category(models.Model):
	title = models.CharField(max_length=120, unique=True)
	slug = models.SlugField(unique=True)
	description = models.TextField(null=True, blank=True)
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse("category_detail", kwargs={"slug": self.slug })

def image_upload_to_featured(instance, filename):
	title = instance.product.title
	slug = slugify(title)
	basename, file_extension = filename.split(".")
	new_filename = "%s-%s.%s" %(slug, instance.id, file_extension)
	return "products/%s/featured/%s" %(slug, new_filename)


class ProductFeatured(models.Model):
	product = models.ForeignKey(Products)
	image = models.ImageField(upload_to=image_upload_to_featured)
	title = models.CharField(max_length=120, null=True, blank=True)
	text = models.CharField(max_length=220, null=True, blank=True)
	text_right = models.BooleanField(default=False)
	text_css_color = models.CharField(max_length=6, null=True, blank=True)
	show_price = models.BooleanField(default=False)
	make_image_background = models.BooleanField(default=False)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.product.title
