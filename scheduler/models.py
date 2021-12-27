from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Schedule(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()

    def __str__(self):

        return f"{self.user.username} Schedule Id ({self.id}) - {self.start_date_time} | to | {self.end_date_time}"

class Reservation(models.Model):

    fullname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    schedule = models.OneToOneField(Schedule, on_delete=models.CASCADE)

    def __str__(self):

        return f"{self.fullname} - {self.email} - Schedule Id ({self.schedule.id})"

