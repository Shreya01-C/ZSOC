import yaml
import os

def generate_helm_chart(app_name, image, port):
    chart = {
        "apiVersion": "v2",
        "name": app_name,
        "version": "0.1.0",
        "appVersion": "1.0",
    }

    deployment = {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {"name": app_name},
        "spec": {
            "replicas": 1,
            "selector": {"matchLabels": {"app": app_name}},
            "template": {
                "metadata": {"labels": {"app": app_name}},
                "spec": {
                    "containers": [{
                        "name": app_name,
                        "image": image,
                        "ports": [{"containerPort": port}]
                    }]
                }
            }
        }
    }

    os.makedirs(f"charts/{app_name}", exist_ok=True)
    with open(f"charts/{app_name}/Chart.yaml", "w") as f:
        yaml.dump(chart, f)
    with open(f"charts/{app_name}/deployment.yaml", "w") as f:
        yaml.dump(deployment, f)
    print(f"Helm chart generated in charts/{app_name}/")