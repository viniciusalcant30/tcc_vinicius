import os, uuid
from dotenv import load_dotenv
from blob_storage import client
from tqdm import tqdm

load_dotenv()

ACCOUNT_URL = os.environ.get('ACCOUNT_URL')
CONTAINER = os.environ.get('CONTAINER')

blob_service_client = client.get_blob_client(ACCOUNT_URL)
container_client = blob_service_client.get_container_client(CONTAINER)


def download_blob_storage(local_path, container_client=container_client):
    print("\nListing blobs...")
    # List the blobs in the container
    blob_list = container_client.list_blobs()
    i = 0
    j = 0

    for blob in tqdm(blob_list):
        i+=1
        # print(f"\n{i}: {blob.name} initiating download")
        blob_name = blob.name
        local_file_name = blob_name

        # Download the blob to a local file
        download_file_path = os.path.join(local_path, local_file_name)
        # print("Downloading blob to " + download_file_path)
        try: 
            with open(download_file_path, "wb") as download_file:
                content = container_client.download_blob(blob_name).readall()
                download_file.write(content)
                # print(f'\t{blob_name} download 100%')
        except Exception as ex:
            j = j+i
            print('Exception:')
            print(ex)

    print(f'{i} arquivos baixados com sucesso')
    if j > 0:
        print(f'e {j} erros encontrados')