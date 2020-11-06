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
    description = models.TextField(max_length=200,default=None)
    img = models.CharField(max_length=200,default=None)


class Rune(models.Model):
    img = models.CharField(max_length=200,default=None)

class ImageChampion(models.Model):
    main = models.CharField(max_length=200, default= None, null= True)
    splash_art = models.CharField(max_length=200, default= None, null= True)
class Champion(models.Model):
    name = models.CharField(max_length = 200, null=True)
    title = models.CharField(max_length=200, default= None, null= True)
    img = models.ForeignKey(ImageChampion,on_delete= models.CASCADE, default=None, null=True)
    spell = models.ForeignKey(Spell, on_delete=models.CASCADE)
