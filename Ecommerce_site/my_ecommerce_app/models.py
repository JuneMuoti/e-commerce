from django.db import models
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

User=get_user_model()
#Image model class to hold all image details

class Category(models.Model):
    name=models.CharField(max_length=60)



    def __str__(self):
        return self.name

class Product(models.Model):
    title=models.CharField(max_length=60)
    description=models.TextField()
    product_image=models.ImageField(upload_to='images/',blank=True)
    category=models.ForeignKey(Category,null=True,blank=True)
    active=models.BooleanField()
    price = models.PositiveIntegerField(null=True)
    cart=models.ManyToManyField(User, blank=True, related_name='cart')
    @classmethod
    def search_by_category(cls,query):
        result = cls.objects.filter(category__name__icontains=query)
        return result

    def __str__(self):
        return self.title
    @classmethod
    def my_product(cls):
        products=Product.objects.all()

        return products

    def get_specific_product(self):
        return reverse("ecommerce:product", kwargs = {"id":self.id})

    def get_cart_url(self):
        return reverse("ecommerce:cart", kwargs = {"id":self.id})










    # @classmethod
    # def search_by_category(cls,query):
    #     result = cls.objects.filter(category__name__icontains=query)
    #     return result
    # def __str__(self):
    #     return self.name
    # @classmethod
    # def filter_by_location(cls):
    #     result = cls.objects.filter(location__location__icontains='canada')
    #     return result










# Create your models here.


# Create your models here.
