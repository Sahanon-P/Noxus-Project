from django.db import models

# Create your models here.
# class ImageChampion(models.Model):
#     main = models.ImageField()
#     splash_art = models.ImageField()

# class ImageSpell(models.Model):
#     passive = models.ImageField()
#     q = models.ImageField()
#     w = models.ImageField()
#     e = models.ImageField()
#     r = models.ImageField()

# class Spell(models.Model):
#     passive = models.CharField(max_length = 200)
#     q = models.CharField(max_length = 200)
#     w = models.CharField(max_length = 200)
#     e = models.CharField(max_length = 200)
#     r = models.CharField(max_length = 200)
#     img = models.ForeignKey(ImageSpell, models.CASCADE)

# class Items(models.Model):
#     description = models.CharField(max_length = 200)
#     img = models.ImageField()

# class Rune(models.Model):
#     img = models.ImageField()

# class ChampionRune(models.Model):
#     key_stone = models.ForeignKey(Rune,on_delete=models.CASCADE)
#     sub_key_1 = models.ForeignKey(Rune,on_delete=models.CASCADE)
#     sub_key_2 = models.ForeignKey(Rune,on_delete=models.CASCADE)
#     sub_key_3 = models.ForeignKey(Rune,on_delete=models.CASCADE)
#     sub_rune_1 = models.ForeignKey(Rune,on_delete=models.CASCADE)
#     sub_rune_2 = models.ForeignKey(Rune,on_delete=models.CASCADE)

# class ChampionItem(models.Model):
#     starter_1 = models.ForeignKey(Items,on_delete=models.CASCADE)
#     starter_2 = models.ForeignKey(Items,on_delete=models.CASCADE)
#     items_1 = models.ForeignKey(Items,on_delete=models.CASCADE)
#     items_2 = models.ForeignKey(Items,on_delete=models.CASCADE)
#     items_3 = models.ForeignKey(Items,on_delete=models.CASCADE)
#     items_4 = models.ForeignKey(Items,on_delete=models.CASCADE)
#     items_5 = models.ForeignKey(Items,on_delete=models.CASCADE)
#     items_6 = models.ForeignKey(Items,on_delete=models.CASCADE)

# class Champion(models.Model):
#     name = models.CharField(max_length = 200)
#     title = models.CharField(max_length = 200)
#     img = models.ForeignKey(ImageChampion,on_delete= models.CASCADE)
#     spell = models.ForeignKey(Spell, on_delete= models.CASCADE)
#     items = models.ForeignKey(ChampionItem, on_delete=models.CASCADE)
#     rune = models.ForeignKey(ChampionRune,on_delete= models.CASCADE)


    


    