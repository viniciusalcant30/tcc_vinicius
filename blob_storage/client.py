from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

def get_blob_client(account_url):
    try:
        default_credential = DefaultAzureCredential()
        
        # Create the BlobServiceClient object
        blob_service_client = BlobServiceClient(account_url, credential=default_credential)
        return blob_service_client

    except Exception as ex:
        print('Exception:')
        print(ex)