import unittest
from drone_controller import DroneModel, DroneView, DroneController

# Юнит-тесты

class TestDroneNavigation(unittest.TestCase):  #Класс TestDroneNavigation тестирует основные функции управления БПЛА.

    def test_update_position(self):  #Тестирует обновление позиции БПЛА.

        drone_model = DroneModel()
        controller = DroneController(drone_model, DroneView())
        controller.change_position((10, 20))
        self.assertEqual(drone_model.position, (10, 20))

    def test_battery_monitoring(self):  #Тестирует мониторинг уровня заряда батареи и возвращение на базу.

        drone_model = DroneModel()
        drone_model.update_battery_level(85)  # Понижаем заряд батареи
        controller = DroneController(drone_model, DroneView())
        controller.monitor_battery()
        self.assertEqual(drone_model.position, (0, 0))  # Дрон должен вернуться на базу


if __name__ == '__main__':
    unittest.main()
