from prometheus_client import start_http_server

def start_metrics_server(port=8000):
    start_http_server(port)