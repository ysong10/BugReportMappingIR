import json


def json_extract(obj):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr)
                elif k == "resource-id":
                    arr.append(obj.get("text"))
                    #arr.append(obj.get("text"))

        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr)
        return arr

    values = extract(obj, arr)
    return values


if __name__ == '__main__':
    with open('/Users/antusaha/Documents/GitHub/JSON files/13.json', 'r') as f:
        data = json.load(f)
        #data = json.dumps(data)
        values = json_extract(data)
        print(values.__len__())
        print(values)

