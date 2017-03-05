import getpass
import yaml

file_name = "test_account.yaml"
data = {}

print("Creating file to store credentials for todoist.com")
user = raw_input("user name: ")
pwd = getpass.getpass("password: ")

data["todoist.com"] = {"user": user, "password": pwd}

with open(file_name, "w") as f:
    f.write(yaml.dump(data, encoding='utf-8'))

print(file_name + " created")
