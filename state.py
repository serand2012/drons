#from drone_model import DroneModel
#from drone_view import DroneView
from drone_controller import DroneModel, DroneView, DroneController

# Состояния полета
class DroneState:  # Базовый класс для различных состояний полета.

    def handle(self, drone: DroneModel):
        #Метод обработки состояния. Должен быть реализован в подклассах.
        raise NotImplementedError("Метод handle должен быть реализован")


class TakeoffState(DroneState):  # Класс TakeoffState отвечает за состояние взлета БПЛА.
    def handle(self, drone: DroneModel):
        # Реализует логику взлета БПЛА.
        # :param drone: Экземпляр StatefulDrone
        print("Взлет...")
        drone.update_altitude(10)


class LandingState(DroneState):  # Класс LandingState отвечает за состояние посадки БПЛА.

    def handle(self, drone: DroneModel):
        # Реализует логику посадки БПЛА.
        # :param drone: Экземпляр StatefulDrone
        print("Посадка...")
        drone.update_altitude(0)
        drone.update_speed(0)


# Дрон с поддержкой состояний
class StatefulDrone:  #  Класс StatefulDrone управляет состояниями и действиями БПЛА.

    def __init__(self, state: DroneState, model: DroneModel, view: DroneView):
        # Инициализация дрона с состояниями.
        # :param state: Начальное состояние полета
        # :param model: Экземпляр DroneModel
        # :param view: Экземпляр DroneView
        self.state = state
        self.model = model
        self.view = view

    def change_state(self, state: DroneState):
        # Изменяет текущее состояние БПЛА.
        # :param state: Новое состояние полета
        self.state = state

    def perform_action(self):
        # Выполняет действие в соответствии с текущим состоянием БПЛА.
        self.state.handle(self)
        self.view.display_status(self.model)
