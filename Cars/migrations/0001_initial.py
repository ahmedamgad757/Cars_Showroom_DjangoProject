# Generated by Django 4.0.3 on 2022-05-01 03:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewCars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_title', models.CharField(max_length=60, verbose_name='Title')),
                ('Describtion', models.TextField(blank=True, null=True, verbose_name='Describtion')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('type', models.CharField(choices=[('Sedan', 'Sedan'), ('Hatchback', 'Hatchback'), ('Coupe', 'Coupe'), ('SUV', 'SUV'), ('4X4', '4X4'), ('MiniVan', 'MiniVan')], max_length=20)),
                ('brand', models.CharField(choices=[('Audi', 'Audi'), ('BMW', 'BMW'), ('BYD', 'BYD'), ('Chery', 'Chery'), ('Chevrolet', 'Chevrolet'), ('Citroën', 'Citroën'), ('Daewoo', 'Daewoo'), ('Dodge', 'Dodge'), ('Ferrari', 'Ferrari'), ('Fiat', 'Fiat'), ('Ford', 'Ford'), ('Geely', 'Geely'), ('Honda', 'Honda'), ('Hyundai', 'Hyundai'), ('Jeep', 'Jeep'), ('Kia', 'Kia'), ('Lada', 'Lada'), ('Land Rover', 'Land Rover'), ('Mercedes', 'Mercedes'), ('Nissan', 'Nissan'), ('Opel', 'Opel'), ('Peugeot', 'Peugeot'), ('Porsche', 'Porsche'), ('Renault', 'Renault'), ('Skoda', 'Skoda'), ('Speranza', 'Speranza'), ('Toyota', 'Toyota'), ('Volvo', 'Volvo'), ('Other', 'Other')], max_length=20)),
                ('transmission_type', models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], max_length=20)),
                ('CC', models.IntegerField()),
                ('model_year', models.CharField(choices=[('2022', '2022'), ('2021', '2021'), ('2020', '2020'), ('2019', '2019'), ('2018', '2018'), ('2017', '2017'), ('2016', '2016'), ('2015', '2015'), ('2014', '2014'), ('2013', '2013'), ('2012', '2012'), ('2011', '2011'), ('2010', '2010'), ('2009', '2009'), ('2008', '2008'), ('2007', '2007'), ('2006', '2006'), ('2005', '2005'), ('2004', '2004'), ('2003', '2003'), ('2002', '2002'), ('2001', '2001'), ('2000', '2000'), ('1999', '1999'), ('1998', '1998'), ('1997', '1997'), ('1996', '1996'), ('1995', '1995'), ('Older than 1995', 'Older tahn 1995')], max_length=20)),
                ('fuel', models.CharField(choices=[('Gas', 'Gas'), ('Diesel', 'Diesel'), ('Natural Gas', 'Natural Gas'), ('Electric', 'Electric')], max_length=20)),
                ('color', models.CharField(max_length=20, verbose_name='Color')),
                ('image', models.ImageField(default='image/default car.png', upload_to='photos', verbose_name='Photo')),
                ('active', models.BooleanField(default=True)),
                ('createddate', models.DateTimeField(default=datetime.datetime.now, verbose_name='Created Date')),
            ],
        ),
    ]
