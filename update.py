import json,urllib.request
from noxusProject.models import Champion, ImageChampion, ImageSpell,Spell
main_url = "http://ddragon.leagueoflegends.com/cdn/10.23.1/data/en_US/champion.json"
data_byte = urllib.request.urlopen(main_url)
data_str = json.load(data_byte)
for name in data_str['data'].keys():
    url_champion = urllib.request.urlopen(f'http://ddragon.leagueoflegends.com/cdn/10.23.1/data/en_US/champion/{name}.json')
    champ = json.load(url_champion)
    temp_name = name
    temp_title = data_str['data'][name]['title']
    square_pic = champ['data'][name]['image']['full']
    splash_pic = f"{name}_0.png"
    sq = champ['data'][name]['spells'][0]['name'] # Champion Skills q,w,e,r
    sw = champ['data'][name]['spells'][1]['name']
    se = champ['data'][name]['spells'][2]['name']
    sr = champ['data'][name]['spells'][3]['name']

    pic_q = champ['data'][name]['spells'][0]['id'] # skill pic
    pic_w = champ['data'][name]['spells'][1]['id']
    pic_e = champ['data'][name]['spells'][2]['id']
    pic_r = champ['data'][name]['spells'][3]['id']
    spell_image = ImageSpell(passive = "",q= pic_q,w=pic_w,e=pic_e,r=pic_r)
    spell_image.save()
    sp = Spell(passive ="",q = sq,w = sw,e =se,r=sr,img = spell_image)
    sp.save()
    image = ImageChampion(main = square_pic, splash_art = splash_pic)
    image.save()
    champion = Champion(name = temp_name, title= temp_title, img = image,spell = sp)
    champion.save()