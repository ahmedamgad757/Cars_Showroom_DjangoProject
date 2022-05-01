from django.db import models
from datetime import datetime
# Create your models here.
Type_list=[
        ('Sedan','Sedan'),('Hatchback','Hatchback'),('Coupe','Coupe'),
        ('SUV','SUV'),('4X4','4X4'),('MiniVan','MiniVan'),
    ]
Transmition_list=[
        ('Manual','Manual'),('Automatic','Automatic'),
    ]
Brand_list=[
        ('Audi','Audi'),('BMW','BMW'),('BYD','BYD'),('Chery','Chery'),('Chevrolet','Chevrolet'),('Citroën','Citroën'),
        ('Daewoo','Daewoo'),('Dodge','Dodge'),('Ferrari','Ferrari'),('Fiat','Fiat'),('Ford','Ford'),('Geely','Geely'),
        ('Honda','Honda'),('Hyundai','Hyundai'),('Jeep','Jeep'),('Kia','Kia'),('Lada','Lada'),('Land Rover','Land Rover'),
        ('Mercedes','Mercedes'),('Nissan','Nissan'),('Opel','Opel'),('Peugeot','Peugeot'),('Porsche','Porsche'),('Renault','Renault'),
        ('Skoda','Skoda'),('Speranza','Speranza'),('Toyota','Toyota'),('Volvo','Volvo'),('Other','Other'),
    ]
Fuel_list=[
        ('Gas','Gas'),('Diesel','Diesel'),('Natural Gas','Natural Gas'),('Electric','Electric'),
    ]
Model_Year_list=[
        ('2022','2022'),('2021','2021'),('2020','2020'),('2019','2019'),('2018','2018'),('2017','2017'),
        ('2016','2016'),('2015','2015'),('2014','2014'),('2013','2013'),('2012','2012'),('2011','2011'),
        ('2010','2010'),('2009','2009'),('2008','2008'),('2007','2007'),('2006','2006'),('2005','2005'),
        ('2004','2004'),('2003','2003'),('2002','2002'),('2001','2001'),('2000','2000'),('1999','1999'),
        ('1998','1998'),('1997','1997'),('1996','1996'),('1995','1995'),('Older than 1995','Older tahn 1995'),
    ]
class NewCar(models.Model):
    ad_title=models.CharField(max_length=20,verbose_name='Title')
    Describtion=models.TextField(null=True,blank=True,verbose_name='Describtion')
    price=models.DecimalField(max_digits=8,decimal_places=2)
    type=models.CharField(max_length=20,choices=Type_list)
    brand=models.CharField(max_length=20,choices=Brand_list)
    transmission_type=models.CharField(max_length=20,choices=Transmition_list)
    CC=models.IntegerField()
    model_year=models.CharField(max_length=20,choices=Model_Year_list)
    fuel=models.CharField(max_length=20,choices=Fuel_list)
    color=models.CharField(max_length=20,verbose_name='Color')
    image=models.ImageField(upload_to='photos',default='image/default car.png',verbose_name='Photo')
    active=models.BooleanField(default=True)
    createddate=models.DateTimeField(default=datetime.now,verbose_name='Created Date')

    def __str__(self):
        return self.ad_title

class UsedCar(models.Model):
    ad_title=models.CharField(max_length=20,verbose_name='Title')
    Describtion=models.TextField(null=True,blank=True,verbose_name='Describtion')
    travelled_KM=models.IntegerField()
    owner_name=models.CharField(max_length=20,verbose_name='Owner Name')
    owner_phonenumber=models.CharField(max_length=11,verbose_name='Owner Phone Number')
    price=models.DecimalField(max_digits=8,decimal_places=2)
    type=models.CharField(max_length=20,choices=Type_list)
    brand=models.CharField(max_length=20,choices=Brand_list)
    transmission_type=models.CharField(max_length=20,choices=Transmition_list)
    CC=models.IntegerField()
    model_year=models.CharField(max_length=20,choices=Model_Year_list)
    used_since=models.CharField(max_length=20,choices=Model_Year_list)
    fuel=models.CharField(max_length=20,choices=Fuel_list)
    color=models.CharField(max_length=20,verbose_name='Color')
    extra_equipment=models.TextField(null=True,blank=True,verbose_name='Extras')
    image=models.ImageField(upload_to='photos',default='image/default car.png',verbose_name='Photo')
    address=models.CharField(max_length=50,verbose_name='Address')
    negotiable=models.BooleanField(default=False)
    active=models.BooleanField(default=True)
    createddate=models.DateTimeField(default=datetime.now,verbose_name='Created Date')

    def __str__(self):
        return self.ad_title