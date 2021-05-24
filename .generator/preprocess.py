import yaml
import sys

with open(sys.argv[1]) as f:
    list_doc = yaml.load(f, Loader=yaml.BaseLoader)

list_doc["info"]["title"] = "Firefly III API Client"
list_doc["info"]["description"] = "This is the Python client for Firefly III API"

with open(sys.argv[2], "w") as f:
    yaml.dump(list_doc, f)
