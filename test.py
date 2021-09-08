## Initialize Dataset
import json
f = open('intents2.json')
dataset = json.load(f)
mylist = []

## Add Some Depression Data
import yaml

with open("depression.yml", 'r') as stream:
    try:
        ret = yaml.safe_load(stream)

        for lines in ret['conversations']:
            set = {}
            set['tag'] = lines[0].lower()
            set['patterns'] = [lines[0].lower()]
            string = ""
            for i in range(1,len(lines)):
                string = string + lines[i]
            set['responses'] = [string.lower()]

            mylist.append(set)

    except yaml.YAMLError as exc:
        print(exc)


final_json = {}
final_json['intents'] = mylist

json_object = json.dumps(final_json,indent=4)
with open("intents.json", "w") as outfile:
    outfile.write(json_object)