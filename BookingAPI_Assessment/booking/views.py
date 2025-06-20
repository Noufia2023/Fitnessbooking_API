from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import fitness_studio,booking_requests
from .serializers import fitness_studioSerializer,booking_requestSerializer

#to return the list of all fitness classes
@api_view(['GET'])
def get_classes(request):
    classes = fitness_studio.objects.all()
    serializer = fitness_studioSerializer(classes, many=True)
    return Response(serializer.data)

#to accept a booking request
@api_view(['POST'])
def book_fitness_class(request):
    serializer = booking_requestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#to return bookings made by specific email d
@api_view(['GET'])
def booking_list_by_email(request):
    email = request.query_params.get('email')
    #if we didn't give email in the endpoint, it should report error
    if not email:
        return Response({"error": "Email query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
    
    bookings = booking_requests.objects.filter(client_email=email)

    if not bookings.exists():
        return Response(
            {"error: No bookings found for this email"},
            status=status.HTTP_404_NOT_FOUND
        ) 
    
    
    
    serializer = booking_requestSerializer(bookings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
