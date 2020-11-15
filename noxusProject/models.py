from django.db import models
from django.db.models.aggregates import Max

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

class SubRune(models.Model):
    rune = models.CharField(max_length=200,default=None,null=True)
    row = models.IntegerField(default=None,null=True)
    name = models.CharField(max_length=200,default=None,null=True)
    img = models.CharField(max_length=200,default=None,null=True)
    def __str__(self):
        return self.name

class KeyStone(models.Model):
    rune = models.CharField(max_length=200,default=None,null=True)
    name = models.CharField(max_length=200,default=None,null=True)
    img = models.CharField(max_length=200,default=None,null=True)
    
    def __str__(self):
        return self.name

class Rune(models.Model):
    name = models.CharField(max_length=200,default=None)
    img = models.CharField(max_length=200,default=None)
    def __str__(self):
        return self.name

class RuneChampion(models.Model):
    name = models.CharField(max_length=200,default=None)
    rune = models.ForeignKey(Rune,on_delete=models.CASCADE,related_name="main")
    key_stone = models.ForeignKey(KeyStone,on_delete=models.CASCADE,related_name="main")
    row1 = models.ForeignKey(SubRune,on_delete=models.CASCADE,related_name="row1")
    row2 = models.ForeignKey(SubRune,on_delete=models.CASCADE,related_name="row2")
    row3 = models.ForeignKey(SubRune,on_delete=models.CASCADE,related_name="row3")
    sub_rune = models.ForeignKey(Rune,on_delete=models.CASCADE,related_name="sub")
    sub_row1 = models.ForeignKey(SubRune,on_delete=models.CASCADE,related_name="sub_row1")
    sub_row2 = models.ForeignKey(SubRune,on_delete=models.CASCADE,related_name="sub_row2")
    def __str__(self) -> str:
        return f"{self.name} Rune"

class ImageChampion(models.Model):
    main = models.CharField(max_length=200, default= None, null= True)
    splash_art = models.CharField(max_length=200, default= None, null= True)

class ItemChampion(models.Model):
    name = models.CharField(max_length=200)
    starter1 = models.ForeignKey(Items,on_delete=models.CASCADE,related_name="starter1")
    starter2 = models.ForeignKey(Items,on_delete=models.CASCADE,related_name="starter2")
    items_1 = models.ForeignKey(Items,on_delete=models.CASCADE,related_name="item1")
    items_2 = models.ForeignKey(Items,on_delete=models.CASCADE,related_name="item2")
    items_3 = models.ForeignKey(Items,on_delete=models.CASCADE,related_name="item3")
    items_4 = models.ForeignKey(Items,on_delete=models.CASCADE,related_name="item4")
    items_5 = models.ForeignKey(Items,on_delete=models.CASCADE,related_name="item5")
    items_6 = models.ForeignKey(Items,on_delete=models.CASCADE,related_name="item6")

    def __str__(self):
        return f"{self.name} Build"

class Champion(models.Model):
    name = models.CharField(max_length = 200, null=True)
    title = models.CharField(max_length=200, default= None, null= True)
    img = models.ForeignKey(ImageChampion, on_delete= models.CASCADE, default=None, null=True)
    spell = models.ForeignKey(Spell, on_delete=models.CASCADE)
    top = models.BooleanField(default=False)
    mid = models.BooleanField(default=False)
    jungler = models.BooleanField(default=False)
    adc = models.BooleanField(default=False)
    support = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class SummonnerSpell(models.Model):
    name = models.CharField(max_length = 200, null=True)
    img = models.CharField(max_length = 200, null=True)
    def __str__(self) -> str:
        return self.name

class SummonnerSpellChampion(models.Model):
    name = models.CharField(max_length = 200, null=True)
    spell1 = models.ForeignKey(SummonnerSpell,on_delete=models.CASCADE,related_name="spell1")
    spell2 = models.ForeignKey(SummonnerSpell,on_delete=models.CASCADE,related_name="spell2")
    def __str__(self) -> str:
        return f"{self.name} Spell"

