ips = {"10.0.0.1","10.0.0.2","10.0.0.1"}
print(type(ips))
print(ips)


server_list = ["web1", "web2", "web1"]                              # convert list to set
unique_servers = set(server_list)
print(unique_servers)


servers = {"web1", "web2", "db1"}
if "db1" in servers:
    print("DB server found")


expected_pods = {"pod1", "pod2", "pod3"}    
running_pods = {"pod1", "pod3"}
missing_pods = expected_pods - running_pods                         #missing
print(missing_pods)


prod_servers = {"web1", "web2", "db1"}
monitoring_servers = {"web2", "db1"}    
common = prod_servers & monitoring_servers                          #common
print(common)

env1 = {"dev", "qa"}
env2 = {"prod", "staging"}      
all_envs = env1 | env2                                              #merge


servers.add("cache1")
servers.remove("web1")                                              # error if not exists
servers.discard("webX")                                             # safe


expected_ports = {22, 80, 443}
open_ports = {22, 80}
if expected_ports <= open_ports:
    print("All required ports open")
else:
    print("Some ports missing")
