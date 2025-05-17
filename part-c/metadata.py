import requests

metadata_url = "http://169.254.169.254/latest/meta-data/"
fields = [
    "instance-id", "ami-id", "hostname", "instance-type",
    "local-ipv4", "public-ipv4", "placement/availability-zone"
]

print("📡 EC2 Instance Metadata:\n")
for field in fields:
    try:
        res = requests.get(metadata_url + field, timeout=1)
        print(f"{field}: {res.text}")
    except Exception as e:
        print(f"{field}: ERROR - {e}")
    