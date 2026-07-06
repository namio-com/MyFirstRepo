import os
os.environ["REQUESTS_CA_BUNDLE"] = r"C:\Users\10264051\tools\Cisco_Secure_Access_Root_CA.pem"
os.environ["SSL_CERT_FILE"] = r"C:\Users\10264051\tools\Cisco_Secure_Access_Root_CA.pem"
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

endpoint = "https://namio-m-0298-resource.services.ai.azure.com/openai/v1"
deployment_name = "gpt-4o-mini"
token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://ai.azure.com/.default")

client = OpenAI(
    base_url=endpoint,
    api_key=token_provider
)

response = client.responses.create(
    model=deployment_name,
    input="What is the capital of France?",
)

print(f"answer: {response.output[0]}")