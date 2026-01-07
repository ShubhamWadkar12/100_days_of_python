""" marks = [3,5,6,"Shubham",True]
#List → Mutable (can be changed)
marks[2] = 7
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4]) """
 
# Initial list of servers
servers = ["web1", "web2", "db1"]

print(f"Initial servers list:{servers}")

# Accessing elements
print("First server:", servers[0])
print("Last server:", servers[-1])

print("\nChecking servers:")
for server in servers:
    print(f"Checking {server}")

# Adding elements
servers.append("cache1")
print("\nAfter append:", servers)                                   #After append: ['web1', 'web2', 'db1', 'cache1']

servers.insert(1, "loadbalancer")
print("After insert:", servers)                                     #After insert: ['web1', 'loadbalancer', 'web2', 'db1', 'cache1']

# Extending list
new_servers = ["web3", "web4"]
servers.extend(new_servers)
print("After extend:", servers)                                     #After extend: ['web1', 'loadbalancer', 'web2', 'db1', 'cache1', 'web3', 'web4']

# Removing elements
servers.remove("db1")
print("\nAfter removing db1:", servers)                             #After removing db1: ['web1', 'loadbalancer', 'web2', 'cache1', 'web3', 'web4']

servers.pop()
print("After pop (last):", servers)                                 #After pop (last): ['web1', 'loadbalancer', 'web2', 'cache1', 'web3']

servers.pop(0)
print("After pop index 0:", servers)                                #After pop index 0: ['loadbalancer', 'web2', 'cache1', 'web3']

# Final list
print("\nFinal servers list:", servers)


servers = ["192.168.1.10", "192.168.1.11"]
for ip in servers:
    print(f"Pinging {ip}")
