"""
百度测试脚本
base-url: http://www.baidu.com
"""
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):

    wait_time = between(0.1, 0.2)

    @task
    def index_page(self):
        """
        https://www.baidu.com/
        :return:
        """
        self.client.get("/")
