import json



def read_json():
    with open('../test/data/savejson.json', 'r') as f:
        message = '[' + f.read() + ']'
        # print(message)
        data = json.loads(message)
        # print(data[0])
        return data

def save_json(data):
    json_str = json.dumps(data)
    with open('../test/data/savejson.json', 'w') as f:
        f.write('[' + json_str + ']')

def add_json(data):
    json_str = json.dumps(data)
    with open('../test/data/savejson.json', 'a') as f:
        f.write(',' + '\n' + json_str)

def save_entity(data):
    with open('../test/data/entity.txt', 'w') as f:
        f.write(data)

if __name__ == '__main__':
    data = {
        'name': 'ACME',
        'shares': 100,
        'price': 542.23
    }
    read_json()
