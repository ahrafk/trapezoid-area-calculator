from django.db import models

# Create your models here.
class TrapezoidCalculation(models.Model):
    base1 = models.FloatField()
    base2 = models.FloatField()
    height = models.FloatField()
    area = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.base1}, {self.base2}, {self.height} → {self.area}"
