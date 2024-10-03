from drone_model import DroneModel
from drone_view import DroneView


class DroneController:  #Класс DroneController отвечает за управление логикой работы БПЛА

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(DroneController, cls).__new__(cls)
            cls.__status_drones = list()
        return cls.__instance

    def get_instance(self):
        return self.__instance

    def __init__(self, view: DroneView, model: DroneModel = None):
        """
        Инициализация контроллера.
        :param model: Экземпляр DroneModel
        :param view: Экземпляр DroneView
        """
        self.__model = model
        self.__view = view

    def set_new_model(self, model: DroneModel):
        self.__model = model

    def change_position(self, new_position):
        """
        Обновляет координаты БПЛА.
        :param new_position: Новые координаты (x, y)
        """
        self.__model.update_position(new_position)
        self.__view.display_status(self.__model)

    def change_altitude(self, new_altitude):
        """
        Обновляет высоту БПЛА.
        :param new_altitude: Новая высота
        """
        self.__model.update_altitude(new_altitude)
        self.__view.display_status(self.__model)

    def change_speed(self, new_speed):
        """
        Обновляет скорость БПЛА.
        :param new_speed: Новая скорость
        """
        self.__model.update_speed(new_speed)
        self.__view.display_status(self.__model)

    def monitor_battery(self):  #Проверяет уровень заряда батареи и выполняет возвращение на базу при низком заряде

        if self.__model.get_battery_level() < 20:
            self.__view.alert("Low battery! Returning to base.")
            self.return_to_base()

    def return_to_base(self):  #Возвращает БПЛА на базу (в начальную точку)

        self.__model.update_position((0, 0))
        self.__model.update_altitude(0)
        self.__model.update_speed(0)
        self.__view.display_status(self.__model)
        self.__view.alert("Drone has returned to base.")

    def get_status(self): #Получение статуса дрона
        return self.__model.get_status()


if __name__ == '__main__':
    drone_model = DroneModel("01", "0123BX", "X_Model", 1500, 100, 15000)
    drone_view = DroneView()
    drone_view.display_status(drone_model)

    drone_model.update_speed(10)
    drone_view.display_status(drone_model)

    #drone_controller = DroneController(drone_model, drone_view)
    #drone_controller.return_to_base()
