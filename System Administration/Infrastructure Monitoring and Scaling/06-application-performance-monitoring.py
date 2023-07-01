import docker

def deploy_container(image_name, container_name, port_mapping):
    client = docker.from_env()

    # Pull the Docker image
    client.images.pull(image_name)

    # Check if the container is already running
    container = client.containers.get(container_name) if container_name in client.containers.list() else None

    if container:
        # If the container already exists, stop and remove it
        container.stop()
        container.remove()

    # Run a new container with the specified image and port mapping
    container = client.containers.run(image_name, detach=True, name=container_name, ports=port_mapping)

    print(f"Container {container_name} deployed and running.")

def scale_container(container_name, num_instances):
    client = docker.from_env()

    # Get the container by name
    containers = client.containers.list(filters={"name": container_name})

    # Scale up or down based on the desired number of instances
    if len(containers) < num_instances:
        # Scale up by starting additional containers
        num_to_start = num_instances - len(containers)
        for _ in range(num_to_start):
            container = client.containers.get(containers[0].id)
            client.api.create_container(image=container.attrs['Config']['Image'], name=container.name)
            container.start()
        print(f"Scaled up {container_name} to {num_instances} instances.")

    elif len(containers) > num_instances:
        # Scale down by stopping and removing excess containers
        num_to_stop = len(containers) - num_instances
        for i in range(num_to_stop):
            container = client.containers.get(containers[i].id)
            container.stop()
            container.remove()
        print(f"Scaled down {container_name} to {num_instances} instances.")

    else:
        print(f"{container_name} is already scaled to {num_instances} instances.")

# Example usage
deploy_container("nginx:latest", "my-nginx", {"80/tcp": 8080})
scale_container("my-nginx", 3)

