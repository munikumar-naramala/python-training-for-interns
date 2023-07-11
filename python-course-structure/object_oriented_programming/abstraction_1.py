from abc import ABC, abstractmethod


class CarsAbstract(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @property
    def car_name(self):
        return f"{self.brand} {self.model}"

    @abstractmethod
    def get_horses(self):
        pass
        raise NotImplementedError


class CarSpecs(CarsAbstract):
    def __init__(self, brand, model, horses, top_speed, kms, litres):
        super().__init__(brand, model)
        self.horses = horses
        self.top_speed = top_speed
        self.kms = kms
        self.litres = litres

    def get_horses(self):
        return self.horses, self.top_speed

    def get_mileage(self):
        return self.kms / self.litres


if __name__ == '__main__':
    try:
        c1 = CarSpecs('Pagans', 'Zonda R', 800, 350, 100, 10)
    except BaseException as error:
        print('An exception occurred: {}'.format(error))

    print(c1.get_horses())
    print(c1.car_name)
    print(c1.get_mileage())
