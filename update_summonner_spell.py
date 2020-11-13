import json, urllib.request
from noxusProject.models import SummonnerSpell, ImageSummonnerSpell
with urllib.request.urlopen("http://ddragon.leagueoflegends.com/cdn/10.22.1/data/en_US/summoner.json") as input_file:
        data = input_file.read()
        spell = json.loads(data)
        spell_list = spell['data'].keys()
        # each spell id
        for spell_id in spell_list:
            spell_name = spell['data'][spell_id]['name'] # spell name

            spell_pic = spell['data'][spell_id]['image']['full'] # spell pic
            # http://ddragon.leagueoflegends.com/cdn/10.22.1/img/spell/{spell_pic}
            
            pic = ImageSummonnerSpell(img = spell_pic)
            pic.save()
            name = SummonnerSpell(name = spell_name, img = pic)
            name.save()

            

      