# if __name__ == "__main__":
#     print("Hello world")

import sys
from google.cloud import storage
from google.cloud import storage

storage_client = storage.Client()

bucket_name = "my-new-bucket"

bucket = storage_client.create_bucket(bucket_name)

def add_blob_owner(bucket_name, blob_name, user_email):
    """Adds a user as an owner on the given blob."""
    bucket_name = "demo-bucket-name"
    blob_name = "demo-object-name"
    user_email = "ayatimaitra@gmail.com"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    blob.acl.reload()

    blob.acl.user(user_email).grant_owner()
    blob.acl.save()

    print(
        "Added user {} as an owner on blob {} in bucket {}.".format(
            user_email, blob_name, bucket_name
        )
    )


def write_read(bucket_name, blob_name):
    """Write and read a blob from GCS using file-like IO"""
    bucket_name = "demo-bucket-name"

    blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    with blob.open("w") as f:
        f.write("Testing")

    with blob.open("r") as f:
        print(f.read())


if __name__ == "__main__":
    add_blob_owner(
        bucket_name=sys.argv[1], blob_name=sys.argv[2], user_email=sys.argv[3],
    )
