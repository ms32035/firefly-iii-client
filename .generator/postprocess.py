import os
import sys

ROOT_DIR = sys.argv[1]


def file_replace(file_name, replacements):
    with open(file_name, "r") as file:
        filedata = file.read()

    for rep in replacements:
        filedata = filedata.replace(rep[0], rep[1])

    with open(file_name, "w") as file:
        file.write(filedata)


OLD_AUTHOR = 'author="James Cole"'
NEW_AUTHOR = 'author="Marcin Szymanski"'
OLD_EMAIL = "james@firefly-iii.org"
NEW_EMAIL = "ms32035@gmail.com"
setup_rep = [(OLD_AUTHOR, NEW_AUTHOR), (OLD_EMAIL, NEW_EMAIL), ("  # noqa: E501", "")]
file_replace(os.path.join(ROOT_DIR, "setup.py"), setup_rep)

CONF_STRING_OLD = "configuration.access_token = 'YOUR_ACCESS_TOKEN'"
CONF_STRING_NEW = """configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration.host = 'YOUR_HOST_URL'"""
readme_rep = [
    (OLD_EMAIL, NEW_EMAIL),
    (
        "pip install git+https://github.com/ms32035/firefly-iii-client.git",
        "pip install firefly-iii-client",
    ),
    (CONF_STRING_OLD, CONF_STRING_NEW),
    (
        "configuration = firefly_iii_client.Configuration()",
        "configuration = firefly_iii_client.configuration.Configuration()",
    ),
]

file_replace(os.path.join(ROOT_DIR, "README.md"), readme_rep)
