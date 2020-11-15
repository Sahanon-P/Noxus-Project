import json, urllib.request
from noxusProject.models import Items
urls = "http://ddragon.leagueoflegends.com/cdn/10.23.1/data/en_US/item.json"
data = urllib.request.urlopen(urls)
item = json.load(data)
item_list = item['data'].keys()
for item_id in item_list:
    item_name = item['data'][item_id]['name'] # item name
    item_pic = item['data'][item_id]['image']['full'] # item pic
    # http://ddragon.leagueoflegends.com/cdn/10.22.1/img/item/{item_pic} << link to item pic
    item_description = item['data'][item_id]['plaintext'] # item plaintext (**not actually description**)
    items = Items(id=item_id,name = item_name,description = item_description,img = item_pic)
    items.save()
    # print(item['data'][item_id]['description']) # item description (**need to do some thing about <> thingy)
