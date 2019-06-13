from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User
# Create your models here.


class CupCakes(models.Model):
    # manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=20)
    area = models.CharField(max_length=100)
    # quantity = models.CharField(max_length=100)
    flavour = models.CharField(max_length=30)
    avilable = models.CharField(max_length=50, choices=(
        ('avilable', 'yes'),
        ('unavilable', 'no')
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=datetime.now)
    noofitems = models.IntegerField(default= 0)
    price=models.IntegerField(default= 0)
    def __str__(self):
        return self.name


class ReturnGift(models.Model):
    # manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=20)
    area = models.CharField(max_length=100,default="",)
    # quantity = models.CharField(max_length=100)
    Type = models.CharField(max_length=30)
    avilable = models.CharField(max_length=50, choices=(
        ('avilable', 'yes'),
        ('unavilable', 'no')
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=datetime.now)
    noofitems = models.IntegerField(default= 0)
    price=models.IntegerField(default= 0)
    def __str__(self):
        return self.name

class Hydhalls(models.Model):
    name = models.CharField(max_length=20)
    area = models.CharField(max_length=100)
    # quantity = models.CharField(max_length=100)
    hallname = models.CharField(max_length=30)
    halltype = models.CharField(max_length=30)
    avilable = models.CharField(max_length=50, choices=(
        ('avilable', 'yes'),
        ('unavilable', 'no')
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=datetime.now)
    noofitems = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Hydbdaygifts(models.Model):
    name = models.CharField(max_length=20)
    area = models.CharField(max_length=100)
    # quantity = models.CharField(max_length=100)
    giftname = models.CharField(max_length=30)
    gifttype = models.CharField(max_length=30)
    avilable = models.CharField(max_length=50, choices=(
        ('avilable', 'yes'),
        ('unavilable', 'no')
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=datetime.now)
    noofitems = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Hydbdaydecoration(models.Model):
    name = models.CharField(max_length=20)
    area = models.CharField(max_length=100)
    # quantity = models.CharField(max_length=100)
    decorationname = models.CharField(max_length=30)
    decorationtype = models.CharField(max_length=30)
    avilable = models.CharField(max_length=50, choices=(
        ('avilable', 'yes'),
        ('unavilable', 'no')
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=datetime.now)
    noofitems = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Hydbdaycakes(models.Model):
    name = models.CharField(max_length=20)
    area = models.CharField(max_length=100)
    # quantity = models.CharField(max_length=100)
    decorationname = models.CharField(max_length=30)
    decorationtype = models.CharField(max_length=30)
    avilable = models.CharField(max_length=50, choices=(
        ('avilable', 'yes'),
        ('unavilable', 'no')
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=datetime.now)
    noofitems = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

#*****************************************************************************************************
# wedding events
class Hydmrghalls(models.Model):
    name = models.CharField(max_length=20)
    area = models.CharField(max_length=100)
    # quantity = models.CharField(max_length=100)
    hallname = models.CharField(max_length=30)
    halltype = models.CharField(max_length=30)
    avilable = models.CharField(max_length=50, choices=(
        ('avilable', 'yes'),
        ('unavilable', 'no')
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=datetime.now)
    noofitems = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
        
class Hydmrggifts(models.Model):
    name = models.CharField(max_length=20)
    area = models.CharField(max_length=100)
    # quantity = models.CharField(max_length=100)
    giftname = models.CharField(max_length=30)
    gifttype = models.CharField(max_length=30)
    avilable = models.CharField(max_length=50, choices=(
        ('avilable', 'yes'),
        ('unavilable', 'no')
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=datetime.now)
    noofitems = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Hydmrgmandapdecoration(models.Model):
    name = models.CharField(max_length=20)
    area = models.CharField(max_length=100)
    # quantity = models.CharField(max_length=100)
    decorationname = models.CharField(max_length=30)
    decorationtype = models.CharField(max_length=30)
    avilable = models.CharField(max_length=50, choices=(
        ('avilable', 'yes'),
        ('unavilable', 'no')
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=datetime.now)
    noofitems = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Hydmrgfood(models.Model):
    name = models.CharField(max_length=20)
    area = models.CharField(max_length=100)
    # quantity = models.CharField(max_length=100)
    foodname = models.CharField(max_length=30)
    foodtype = models.CharField(max_length=30)
    avilable = models.CharField(max_length=50, choices=(
        ('avilable', 'yes'),
        ('unavilable', 'no')
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=datetime.now)
    noofitems = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name        

class Hydmrgbachelorparty(models.Model):
    name = models.CharField(max_length=20)
    area = models.CharField(max_length=100)
    # quantity = models.CharField(max_length=100)
    partyname = models.CharField(max_length=30)
    partytype = models.CharField(max_length=30)
    avilable = models.CharField(max_length=50, choices=(
        ('avilable', 'yes'),
        ('unavilable', 'no')
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=datetime.now)
    noofitems = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
class Hydmrgsangeethdecoration(models.Model):
    name = models.CharField(max_length=20)
    area = models.CharField(max_length=100)
    # quantity = models.CharField(max_length=100)
    decorationname = models.CharField(max_length=30)
    decorationtype = models.CharField(max_length=30)
    avilable = models.CharField(max_length=50, choices=(
        ('avilable', 'yes'),
        ('unavilable', 'no')
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=datetime.now)
    noofitems = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name        


 #**************************************************
 #cart       
class Products(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(blank=True)
    noofitems = models.IntegerField(default= 0)
    price=models.IntegerField(default= 0)
    person=models.CharField(max_length=20)
    totalprice=models.IntegerField(default= 0)
    def __str__(self):
        return self.name
class Add_to_cart(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    product=models.ManyToManyField(Products)
    totalprice=models.IntegerField(default= 0)



class Feedback(models.Model):
    customer_name=models.CharField(max_length=120)
    email=models.EmailField()
    #person=models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    details=models.TextField()
    happy=models.BooleanField()
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.customer_name



#***********************************************88
# bachelor party        
class Farmhouses(models.Model):
    name = models.CharField(max_length=20)
    area = models.CharField(max_length=100)
    # quantity = models.CharField(max_length=100)
    farmhousename = models.CharField(max_length=30)
    farmhousetype = models.CharField(max_length=30)
    avilable = models.CharField(max_length=50, choices=(
        ('avilable', 'yes'),
        ('unavilable', 'no')
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=datetime.now)
    noofitems = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name  

class Villas(models.Model):
    name = models.CharField(max_length=20)
    area = models.CharField(max_length=100)
    # quantity = models.CharField(max_length=100)
    villasname = models.CharField(max_length=30)
    villastype = models.CharField(max_length=30)
    avilable = models.CharField(max_length=50, choices=(
        ('avilable', 'yes'),
        ('unavilable', 'no')
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=datetime.now)
    noofitems = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name  

class pubs(models.Model):
    name = models.CharField(max_length=20)
    area = models.CharField(max_length=100)
    # quantity = models.CharField(max_length=100)
    pubname = models.CharField(max_length=30)
    pubtype = models.CharField(max_length=30)
    avilable = models.CharField(max_length=50, choices=(
        ('avilable', 'yes'),
        ('unavilable', 'no')
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=datetime.now)
    noofitems = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name          

class outstation(models.Model):
    name = models.CharField(max_length=20)
    area = models.CharField(max_length=100)
    # quantity = models.CharField(max_length=100)
    stationname = models.CharField(max_length=30)
    stationtype = models.CharField(max_length=30)
    avilable = models.CharField(max_length=50, choices=(
        ('avilable', 'yes'),
        ('unavilable', 'no')
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=datetime.now)
    noofitems = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name     

class entertainment(models.Model):
    name = models.CharField(max_length=20)
    area = models.CharField(max_length=100)
    # quantity = models.CharField(max_length=100)
    entertainmentname = models.CharField(max_length=30)
    entertainmenttype = models.CharField(max_length=30)
    avilable = models.CharField(max_length=50, choices=(
        ('avilable', 'yes'),
        ('unavilable', 'no')
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=datetime.now)
    noofitems = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name           