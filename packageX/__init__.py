import requests


def get_own_version_from_package():
    GITHUB_API_URL = "https://api.github.com/repos/Franreno/tag-testing-2/releases/latest"
    response = requests.get(GITHUB_API_URL)
    response.raise_for_status()

    data = response.json()
    version = data.get("tag_name", "").strip()

    return version


def version_check():
    URL = "http://localhost:3000/version-check"
    response = requests.get(URL)
    server_version = response.text.strip()

    PACKAGE_VERSION = get_own_version_from_package()

    print(f"Client Version: {PACKAGE_VERSION}")
    print(f"Server Version: {server_version}")

    if server_version != PACKAGE_VERSION:
        raise ValueError(
            "Client version does not match with the server version. Please update the client!"
        )
    else:
        print("Version check successful!")


# Test the function
version_check()

from .hello import GetHelloWorld
