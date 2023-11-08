import sys
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
    return response


arguments = sys.argv
if arguments[1].find("/") > 0:
    secretName = arguments[1]
else:
    secretName = (
        "projects/th-olr-common-devqa-3beb/secrets/" + arguments[1] + "/versions/latest"
    )

print("Accessing secret: " + secretName)
secretPayload = sample_access_secret_version(secretName)
secretValue = secretPayload.payload.data.decode("utf-8")
print("the secret value is: " + secretValue)
