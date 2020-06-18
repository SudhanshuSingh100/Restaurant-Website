from django.db import models

# Create your models here.

class Offers(models.Model):
    offer_name = models.CharField(max_length=25)
    offer_img = models.ImageField(upload_to='newoffer/')
    pub_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.offer_name


class Gallery(models.Model):
    gallery_name = models.CharField(max_length=20)
    gallery_img = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.gallery_name

class Chef(models.Model):
    chef_name = models.CharField(max_length=20)
    chef_img = models.ImageField(upload_to='chefs/')

    def __str__(self):
        return self.chef_name

class BookedTable(models.Model):
    name = models.CharField(max_length=22)
    email_id = models.EmailField(max_length=255,null=False)
    mobile = models.IntegerField(null=False)
    tot_people = models.IntegerField(null=False)
    date = models.DateField(null=False)
    time = models.TimeField(unique=True)

    def __str__(self):
        return self.name


