from django.db import models

# Create your models here.
# Returns a list of all upcoming fitness classes (name, date/time, instructor, available slots)
#creating model named fitmess_studio

class fitness_studio(models.Model):
    name = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    instructor = models.CharField(max_length=200)
    available_slots = models.PositiveIntegerField()

    def __str__(self):
        return self.name

#creating a model named booking to accept the booking requests

class booking_requests(models.Model):
    fitness_class = models.ForeignKey(fitness_studio,on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)# automatically ensures CharField and EmailField are not empty
    client_email = models.EmailField()

    class Meta:
        unique_together = ('fitness_class', 'client_email') #prevents duplication,cannot book same email id for same fitness class
        


    def __str__(self):
        return self.client_name
