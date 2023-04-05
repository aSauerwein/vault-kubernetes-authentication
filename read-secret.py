from hvac import Client
from hvac.api.auth_methods import Kubernetes
import os
from pathlib import Path
from time import sleep

VAULT_URL = os.environ.get("VAULT_URL", "")
VAULT_VERIFY = os.environ.get("VAULT_VERIFY", True)
if VAULT_VERIFY.lower() in ["false", "no", "0", "off"]:
    VAULT_VERIFY = False
VAULT_ROLE = os.environ.get("VAULT_ROLE", "")
VAULT_MOUNT_POINT = os.environ.get("VAULT_MOUNT_POINT", "kubernetes")
VAULT_SECRET = os.environ.get("VAULT_SECRET", "")

# read token from automounted service account
VAULT_TOKEN = Path("/var/run/secrets/kubernetes.io/serviceaccount/token").read_text()

print(f"""
Connecting to vault with these settings:
url: {VAULT_URL}
verify: {VAULT_VERIFY}
role: {VAULT_ROLE}
mount point: {VAULT_MOUNT_POINT}
secret: {VAULT_SECRET}
""")

# prepare vault client
client = Client(url=VAULT_URL, verify=VAULT_VERIFY)
# login with kubernetes authentication
Kubernetes(client.adapter).login(
    role=VAULT_ROLE, jwt=VAULT_TOKEN, mount_point=VAULT_MOUNT_POINT
)

if client.is_authenticated():
    print("Succesfully Authenticated with vault")
else:
    print("Authentication with vault failed")


# sleep forever
while True:
    sleep(30)