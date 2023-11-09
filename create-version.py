import sys
from google.cloud import secretmanager_v1


def add_secret_version(secret_id: str, payload: str) -> secretmanager_v1.SecretVersion:
    """
    Add a new secret version to the given secret with the provided payload.
    """

    # Import the Secret Manager client library.
    # from google.cloud import secretmanager

    # Create the Secret Manager client.
    client = secretmanager_v1.SecretManagerServiceClient()

    # Build the resource name of the parent secret.
    parent = client.secret_path("th-olr-common-devqa-3beb", secret_id)

    # Convert the string payload into a bytes. This step can be omitted if you
    # pass in bytes instead of a str for the payload argument.
    payload_bytes = payload.encode("UTF-8")

    # Add the secret version.
    response = client.add_secret_version(
        request={
            "parent": parent,
            "payload": {
                "data": payload_bytes,
            },
        }
    )

    # Print the new secret version name.
    print(f"Added secret version: {response.name}")
    return(response)

arguments = sys.argv
add_secret_version(arguments[1], arguments[2])
