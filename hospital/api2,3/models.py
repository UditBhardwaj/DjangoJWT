from django.db import models
from multiselectfield import MultiSelectField


repeat_choice = (
		('None', 'None'),
		('Daily', 'Daily'),
		('Weekly', 'Weekly'),
)
RELEVANCE_CHOICES = (
    (1, ('Weekdays only')),
)
MY_CHOICES2 = ((1, 'Mon'),
               (2, 'Tue'),
               (3, 'Wed'),
               (4, 'Thu'),
               (5, 'Fri'),
               (6, 'Sat'),
               (7, 'Sun'),)
shift_choice = (
    ('Morning','Morning'),
)

class Client(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    email = models.EmailField(verbose_name='email', max_length=255,unique=False)
    repeat_type = models.CharField(max_length=50, blank=True, null=True, choices=repeat_choice)
    shift = models.CharField(max_length=50, blank=True, null=True, choices=shift_choice)
    start_time = models.TimeField()
    end_time = models.TimeField()
    my_field = MultiSelectField(choices=MY_CHOICES2,blank=True)
    weekdays_only = models.BooleanField(blank=True,default=False)

    def __str__(self):
        return self.shift

