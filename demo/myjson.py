import json
filename = 'file.json'

try:
    f2 = open(filename,"r")
    data = json.load(f2)
    if('name' in data):
        print("hello "+data['name'])
    else:
        name = input("what is your name? ")
        f1 = open(filename,'w')
        json.dump({"name":name},f1)
        f1.close()
except FileNotFoundError:
    print('file.json not found')
except json.decoder.JSONDecodeError as e:
    print('json error',e)