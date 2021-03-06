# Generated by Django 2.2.1 on 2019-06-05 08:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_hydbdaycakes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hydmrgbachelorparty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=100)),
                ('partyname', models.CharField(max_length=30)),
                ('partytype', models.CharField(max_length=30)),
                ('avilable', models.CharField(choices=[('avilable', 'yes'), ('unavilable', 'no')], max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('date_added', models.DateTimeField(default=datetime.datetime.now)),
                ('noofitems', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Hydmrgfood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=100)),
                ('foodname', models.CharField(max_length=30)),
                ('foodtype', models.CharField(max_length=30)),
                ('avilable', models.CharField(choices=[('avilable', 'yes'), ('unavilable', 'no')], max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('date_added', models.DateTimeField(default=datetime.datetime.now)),
                ('noofitems', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Hydmrggifts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=100)),
                ('giftname', models.CharField(max_length=30)),
                ('gifttype', models.CharField(max_length=30)),
                ('avilable', models.CharField(choices=[('avilable', 'yes'), ('unavilable', 'no')], max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('date_added', models.DateTimeField(default=datetime.datetime.now)),
                ('noofitems', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Hydmrghalls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=100)),
                ('hallname', models.CharField(max_length=30)),
                ('halltype', models.CharField(max_length=30)),
                ('avilable', models.CharField(choices=[('avilable', 'yes'), ('unavilable', 'no')], max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('date_added', models.DateTimeField(default=datetime.datetime.now)),
                ('noofitems', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Hydmrgmandapdecoration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=100)),
                ('decorationname', models.CharField(max_length=30)),
                ('decorationtype', models.CharField(max_length=30)),
                ('avilable', models.CharField(choices=[('avilable', 'yes'), ('unavilable', 'no')], max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('date_added', models.DateTimeField(default=datetime.datetime.now)),
                ('noofitems', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Hydmrgsangeethdecoration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=100)),
                ('decorationname', models.CharField(max_length=30)),
                ('decorationtype', models.CharField(max_length=30)),
                ('avilable', models.CharField(choices=[('avilable', 'yes'), ('unavilable', 'no')], max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('date_added', models.DateTimeField(default=datetime.datetime.now)),
                ('noofitems', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
