# Generated by Django 3.0.6 on 2020-06-03 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homeapp', '0003_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chef_name', models.CharField(max_length=20)),
                ('chef_img', models.ImageField(upload_to='chefs/')),
            ],
        ),
    ]
