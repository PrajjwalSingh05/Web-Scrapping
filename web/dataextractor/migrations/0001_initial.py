# Generated by Django 4.2.4 on 2023-08-06 07:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, null=True)),
                ('email', models.CharField(max_length=40, null=True)),
                ('feedback', models.CharField(max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FlipkartBikeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('displacement', models.CharField(max_length=100)),
                ('max_power', models.CharField(max_length=100)),
                ('mileage', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FlipkartEarphoneModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('headphone_type', models.CharField(max_length=100)),
                ('inline_remote', models.CharField(max_length=100)),
                ('connectivity', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FlipkartLaptopModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('processor', models.CharField(max_length=100)),
                ('ram', models.CharField(max_length=100)),
                ('opearting_system', models.CharField(max_length=100)),
                ('hard_disk', models.CharField(max_length=100)),
                ('display', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FlipkartMobileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('memory', models.CharField(max_length=100)),
                ('display', models.CharField(max_length=100)),
                ('camera', models.CharField(max_length=100)),
                ('battery', models.CharField(max_length=100)),
                ('rom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FlipkartTelivisionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('display', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=100)),
                ('operating_system', models.CharField(max_length=100)),
                ('warrently', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FlipkartWachingMachineModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('energy_rating', models.CharField(max_length=100)),
                ('maximum_spin_speed', models.CharField(max_length=100)),
                ('washing_capacity', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TrainedModel',
            fields=[
                ('uniqueid', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=200)),
                ('modelname', models.CharField(max_length=40)),
                ('date', models.CharField(max_length=30, null=True)),
                ('time', models.TimeField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
