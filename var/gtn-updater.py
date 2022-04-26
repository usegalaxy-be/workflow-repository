import sys
import json
import re
import os

pwd = sys.argv[1]
filename = sys.argv[2]
topic = sys.argv[3]
tutorial = sys.argv[4]

print(filename)

with open(filename) as json_file:
    data = json.load(json_file)
    if 'tags' in data:
        if topic not in data['tags']:
            data['tags'].append(str(topic))
    else:
        data['tags'] = [str(topic)]
    name = re.sub(r'(\S)-(\S)', r'\1 \2', data['name'])
    splitnamename =  name.replace('(imported from uploaded file)','').replace('_', ' ').split(' ')
    newname = []
    for word in splitnamename:
        if word:
            if any(c.isupper() for c in word):
                newname.append(word)  
            else:
                newname.append(word.capitalize())
    
    data['name'] = ' '.join(newname)

with open(f"{pwd}/GTN/{tutorial}_{os.path.basename(filename)}", 'w') as f:
    json.dump(data, f, sort_keys=False, indent=2)
