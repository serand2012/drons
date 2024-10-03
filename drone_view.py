from drone_model import DroneModel


class DroneView:
    """
    Класс DroneView отвечает за визуализацию данных о состоянии БПЛА.
    """

    def display_status(self, model: DroneModel):

        if model is None:
            print("Дрон отсутствует в списке зарегистрированных дронов")
            return
        """
        Выводит на экран информацию о текущем состоянии БПЛА.
        :param model: Экземпляр DroneModel с данными о состоянии
        """
        print(f"Altitude: {model.get_altitude()} meters\nSpeed: {model.get_speed()} m/s\n"
              f"Position: {model.get_position()}\nBattery: {model.get_battery_level()}%")

    def alert(self, message: str):
        """
        Выводит предупреждающее сообщение.
        :param message: Текст предупреждения
        """
        print(f"ALERT: {message}")
