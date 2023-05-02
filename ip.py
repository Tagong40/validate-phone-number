import requests
import socket
from fastapi import HTTPException

import requests


def get_ip(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

    if (response.get('error')):
        raise HTTPException(status_code=404, detail="Invalid ip address!!")

    return response
