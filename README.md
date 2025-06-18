# Fitnessbooking_API
Assessment to build simple fitness booking API using Python
In this, cliens can-
  i. view available classes
  ii. book a class
  iii. view bookings by email
Tools used- Django, Djangorestframework(for creating Restful API's), Postman(for Testing)
Created two models- fitness_studio,booking requests
API Endpoints: 1. Get/classes
               2. POST/book
               3. GET/get_bookings/?email=len432@gmail.com
Check if slots are available(validation)
prevent duplicate bookings
Upon successful booking classes, available_slot is decreased by one.
If no slot is available, print 400 with error message
If no email is matched, returns 404
error message for duplicate bookings and missing email in the endpoints also
enabled time-zone aware(IST is UTC+05.30)
  
