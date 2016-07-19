from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class User(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=15)
	email_address = models.EmailField(max_length=75)
	weekly_hours = models.IntegerField()

	def __str__(self):
		return(self.first_name + " " + self.last_name)

class News_Messages(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length = 500)
	content = models.TextField()
	publish_date = models.DateTimeField(
		default = timezone.now,
	)
	def __str__(self):
		return(self.title)

class Shift(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	date = models.DateField(
	)

	SHIFT_AM_6 = "6AM"
	SHIFT_AM_7 = "7AM"
	SHIFT_AM_8 = "8AM"
	SHIFT_AM_9 = "9AM"
	SHIFT_AM_10 = "10AM"
	SHIFT_AM_11 = "11AM"
	SHIFT_PM_12 = "12PM"
	SHIFT_PM_1 = "1PM"
	SHIFT_PM_2 = "2PM"
	SHIFT_PM_3 = "3PM"
	SHIFT_PM_4 = "4PM"
	SHIFT_PM_5 = "5PM"
	SHIFT_PM_6 = "6PM"
	SHIFT_PM_7 = "7PM"
	SHIFT_PM_8 = "8PM"
	SHIFT_PM_9 = "9PM"
	SHIFT_PM_10 = "10PM"
	SHIFT_PM_11 = "11PM"

	TIMES_AVAILABLE = (
		(SHIFT_AM_6, "6 A.M."),
		(SHIFT_AM_7, "7 A.M."),
		(SHIFT_AM_8, "8 A.M."),
		(SHIFT_AM_9, "9 A.M."),
		(SHIFT_AM_10, "10 A.M."),
		(SHIFT_AM_11, "11 A.M."),
		(SHIFT_PM_12, "12 P.M."),
		(SHIFT_PM_1, "1 P.M."),
		(SHIFT_PM_2, "2 P.M."),
		(SHIFT_PM_3, "3 P.M."),
		(SHIFT_PM_4, "4 P.M."),
		(SHIFT_PM_5, "5 P.M."),
		(SHIFT_PM_6, "6 P.M."),
		(SHIFT_PM_7, "7 P.M."),
		(SHIFT_PM_8, "8 P.M."),
		(SHIFT_PM_9, "9 P.M."),
		(SHIFT_PM_10, "10 P.M."),
		(SHIFT_PM_11, "11 P.M."),
	)

	time = models.CharField(
		max_length = 4,
		choices=TIMES_AVAILABLE,
		default= SHIFT_PM_12,
	)

	BOXOFFICE = 'Box Office'
	MAINDESK = 'Main Desk' 
	FITNESSCENTER = "Fitness Center"
	EQUIPMENTCHECKOUT = 'Equipment Checkout'
	LOCATIONS_TO_WORK = (
		(BOXOFFICE, "Box Office"),
		(MAINDESK, "Main Desk"),
		(FITNESSCENTER, "Fitness Center"),
		(EQUIPMENTCHECKOUT, "Equipment Checkout"),
	)

	working_location = models.CharField(
		max_length=20, 
		choices=LOCATIONS_TO_WORK,
		default=MAINDESK,
	)

	PERMANENTSHIFT = 'PS'
	TEMPORARYSHIFT = 'TS'

	SHIFTS_SPECIFICATION =(
		(PERMANENTSHIFT, "Permanent shift"),
		(TEMPORARYSHIFT, "Temporary shift"),
	)

	type_of_shift = models.CharField(
		max_length = 20,
		choices = SHIFTS_SPECIFICATION,
		default = PERMANENTSHIFT,
	)

	release_reason = models.TextField(
		default="Blank")
	
	release_shift_temp = False
	release_shift_perm = False

	

	def __str__(self):
		#figure out what to return
		return(self.user.first_name + " " + self.user.last_name + 
			" " + self.working_location + " " + self.time)
	