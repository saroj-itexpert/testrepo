from django.db import models
from datetime import datetime
from realtors.models import Realtor



# Create your models here.
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete = models.DO_NOTHING)
    title = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    zipcode = models.CharField(max_length = 20)
    description = models.TextField(blank=True)      #blank -> this field is optional to fill description
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)       #first number should be of 2 digits
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d/')  #Location inside media folder img goes to
    photo_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)  #Location inside media folder img goes to
    photo_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)  #Location inside media folder img goes to
    photo_3 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)  #Location inside media folder img goes to
    photo_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)  #Location inside media folder img goes to
    photo_5 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)  #Location inside media folder img goes to
    photo_6 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)  #Location inside media folder img goes to
    is_pubished = models.BooleanField(default=True)
    list_date = models.DateTimeField(default = datetime.now, blank=True)
    def __str__(self):          #Main thing to display
        return self.title   
