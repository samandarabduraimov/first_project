from django.db import models

class SerialNumber(models.Model):
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.code
class SerialEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    serial_number = models.ForeignKey(SerialNumber, on_delete=models.CASCADE)
    event_time = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.serial_number.code} - {self.event_time}"