from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.FloatField()
    new = models.BooleanField()
    used = models.BooleanField()

class CarCatalog(models.Model):
    cars = models.ManyToManyField(Car)

    def add_car(self, car):
        self.cars.add(car)

    def find_car_by_model_year(self, model, year):
        for car in self.cars.all():
            if car.model.lower() == model.lower() and car.year == year:
                return car
        return None
