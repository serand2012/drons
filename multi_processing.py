import multiprocessing


# Параллельная обработка данных с сенсоров
def process_sensor_data(data):
    """
    Обрабатывает данные с сенсора в параллельном процессе.
    :param data: Данные сенсора
    :return: Обработанные данные
    """
    processed_data = data * 2  # Пример обработки
    return processed_data


if __name__ == '__main__':
    sensor_data = [1, 2, 3, 4, 5]
    pool = multiprocessing.Pool()
    results = pool.map(process_sensor_data, sensor_data)
    print(f"Processed sensor data: {results}")
