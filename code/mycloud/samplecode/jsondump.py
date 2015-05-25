import json

my_dict={'../do':['lasmc',1]}
my_dict['../di']=['skmc',2]
with open('my_dict.json', 'w') as f:
    json.dump(my_dict, f)

# elsewhere...

with open('my_dict.json') as f:
    my_dict = json.load(f)
print(my_dict)
