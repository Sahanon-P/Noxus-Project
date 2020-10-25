from django.db import models

# Create your models here.
class Spell(models.Model):
    passive = models.CharField(max_length = 200)
    image_passive = models.CharField(max_length = 200)
    skill_q = models.CharField(max_length = 200)
    image_q = models.CharField(max_length = 200)
    skill_w = models.CharField(max_length = 200)
    image_w = models.CharField(max_length = 200)
    skill_e = models.CharField(max_length = 200)
    image_e = models.CharField(max_length = 200)
    skill_r = models.CharField(max_length = 200)
    image_r = models.CharField(max_length = 200)
    def __str__(self):
        return self.passive

class Champion(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length = 200)
    image = models.CharField(max_length = 200)
    spell = models.ForeignKey(Spell, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
