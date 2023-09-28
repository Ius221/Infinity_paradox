from django.db import models
from . import db_connect	#import database connection variables to models

# Create your models here.

hotel_staff = db_connect.admin_collec		#Collection of staff
hotel_customer = db_connect.customer_collec	#Collection of customer