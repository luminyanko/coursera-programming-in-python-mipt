"""
Классы и наследование

В базовом классе CarBase нужно реализовать метод get_photo_file_ext
для получения расширения файла изображения. Расширение файла
можно получить при помощи os.path.splitext.

Для грузового автомобиля необходимо в конструкторе класса
определить атрибуты: body_length, body_width, body_height,
отвечающие соответственно за габариты кузова — длину, ширину и
высоту. Габариты передаются в параметре body_whl (строка,
в которой размеры разделены латинской буквой «x»). Обратите
внимание на то, что характеристики кузова должны быть вещественными
числами и характеристики кузова могут быть не валидными (например,
пустая строка). В таком случае всем атрибутам, отвечающим за габариты
кузова, присваивается значение равное нулю.

Также для класса грузового автомобиля необходимо реализовать метод
get_body_volume, возвращающий объем кузова.

В классе Car должен быть определен атрибут passenger_seats_count
(количество пассажирских мест), а в классе SpecMachine — extra
(дополнительное описание машины).
"""
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.car_type = None
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        self.body_width = 0.0
        self.body_height = 0.0
        self.body_length = 0.0
        self.body_volume = 0.0

        if body_whl:
            self.set_truck_body(body_whl)

    def set_truck_body(self, body_whl):
        try:
            length, width, height = map(float, body_whl.split('x'))
        except ValueError:
            length, width, height = 0.0, 0.0, 0.0

        self.body_length = length
        self.body_width = width
        self.body_height = height
        self.body_volume = length * width * height

    def get_body_volume(self):
        return self.body_volume


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra
