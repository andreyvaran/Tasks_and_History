import csv
import os.path
{{2,1,1,-1},{1,2,1,-1},{-3,-3,-2,3},{-1,-1,-1,2}}

class CarBase():
    required = []

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = self.validate_input(brand)
        self.photo_file_name = self.validate_photo_filename(photo_file_name)
        self.carrying = float(self.validate_input(carrying))

    def validate_input(self, value):
        if value == '':
            raise ValueError
        return value

    def validate_photo_filename(self, filename):
        for ext in ('.jpg', '.jpeg', '.png', '.gif'):
            if filename.endswith(ext):
                return filename
        raise ValueError

    def get_photo_file_ext(self):
        _, ext = os.path.splitext(self.photo_file_name)
        return ext

    @classmethod
    def create_from_dict(cls, data):
        parameters = [data[parameter] for parameter in cls.required]
        return cls(*parameters)


class Car(CarBase):
    car_type = "car"
    required = ['brand', 'photo_file_name', 'carrying', 'passenger_seats_count']

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(self.validate_input(passenger_seats_count))


class Truck(CarBase):
    car_type = "truck"
    required = ['brand', 'photo_file_name', 'carrying', 'body_whl']

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_length, self.body_width, self.body_height = self.parse_whl(body_whl)

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height

    def parse_whl(self, body_whl):
        try:
            length, width, height = (float(c) for c in body_whl.split("x", 2))
        except Exception:
            length, width, height = 0.0, 0.0, 0.0
        return length, width, height


class SpecMachine(CarBase):
    car_type = "spec_machine"
    required = ['brand', 'photo_file_name', 'carrying', 'extra']

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = self.validate_input(extra)


def get_car_list(csv_filename):
    car_types = {'car': Car, 'spec_machine': SpecMachine, 'truck': Truck}
    csv.register_dialect('cars', delimiter=';')
    car_list = []

    with open(csv_filename, 'r') as file:
        reader = csv.DictReader(file, dialect='cars')
        for row in reader:
            try:
                car_class = car_types[row['car_type']]
                car_list.append(car_class.create_from_dict(row))
            except Exception:
                pass

    return car_list