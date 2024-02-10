import yaml

def read_yaml_data(filepath):
    with open(filepath, 'r') as file:
        data = yaml.safe_load(file)
    return data