from django.urls import path
from .views import get_classes,book_fitness_class,booking_list_by_email

urlpatterns = [ path ('classes/',get_classes, name='get_classes' ),
                path('book/', book_fitness_class, name='book-class'),
                path('get_bookings/',booking_list_by_email, name='booking-list-by-email')
               ]