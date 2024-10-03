from flask import Flask, request, jsonify
from drone_controller import DroneModel, DroneView, DroneController
from state import *

#from drone_controller import DroneController
#from drone_model import DroneModel
#from drone_view import DroneView


app = Flask(__name__)

# Создание экземпляров модели, представления и контроллера
# drone_model: DroneModel = DroneModel()
drone_view: DroneView = DroneView()
drone_controller: DroneController = DroneController(drone_view)
drone_list: list = []
drone_state = DroneState()


def check_drone(data):
    drone_model = None
    for index in range(len(drone_list)):
        if drone_list[index].get_id() == data.get('id'):
            drone_model = drone_list[index]
            drone_controller.set_new_model(drone_model)
            return drone_model
    else:
        return drone_model


# API для управления дроном

@app.route('/drone/status', methods=['GET', 'POST'])
def get_status():
    data = request.get_json()
    drone_model = check_drone(data)
    if drone_model is not None:
        drone_view.display_status(drone_model)
        return jsonify({"info":
                            f"\nAltitude: {drone_controller.get_status().get('altitude')} meters\n"
                            f"Speed: {drone_controller.get_status().get('speed')} m/s\n"
                            f"Position: {drone_controller.get_status().get('position')}\n"
                            f"Battery: {drone_controller.get_status().get('battery_level')}%"}), 200

    return jsonify({"error": f'Дрон с номером id: {data.get('id')} не найден'}), 400


@app.route('/drone/registration', methods=['POST'])
def registration_drone():
    data = request.get_json()
    is_drone = False
    for index in range(len(drone_list)):
        if drone_list[index].get_id() == data.get('id'):
            is_drone = True
            return jsonify({"error": f'Дрон с номером id: {data.get('id')} не уникален'}), 400

    if is_drone is not True:
        drone = DroneModel(data.get('id'), data.get('serial_number'), data.get('model'), data.get('payload'),
                           data.get('battery_level'), data.get('capacity'))
        drone_list.append(drone)
        return jsonify({"info": f'Дрон с номером id: {data.get('id')} добавлен в базу'}), 200


@app.route('/drone/takeoff', methods=['POST'])
def drone_take_off():
    data = request.get_json()
    drone_model = check_drone(data)
    if drone_model is not None:
        takeoff_state = TakeoffState()
        takeoff_state.handle(drone_model)
        _ = drone_controller.get_status().get('altitude')
        return jsonify({"info": f"Altitude: {drone_controller.get_status().get('altitude')}"}), 200
    return jsonify({"error": f'Дрон с номером id: {data.get('id')} не найден'}), 400


@app.route('/drone/position', methods=['POST'])
def update_position():
    data = request.get_json()
    new_position = data.get('position', (0, 0))
    drone_model = check_drone(data)
    if drone_model is not None:
        drone_controller.change_position(new_position)
        return jsonify({"info": f"Position: {drone_controller.get_status().get('position')}"}), 200
    return jsonify({"error": f'Дрон с номером id: {data.get('id')} не найден'}), 400


@app.route('/drone/altitude', methods=['POST'])
def update_altitude():
    data = request.get_json()
    new_altitude = data.get('altitude', 0)
    drone_model = check_drone(data)
    if drone_model is not None:
        drone_controller.change_altitude(new_altitude)
        return jsonify({"info": f"Altitude: {drone_controller.get_status().get('altitude')} meters\n"}), 200
    return jsonify({"error": f'Дрон с номером id: {data.get('id')} не найден'}), 400


@app.route('/drone/speed', methods=['POST'])
def update_speed():
    data = request.get_json()
    new_speed = data.get('speed', 0)
    drone_model = check_drone(data)
    if drone_model is not None:
        drone_controller.change_speed(new_speed)
        return jsonify({"info": f"Speed: {drone_controller.get_status().get('speed')} m/s"}), 200
    return jsonify({"error": f'Дрон с номером id: {data.get('id')} не найден'}), 400


@app.route('/drone/battery', methods=['GET', 'POST'])
def check_battery():
    data = request.get_json()
    drone_model = check_drone(data)
    if drone_model is not None:
        drone_controller.monitor_battery()
        return jsonify({"info": f"Altitude: {drone_controller.get_status().get('battery_level')} %"}), 200
    return jsonify({"error": f'Дрон с номером id: {data.get('id')} не найден'}), 400


@app.route('/drone/return_to_base', methods=['POST'])
def return_to_base():
    data = request.get_json()
    drone_model = check_drone(data)
    if drone_model is not None:
        drone_controller.return_to_base()
        return jsonify({"info": f"Дрон возвращается на базу"}), 200
    return jsonify({"error": f'Дрон с номером id: {data.get('id')} не найден'}), 400


if __name__ == '__main__':
    app.run(debug=False)
