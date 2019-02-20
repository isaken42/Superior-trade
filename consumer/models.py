from django.db import models

class Consumer(models.Model):
    lon = models.DecimalField(max_digits=9, decimal_places=6,blank=True,null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6,blank=True,null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    locale = models.CharField(max_length=250)
    phoneNo =models.IntegerField()
    email  = models.EmailField(max_length=200)
    consumer_image =models.ImageField(upload_to='media/consumer/', blank=True)
    ip_address = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    date_joined = models.DateTimeField(auto_now_add=False)

    @property
    def consumer_details(self):
        "Returns the person's full name and phone number."
        return '%s %s %s' % (self.first_name, self.last_name,self.phoneNo) 

class CustomerRetailer(models.Model):
    retail_consumer = models.ForeignKey(Consumer,on_delete=models.CASCADE)
    retail_name = models.CharField(max_length=200)
    item_brand = models.CharField(max_length=200,blank=True,null=True)
    item_type =models.CharField(max_length=200,blank=True,null=True)
    item_product_line = models.CharField(max_length=200,blank=True,null=True) 
    item_id = models.CharField(max_length=100,blank=True,null=True)
    item_price = models.DecimalField(max_digits=9, decimal_places=6,blank=True,null=True)
    item_quantity = models.FloatField()
    item_manufacture = models.CharField(max_length=200,blank=True,null=True)
    item_bought = models.DateTimeField(auto_now_add=True)

