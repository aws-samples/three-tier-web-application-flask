import boto3
import requests

client = boto3.client('ssm')

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
