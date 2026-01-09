""" tup = (1,5,6)
print(type(tup))
 """
name = ('shubham',)                                         # , is madatory fpr single element tuple
print(type(name))

servers = ("web1", "web2", "db1")
for server in servers:
    print(f"Deploying on {server}")

webservers = servers[1:3]
print(webservers)


host, port = ("localhost", 3306)
print(host)
print(port)


def get_server():
    return ("web1", "running")
name, status = get_server()


ports = (80, 80, 443)
ports.count(80)   # 2
ports.index(443)  # 2
