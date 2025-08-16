from core import helm_generator
import os

def test_helm_chart():
    helm_generator.generate_helm_chart("testapp", "nginx", 80)
    assert os.path.exists("charts/testapp/Chart.yaml")
    assert os.path.exists("charts/testapp/deployment.yaml")