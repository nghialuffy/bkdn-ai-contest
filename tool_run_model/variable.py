import yaml, os

yaml_file = open("settings.yaml")
cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)

MONGO_URI = cfg["MONGO_URI"]
MONGO_DB = cfg["MONGO_DB"]
PYTHON3_VENV = cfg["PYTHON3_VENV"]