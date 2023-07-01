import subprocess

def configure_load_balancer(backend_servers, listen_port, upstream_name):
    # Generate the upstream block configuration
    upstream_config = "upstream " + upstream_name + " {\n"
    for server in backend_servers:
        upstream_config += "    server " + server + ";\n"
    upstream_config += "}\n"

    # Generate the main Nginx configuration
    nginx_config = "http {\n"
    nginx_config += "    upstream " + upstream_name + ";\n"
    nginx_config += "    server {\n"
    nginx_config += "        listen " + listen_port + ";\n"
    nginx_config += "        location / {\n"
    nginx_config += "            proxy_pass http://" + upstream_name + ";\n"
    nginx_config += "        }\n"
    nginx_config += "    }\n"
    nginx_config += "}\n"

    # Write the configuration to a temporary file
    temp_config_file = "/tmp/load_balancer.conf"
    with open(temp_config_file, "w") as f:
        f.write(upstream_config + nginx_config)

    # Run the Nginx configuration test and reload Nginx
    try:
        subprocess.run(["nginx", "-t"], check=True)
        subprocess.run(["nginx", "-s", "reload"], check=True)
        print("Load balancer configuration updated successfully!")
    except subprocess.CalledProcessError as e:
        print("Failed to update load balancer configuration:", e)

# Example usage
backend_servers = ["backend1.example.com", "backend2.example.com", "backend3.example.com"]
listen_port = "80"
upstream_name = "my_backend_servers"

configure_load_balancer(backend_servers, listen_port, upstream_name)

