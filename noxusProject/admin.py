from django.contrib import admin
from noxusProject.models import ItemChampion, Champion, RuneChampion, SummonnerSpell, SummonnerSpellChampion
# Register your models here.
admin.site.register(ItemChampion)
admin.site.register(Champion)
admin.site.register(RuneChampion)
admin.site.register(SummonnerSpellChampion)
