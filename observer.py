from drone_controller import DroneController

# Наблюдатель и сенсор препятствий
class SensorObserver:
    # Базовый класс наблюдателя за данными сенсоров

    def update(self, data):
        # Метод обновления данных сенсора. Должен быть реализован в подклассах.
        raise NotImplementedError("Заглушка. Метод должен быть реализован")


class ObstacleSensor(SensorObserver):
    # Класс ObstacleSensor отвечает за обработку данных о препятствиях и управление БПЛА.

    def __init__(self, controller: DroneController):
        # Инициализация сенсора препятствий.
        self.controller = controller

    def update(self, data):
        """
        Обрабатывает данные о препятствиях и изменяет курс или останавливает БПЛА.
        :param data: Данные сенсора (например, дистанция до препятствия)
        """
        if data['distance'] < 10:
            print("Препятствие слишком близко! Изменение курса...")
            # Простейшая логика изменения курса: смещение на 1 единиц по оси x
            new_position = (self.controller.model.position[0] + 1, self.controller.model.position[1])
            self.controller.change_position(new_position)
        elif data['distance'] < 5:
            print("Опасное расстояние! Остановка БПЛА.")
            self.controller.change_speed(0)  # Остановка
