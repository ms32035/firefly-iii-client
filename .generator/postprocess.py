import os
import sys


OLD_AUTHOR = 'author="James Cole"'
NEW_AUTHOR = 'author="Marcin Szymanski"'
OLD_EMAIL = "james@firefly-iii.org"
NEW_EMAIL = "ms32035@gmail.com"

CONF_STRING_NEW = """configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration.host = 'YOUR_HOST_URL'"""


REPLACEMENTS = {
    "setup.py": {OLD_AUTHOR: NEW_AUTHOR, OLD_EMAIL: NEW_EMAIL, "  # noqa: E501": ""},
    "README.md": {
        OLD_EMAIL: NEW_EMAIL,
        "pip install git+https://github.com/ms32035/firefly-iii-client.git": "pip install firefly-iii-client",
        "configuration.access_token = 'YOUR_ACCESS_TOKEN'": CONF_STRING_NEW,
        "configuration = firefly_iii_client.Configuration()": "configuration = firefly_iii_client.configuration.Configuration()",
        "pip install firefly-iii-client": "pip install Firefly-III-API-Client",
    },
}

for file, changes in REPLACEMENTS.items():
    full_path = os.path.join(sys.argv[1], file)

    with open(full_path, "r") as changed_file:
        file_data = changed_file.read()

    for old, new in changes.items():
        file_data = file_data.replace(old, new)

    with open(full_path, "w") as changed_file:
        changed_file.write(file_data)
