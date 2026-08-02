import json


def write_json(path, data): # Path:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4) ## By using this method we are adding the register data to file


