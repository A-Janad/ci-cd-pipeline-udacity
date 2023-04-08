from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    @task(1)
    def test1(self):
        self.client.get("http://localhost:7000")

    @task(2)
    def test2(self):
        self.client.post("http://localhost:7000/predict")