import os
import configparser

gitconfig_path = os.path.expanduser(".git/config")
config = configparser.ConfigParser()
config.read(gitconfig_path)



print(config.sections())
# Access and print a specific configuration value
print(config.get("remote \"origin\"", "url"))

