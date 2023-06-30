from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)  # Wait time between tasks

    @task
    def load_homepage(self):
        self.client.get("/")

    @task
    def load_products(self):
        self.client.get("/products")

    @task
    def search_products(self):
        payload = {"query": "example"}
        self.client.post("/search", data=payload)


