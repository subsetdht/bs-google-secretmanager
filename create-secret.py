from google.cloud import secretmanager_v1


def sample_access_secret_version(secretRef):
    # Create a client
    client = secretmanager_v1.SecretManagerServiceClient()

    # Initialize request argument(s)
    request = secretmanager_v1.AccessSecretVersionRequest(
        # name="th-olr-common-devqa-3beb/det-gha-var-target-environment-dev"
        name=secretRef
    )

    # Make the request
    response = client.access_secret_version(request=request)

    # Handle the response
    print(response)


sample_access_secret_version(
    "projects/th-olr-common-devqa-3beb/secrets/det-gha-var-target-environment-dev/versions/latest"
)
