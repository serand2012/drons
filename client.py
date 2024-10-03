import requests

BASE_URL = 'http://127.0.0.1:5000/'


def create_drone(drone_id: str, serial_number: str, model: str, payload: int, battery_level: int, capacity: int):
    data = {
        "id": drone_id,
        "serial_number": serial_number,
        "model": model,
        "payload": payload,
        "battery_level": battery_level,
        "capacity": capacity
    }

    response = requests.post(f"{BASE_URL}drone/registration", json=data)

    if response.status_code == 201 or response.status_code == 200:
        print(f'Статус ответа: {response.status_code} - {response.json()["info"]}')
    elif response.status_code == 400:
        print(f'Статус ответа: {response.status_code} - {response.json()["error"]}')
    else:
        print(f'Статус ответа: {response.status_code}')


def get_status(drone_id: str):
    response = requests.post(f"{BASE_URL}drone/status", json={"id": drone_id})
    if response.status_code == 201 or response.status_code == 200:
        print(f'Статус ответа: {response.status_code} - {response.json()["info"]}')
    elif response.status_code == 400:
        print(f'Статус ответа: {response.status_code} - {response.json()["error"]}')
    else:
        print(f'Статус ответа: {response.status_code}')


def take_off(drone_id: str, altitude: int):
    response = requests.post(f"{BASE_URL}drone/takeoff", json={"id": drone_id, "altitude": altitude})
    if response.status_code == 201 or response.status_code == 200:
        print(f'Статус ответа: {response.status_code} - {response.json()["info"]}')
    elif response.status_code == 400:
        print(f'Статус ответа: {response.status_code} - {response.json()["error"]}')
    else:
        print(f'Статус ответа: {response.status_code}')


if __name__ == '__main__':
    create_drone("007C", "SN43g234", "ModelX", 500, 100, 15000)
    create_drone("007D", "SN43g234", "ModelX", 500, 100, 20000)
    get_status("007C")
    take_off("007C", 2)
