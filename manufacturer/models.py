from django.db import models
#this shop
class Manufacturer(models.Model):
    lon = models.FloatField(blank=True,null=True)
    lat = models.FloatField(blank=True,null=True)
    manufacturer_name = models.CharField(max_length=200)
    locale = models.CharField(max_length=250,blank=True,null=True)
    number = models.IntegerField(blank=True,null=True)    
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True)    
    shop_image =models.ImageField(upload_to='media/retailer/', blank=True)
    #ip address they used to shop
    ip_address = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    date_joined = models.DateTimeField(auto_now_add=False)

    #items in this this shop
class Product(models.Model):
    item_brand = models.CharField(max_length=200,blank=True,null=True)
    item_type =models.CharField(max_length=200,blank=True,null=True)
    item_product_line = models.CharField(max_length=200,blank=True,null=True) 
    item_id = models.CharField(max_length=100,blank=True,null=True)
    item_price = models.DecimalField(max_digits=9, decimal_places=6,blank=True,null=True)
    stock = models.PositiveIntegerField()
    item_quality = models.CharField(max_length=100,blank=True,null=True)
    manufacture = models.CharField(max_length=200,blank=True,null=True)
    available = models.BooleanField(default=True)
    item_image = models.ImageField(upload_to='media/products/', blank=True)
  #where item in this this shop was bought
class CustomerProducer(models.Model):
    customer_producer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    producer_name = models.CharField(max_length=200)
    item_brand = models.CharField(max_length=200,blank=True,null=True)
    item_type =models.CharField(max_length=200,blank=True,null=True)
    item_product_line = models.CharField(max_length=200,blank=True,null=True) 
    item_id = models.CharField(max_length=100,blank=True,null=True)
    item_price = models.DecimalField(max_digits=9, decimal_places=6,null=True)
    item_quantity = models.DecimalField(max_digits=9, decimal_places=6,null=True)
