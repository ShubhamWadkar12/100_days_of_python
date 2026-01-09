environments = ("dev", "qa", "prod")
environments_extended = ("staging", "dr")
allowed_environments = environments + environments_extended
print(allowed_environments)

res = environments.count("dev")
print(res)
res = environments.index("prod")
print(res)