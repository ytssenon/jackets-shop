from django.db import models


class Jacket(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='image/')
    section = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Jacket"
        verbose_name_plural = "Jackets"

    def __str__(self):
        return self.name


class Cart(models.Model):
    jacket = models.ForeignKey(Jacket, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.quantity * self.jacket.price
