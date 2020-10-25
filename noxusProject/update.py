import json,urllib.request
from .models import Champion,Spell
main_url = "http://ddragon.leagueoflegends.com/cdn/10.21.1/data/en_US/champion.json"
data_byte = urllib.request.urlopen(main_url)
data_str = json.load(data_byte)
for name in data_str['data'].keys():
    temp_name = name
    url = f"http://ddragon.leagueoflegends.com/cdn/10.21.1/data/en_US/champion/{name}.json"
    temp_title = data_str['data'][name]['title']
    temp_image = f"http://ddragon.leagueoflegends.com/cdn/10.21.1/img/champion/{name}.png"
    spell_byte = urllib.request.urlopen(url)
    spell_str = json.load(spell_byte)
    temp_passive = spell_str['data'][name]['passive']['name']
    img_passive = spell_str['data'][name]['passive']['image']['full']
    url_passive = f"http://ddragon.leagueoflegends.com/cdn/10.21.1/img/passive/{img_passive}"
    temp_q = spell_str['data'][name]['spells'][0]['name']
    img_q =  spell_str['data'][name]['spells'][0]['image']['full']
    url_q = f"http://ddragon.leagueoflegends.com/cdn/10.21.1/img/spell/{img_q}.png"
    temp_w = spell_str['data'][name]['spells'][1]['name']
    img_w =  spell_str['data'][name]['spells'][1]['image']['full']
    url_w = f"http://ddragon.leagueoflegends.com/cdn/10.21.1/img/spell/{img_w}.png"
    temp_e = spell_str['data'][name]['spells'][2]['name']
    img_e =  spell_str['data'][name]['spells'][2]['image']['full']
    url_e = f"http://ddragon.leagueoflegends.com/cdn/10.21.1/img/spell/{img_e}.png"
    temp_r = spell_str['data'][name]['spells'][3]['name']
    img_r =  spell_str['data'][name]['spells'][3]['image']['full']
    url_r = f"http://ddragon.leagueoflegends.com/cdn/10.21.1/img/spell/{img_r}.png"
    spells = Spell(passive = temp_passive, image_passive = url_passive,skill_q = temp_q,image_q = url_q,skill_w = temp_w,image_w = url_w,skill_e = temp_e,image_e = url_e,skill_r = temp_r,image_r = url_r)
    champion = Champion(name = temp_name, title= temp_title,image = temp_image,spell=spells)
    champion.save()