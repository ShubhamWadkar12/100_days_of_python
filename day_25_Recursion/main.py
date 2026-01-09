servers = ["web1", "web2", "db1"]

def check_server(i):
    if i == len(servers):   # stop condition
        return
    print(f"Checking server: {servers[i]}")
    check_server(i + 1)                                             #recursion

check_server(0)
