from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    new = models.BooleanField(default=True)
    image = models.ImageField(upload_to='car_images', null=True, blank=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

class CarCatalog(models.Model):
    cars = models.ManyToManyField(Car)

    def add_car(self, car):
        self.cars.add(car)

    def find_car_by_model_year(self, model, year):
        for car in self.cars.all():
            if car.model.lower() == model.lower() and car.year == year:
                return car
        return None
