import sys
import os
from google.api_core.client_options import ClientOptions
from google.cloud import firestore
from google.cloud.firestore_v1.base_query import FieldFilter


def quickstart_new_instance():
    #from google.cloud import firestore
    db = firestore.Client(project="my-project-id")
    return db


def quickstart_add_data_one():
    db = firestore.Client()
    doc_ref = db.collection("users").document("alovelace")
    doc_ref.set({"first": "Aa", "last": "Bb", "born": 2000})


def quickstart_add_data_two():
    db = firestore.Client()
    doc_ref = db.collection("users").document("aturing")
    doc_ref.set({"first": "Cc", "middle": "Dd", "last": "Ee", "born": 2001})


def quickstart_get_collection():
    db = firestore.Client()
    users_ref = db.collection("users")
    docs = users_ref.stream()

    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")

def add_new_doc():
    db = firestore.Client()
    new_users_ref = db.collection("data").document()
    

def structure_collection_ref():
    db = firestore.Client()
    users_ref = db.collection("users")
    print(users_ref)

def create_and_build_bundle():
    _setup_bundle()
    from google.cloud import firestore
    from google.cloud.firestore_bundle import FirestoreBundle

    db = firestore.Client()
    bundle = FirestoreBundle("user_updates")

    doc_snapshot = db.collection("users").document("user_ref").get()
    query = db.collection("users")._query()
    bundle_buffer: str = (
        bundle.add_document(doc_snapshot)
        .add_named_query(
            "user_updates-query",
            query,
        )
        .build()
    )

if __name__ == "__main__":
    quickstart_new_instance(
        bucket_name=sys.argv[1], blob_name=sys.argv[2], user_email=sys.argv[3],
    )
