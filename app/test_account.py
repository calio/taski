import yaml

f = open("test_account.yaml")
contents = f.read()
accounts = yaml.load(contents)
f.close()

def get(domain):
    return accounts[domain]
