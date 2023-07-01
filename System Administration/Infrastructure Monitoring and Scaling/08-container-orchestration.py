import docker

# Create Docker client
client = docker.from_env()

# Define configuration for the container
container_name = "my-app"
image_name = "my-app-image"
port_mapping = {
    "8000/tcp": 8000  # Example: Map container port 8000 to host port 8000
}
environment_vars = {
    "ENV_VAR1": "value1",
    "ENV_VAR2": "value2"
}
num_instances = 3  # Number of instances to run

def deploy_containers():
    # Pull the latest image
    client.images.pull(image_name)

    # Deploy the containers
    for i in range(num_instances):
        container = client.containers.run(
            image_name,
            name=f"{container_name}-{i+1}",
            ports=port_mapping,
            environment=environment_vars,
            detach=True
        )
        print(f"Container {container.name} deployed successfully.")

def scale_containers(num_instances):
    # Retrieve the running containers
    containers = client.containers.list(filters={"name": container_name})

    # Scale up or down based on the desired number of instances
    if len(containers) < num_instances:
        # Scale up by creating additional containers
        for i in range(len(containers), num_instances):
            container = client.containers.run(
                image_name,
                name=f"{container_name}-{i+1}",
                ports=port_mapping,
                environment=environment_vars,
                detach=True
            )
            print(f"Container {container.name} deployed successfully.")
    elif len(containers) > num_instances:
        # Scale down by removing excess containers
        for i in range(num_instances, len(containers)):
            container = containers[i]
            container.stop()
            container.remove()
            print(f"Container {container.name} removed successfully.")

# Deploy initial set of containers
deploy_containers()

# Scale up to 5 instances
scale_containers(5)

# Scale down to 2 instances
scale_containers(2)

