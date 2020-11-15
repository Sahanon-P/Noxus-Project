import json, urllib.request
from noxusProject.models import SummonnerSpell
with urllib.request.urlopen("http://ddragon.leagueoflegends.com/cdn/10.23.1/data/en_US/summoner.json") as input_file:
        data = input_file.read()
        spell = json.loads(data)
        spell_list = spell['data'].keys()
        # each spell id
        for spell_id in spell_list:
            spell_name = spell['data'][spell_id]['name'] # spell name

            spell_pic = spell['data'][spell_id]['image']['full'] # spell pic
            # http://ddragon.leagueoflegends.com/cdn/10.22.1/img/spell/{spell_pic}
            name = SummonnerSpell(name = spell_name, img = spell_pic)
            name.save()

            

      