from django.db import models

# Create your models here.
class ImageSpell(models.Model):
    passive = models.CharField(max_length=200,default=None)
    q = models.CharField(max_length = 200,default=None)
    w = models.CharField(max_length = 200,default=None)
    e = models.CharField(max_length = 200,default=None)
    r = models.CharField(max_length = 200,default=None)

class Spell(models.Model):
    passive = models.CharField(max_length=200,default=None)
    q = models.CharField(max_length=200,default=None)
    w = models.CharField(max_length=200,default=None)
    e = models.CharField(max_length=200,default=None)
    r = models.CharField(max_length=200,default=None)
    img = models.ForeignKey(ImageSpell, on_delete=models.CASCADE)


class Items(models.Model):
    name = models.TextField(max_length= 200,default=None)
    description = models.TextField(max_length=200,default=None)
    img = models.CharField(max_length=200,default=None)
    def __str__(self):
        return self.name

class ImageChampion(models.Model):
    main = models.CharField(max_length=200, default= None, null= True)
    splash_art = models.CharField(max_length=200, default= None, null= True)

class ItemChampion(models.Model):
    name = models.TextField(max_length=200)
    starter1 = models.IntegerField(default=0)
    starter2 = models.IntegerField(default=0)
    items_1 = models.IntegerField(default=0)
    items_2 = models.IntegerField(default=0)
    items_3 = models.IntegerField(default=0)
    items_4 = models.IntegerField(default=0)
    items_5 = models.IntegerField(default=0)
    items_6 = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} Build"

class Champion(models.Model):
    name = models.CharField(max_length = 200, null=True)
    title = models.CharField(max_length=200, default= None, null= True)
    img = models.ForeignKey(ImageChampion,on_delete= models.CASCADE, default=None, null=True)
    spell = models.ForeignKey(Spell, on_delete=models.CASCADE)
    def __str__(self):
        return self.name