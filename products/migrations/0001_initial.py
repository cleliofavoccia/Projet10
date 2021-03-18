# Generated by Django 3.1.5 on 2021-02-12 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='product name')),
                ('description', models.TextField(verbose_name='product description')),
                ('nutriscore', models.CharField(max_length=1, verbose_name='product nutriscore')),
                ('url', models.URLField(verbose_name='product url')),
                ('image_url', models.URLField(verbose_name='product image url')),
                ('nutrition_image_url', models.URLField(verbose_name='product nutrition image url')),
                ('categories', models.ManyToManyField(related_name='products', to='products.Category')),
            ],
        ),
    ]
