import requests
from config import API_URL


def login(email, password):

    response = requests.post(
        f"{API_URL}/auth/login",
        json={
            "email": email,
            "password": password
        }
    )

    return response



def signup(username, email, password):

    response = requests.post(
        f"{API_URL}/auth/signup",
        json={
            "username": username,
            "email": email,
            "password": password
        }
    )

    return response



def upload_file(file, token):

    headers = {
        "Authorization": f"Bearer {token}"
    }

    files = {
        "file":(
            file.name,
            file,
            file.type
        )
    }

    return requests.post(
        f"{API_URL}/upload/",
        files=files,
        headers=headers
    )



def get_files(token):

    headers = {
        "Authorization": f"Bearer {token}"
    }

    return requests.get(
        f"{API_URL}/files/",
        headers=headers
    )



def download_file(file_id, token):

    headers={
        "Authorization":f"Bearer {token}"
    }

    return requests.get(
        f"{API_URL}/files/download/{file_id}",
        headers=headers
    )



def get_image(file_id, token):

    headers={
        "Authorization":f"Bearer {token}"
    }

    return requests.get(
        f"{API_URL}/files/image/{file_id}",
        headers=headers
    )