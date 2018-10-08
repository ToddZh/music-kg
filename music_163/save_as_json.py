import json

def read_json():
    with open('../test/data/record.json', 'r') as f:
        data = json.load(f)
        print(data)
        return data

def save_json(data):
    data = {
        'name': 'ACME',
        'shares': 100,
        'price': 542.23
    }
    json_str = json.dumps(data)
    with open('../test/data/savejson.json', 'w') as f:
        f.write(json_str)

if __name__ == '__main__':
    save_json('')
