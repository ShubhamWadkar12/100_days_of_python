server = {
    "name" : "web1",
    "status": "running",
    "port": 80
}

config = {"env": "prod", "replicas": 3}
data = {}                                       #empty

print(config.get("env"))                        #prod


config["replicas"] = 5
config["region"] = "ap-south-1"                 #adding and updating


for key, value in config.items():              #Looping Through Dictionary
    print(key, ":", value)

print("--------------------------------------")

servers = {
    "web1": "running",
    "web2": "stopped",
    "db1": "running"
}

for server, status in servers.items():
    print(f"{server} is {status}")



ec2 = {
    "id": "i-123",
    "type": "t2.micro",
    "tags": {
        "env": "prod",                                                  #Nested Dictionary
        "owner": "devops"
    }
}
