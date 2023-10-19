import boto3
import requests

def get_instance_region():
    instance_identity_url = "http://169.254.169.254/latest/dynamic/instance-identity/document"
    session = requests.Session()
    r = requests.get(instance_identity_url)
    response_json = r.json()
    region = response_json.get("region")
    return(region)

client = boto3.client('ssm', get_instance_region())

master_username = client.get_parameter(
    Name='master_username',
    WithDecryption=True
)["Parameter"]["Value"]

db_password = client.get_parameter(
    Name='db_password',
    WithDecryption=True
)["Parameter"]["Value"]

endpoint = client.get_parameter(
    Name='endpoint',
    WithDecryption=True
)["Parameter"]["Value"]

db_instance_name = client.get_parameter(
    Name='db_instance_name',
    WithDecryption=True
)["Parameter"]["Value"]


if __name__ == "__main__":
    print(master_username, db_password, endpoint, db_instance_name)