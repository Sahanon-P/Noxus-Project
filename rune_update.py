import json
import urllib.request
from noxusProject.models import *
# with open("rune.json", 'r', encoding="cp866") as input_file:
data = urllib.request.urlopen(
    "http://ddragon.leagueoflegends.com/cdn/10.23.1/data/en_US/runesReforged.json")
rune = json.load(data)
# each rune id
list_rune = []
list_keystone = []
list_subrune = []
for rune_id in range(5):
    dict_rune = {}
    dict_rune[rune[rune_id]['name']] = rune[rune_id]['icon']  # Main rune icon
    list_rune.append(dict_rune)
    for sub_rune_id1 in range(4):
        dict_keystone = {}
        try:
            temp = rune[rune_id]['slots'][0]['runes'][sub_rune_id1]
            dict_keystone[temp['name']] = temp['icon']
            list_keystone.append(dict_keystone)
        except IndexError:
            pass
    count = 1
    for sub_rune_id1 in range(4):
        dict_sub_rune = {}
        try:
            temp1 = rune[rune_id]['slots'][1]['runes'][sub_rune_id1]
            dict_sub_rune[temp1['name']] = temp1['icon']
            list_subrune.append(dict_sub_rune)
        except IndexError:
            pass
    for sub_rune_id1 in range(4):
        dict_sub_rune = {}
        try:
            temp1 = rune[rune_id]['slots'][2]['runes'][sub_rune_id1]
            dict_sub_rune[temp1['name']] = temp1['icon']
            list_subrune.append(dict_sub_rune)
        except IndexError:
            pass
    for sub_rune_id1 in range(4):
        dict_sub_rune = {}
        try:
            temp1 = rune[rune_id]['slots'][3]['runes'][sub_rune_id1]
            dict_sub_rune[temp1['name']] = temp1['icon']
            list_subrune.append(dict_sub_rune)
        except IndexError:
            pass
def get_key(x):
    for i in x:
        return i

def get_value(x):
    for i in x.values():
        return i

r = 1
for i in range(10):
    d_subrune = SubRune(rune = get_key(list_rune[0]),name = get_key(list_subrune[i]),row = r,img=get_value(list_subrune[i]))
    d_subrune.save()
    if (i+1) %3 == 0 and r<3:
        r+=1
for i in range(4):
    d_keystone = KeyStone(rune = get_key(list_rune[0]),name = get_key(list_keystone[i]),img = get_value(list_keystone[i]))
    d_keystone.save()
domination = Rune(name = get_key(list_rune[0]),img = get_value(list_rune[0]))
domination.save()

r = 1
for i in range(10,19):
    d_subrune = SubRune(rune = get_key(list_rune[1]),name = get_key(list_subrune[i]),row = r,img=get_value(list_subrune[i]))
    if (i+1-10) %3 == 0:
        r+=1
    d_subrune.save()
for i in range(4,7):
    d_keystone = KeyStone(rune = get_key(list_rune[1]),name = get_key(list_keystone[i]),img = get_value(list_keystone[i]))
    d_keystone.save()
domination = Rune(name = get_key(list_rune[1]),img = get_value(list_rune[1]))
domination.save()

r = 1
for i in range(19,28):
    d_subrune = SubRune(rune = get_key(list_rune[2]),name = get_key(list_subrune[i]),row = r,img=get_value(list_subrune[i]))
    if (i-19+1) %3 == 0:
        r+=1
    d_subrune.save()
for i in range(7,11):
    d_keystone = KeyStone(rune = get_key(list_rune[2]),name = get_key(list_keystone[i]),img = get_value(list_keystone[i]))
    d_keystone.save()
domination = Rune(name = get_key(list_rune[2]),img = get_value(list_rune[2]))
domination.save()

r = 1
for i in range(28,37):
    d_subrune = SubRune(rune = get_key(list_rune[3]),name = get_key(list_subrune[i]),row = r,img=get_value(list_subrune[i]))
    if (i-28+1) %3 == 0:
        r+=1
    d_subrune.save()
for i in range(11,14):
    d_keystone = KeyStone(rune = get_key(list_rune[3]),name = get_key(list_keystone[i]),img = get_value(list_keystone[i]))
    d_keystone.save()
domination = Rune(name = get_key(list_rune[3]),img = get_value(list_rune[3]))
domination.save()

r = 1
for i in range(37,46):
    d_subrune = SubRune(rune = get_key(list_rune[4]),name = get_key(list_subrune[i]),row = r,img=get_value(list_subrune[i]))
    if (i-37+1) %3 == 0:
        r+=1
    d_subrune.save()
for i in range(14,17):
    d_keystone = KeyStone(rune = get_key(list_rune[4]),name = get_key(list_keystone[i]),img = get_value(list_keystone[i]))
    d_keystone.save()
domination = Rune(name = get_key(list_rune[4]),img = get_value(list_rune[4]))
domination.save()

