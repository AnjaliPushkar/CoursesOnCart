from django.db import models

# Create your models here.


class Blog(models.Model):
    img = models.ImageField(upload_to ='shop/images', default="")
    title = models.CharField(max_length = 200)
    pub_date = models.DateField()
    desc = models.CharField(max_length = 3000)
    author = models.CharField(max_length = 50, default="")
    def __str(self):
        return self.title

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default="")
    Organization = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=1500)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")
    link = models.URLField(max_length=250, default="")

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('product', kwargs={'pk': self.pk})
