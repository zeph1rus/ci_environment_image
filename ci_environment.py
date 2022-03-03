import time
import os
import docker
from beautifultable import BeautifulTable

hostName = ""
hostPort = 8086

env_table = BeautifulTable()

for env_var in os.environ:
    env_table.rows.append([env_var, os.environ[env_var]])
env_table.columns.header = ["var", "value"]
print(env_table)

try: 
    dc = docker.from_env()
    containers = dc.containers.list(all=True)
 
    for image in containers:
        print(f"Container: {image.name}")
        print(f"    id: {image.id}")
        print(f"    labels: {image.labels}")
        print(f"    image: {image.image}")
        print(f"    status: {image.status}")
        print("_________________________________________")
except Exception as de:
    print("Couldn't Get Docker Client")
