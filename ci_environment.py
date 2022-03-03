import time
import os
import docker

hostName = ""
hostPort = 8086

for env_var in os.environ:
    print(f"{env_var} : {os.environ[env_var]}")

try: 
    dc = docker.from_env()
    print("Got Docker Client")
    print(dc.info)
    containers = dc.containers.list(all=True)
    print("Got Container List")

    for image in containers:
        print(f"Container: {image.name}")
        print(f"    id: {image.id}")
        print(f"    labels: {image.labels}")
        print(f"    image: {image.image}")
        print(f"    status: {image.status}")
        print("_________________________________________")
except Exception as de:
    print("Couldn't Get Docker Client")
