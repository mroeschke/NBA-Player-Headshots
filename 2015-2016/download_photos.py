import requests
import string

def string_clean(old_string):
    if len(old_string.split()) > 1:
        old_string = '_'.join(word for word in old_string.split())
    valid_chars = string.ascii_letters + ',-_'
    return ''.join(char for char in old_string if char in valid_chars)

def save_image(search, name, file_extention = "Player Photos"):
    file_name = "{file}/{name}.png".format(file = file_extention, name = name)
    with open(file_name,'wb') as f:
        f.write(search.content)

base_url = "http://i.cdn.turner.com/nba/nba/.element/img/2.0/sect/statscube/players/large/"
missing_file = open('Missing Players.txt','w')
with open('NBA Players 2015-2016.txt','r') as f:
    for line in f:
        desc = map(string_clean, line.split(','))
        team = desc.pop()
        search_name = '_'.join(name.lower() for name in reversed(desc))
        disp_name = ' '.join(name for name in reversed(desc))
        url = base_url + search_name + '.png'
        search = requests.get(url)
        if search.status_code == requests.codes.ok:
            file_name = 'Player Photos/{}.png'.format(disp_name)
            with open(file_name,'wb') as photo:
                photo.write(search.content)
        else:
            missing_file.write(disp_name + '\n')
missing_file.close()
