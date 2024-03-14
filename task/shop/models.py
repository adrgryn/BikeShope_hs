from django.db import models


class Frame(models.Model):
    color = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.color}"


class Seat(models.Model):
    color = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.color}"


class Tire(models.Model):
    type = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.type}"


class Basket(models.Model):
    quantity = models.IntegerField(default=0)


class Bike(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    has_basket = models.BooleanField()
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    tire = models.ForeignKey(Tire, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    PENDING = 'P'
    READY = "R"
    status_choice = [
        (PENDING, "pending"),
        (READY, "ready")
    ]
    status = models.CharField(max_length=1, choices=status_choice, default=PENDING)

