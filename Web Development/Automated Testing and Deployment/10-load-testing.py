from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)  # Wait time between tasks in seconds

    @task
    def perform_request(self):
        self.client.get("/path/to/endpoint")  # Replace with the actual endpoint URL to test

