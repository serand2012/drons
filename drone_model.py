import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class DroneModel:  #Класс DroneModel отвечает за хранение данных о состоянии БПЛА

    def __init__(self, id: str, serial_number: str, model: str, payload: int, battery_level: int, capacity: int):
        self.__id = id  # Уникальный идентификатор дрона
        self.__serial_number = serial_number  # серийный номер
        self.__model = model  # Модель дрона
        self.__payload = payload  # Грузоподъемность в граммах
        self.__altitude = 0  # Высота в метрах
        self.__speed = 0  # Скорость в м/с
        self.__position = (0, 0)  # Координаты на плоскости
        self.__battery_level = battery_level  # Уровень заряда батареи в процентах
        self.__capacity = capacity  # Емкость батареи в мАч

    def update_position(self,
                        new_position: tuple):  # Обновляет координаты БПЛА.:param new_position: Новые координаты (x, y)
        self.__position = new_position

    def update_altitude(self, new_altitude: int):  # Обновляет высоту БПЛА в метрах
        self.__altitude = new_altitude

    def update_speed(self, new_speed: int):  # Обновляет скорость БПЛА в м/с
        self.__speed = new_speed

    def update_battery_level(self, consumption: int):  # Обновляет уровень заряда батареи в %
        self.__battery_level -= consumption

    def get_position(self):  # Возвращает данные геопозиции
        return self.__position

    def get_altitude(self):  # Возвращает текущию высоту в метрах
        return self.__altitude

    def get_speed(self):  # Возвращает текущию скорость в м/с
        return self.__speed

    def get_battery_level(self):  # Возвращает текущий заряд батареи
        return self.__battery_level

    def get_id(self):
        return self.__id

    def get_status(self):
        return {
            "id": self.__id,
        "serial_number": self.__serial_number,
        "model": self.__model,
        "payload": self.__payload,
        "altitude": self.__altitude,
        "speed": self.__speed,
        "position": self.__position,
        "battery_level": self.__battery_level,
        "capacity": self.__capacity
        }



if __name__ == '__main__':
    drone = DroneModel("007C", "SN43g234", "ModelX", 500, 100, 15000)
    logging.info(f'{drone}')
