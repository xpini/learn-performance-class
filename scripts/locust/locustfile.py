"""
locust 官方示例
https://docs.locust.io/en/stable/writing-a-locustfile.html
"""
import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    # 用户登入等待时间
    wait_time = between(1, 5)

    @task
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")

    @task(3)
    def view_items(self):
        for item_id in range(10):
            self.client.get(f"/item?id={item_id}", name="/item")
            time.sleep(1)

    def on_start(self):
        self.client.post("/login", json={"username": "foo", "password": "bar"})
