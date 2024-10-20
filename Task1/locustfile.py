from locust import HttpUser, task, between

class NumericalIntegrationUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def perform_integration(self):
        self.client.get("numericalintegralservice/0/3.14159")
