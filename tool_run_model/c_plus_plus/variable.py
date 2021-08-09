import yaml, os

yaml_file = open("settings.yaml")
cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)

MONGO_URI = cfg["MONGO_URI"]
MONGO_DB = cfg["MONGO_DB"]
MEDIA_PATH = cfg["MEDIA_PATH"]
LANGUAGE_NAME = cfg["LANGUAGE_NAME"]