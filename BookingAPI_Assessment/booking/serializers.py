from rest_framework import serializers
from .models import fitness_studio,booking_requests

#creating serializer for fitness_studio model
class fitness_studioSerializer(serializers.ModelSerializer):
    class Meta:
        model = fitness_studio
        fields = ['id','name', 'date_time', 'instructor', 'available_slots' ]

##creating serializer for booking_requests model
class booking_requestSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking_requests
        fields = ['id','fitness_class', 'client_name', 'client_email']

# validating, if slots are available
    def validate(self, data):
        fitness_class = data['fitness_class']
        if fitness_class.available_slots <= 0:
            raise serializers.ValidationError(
            f"No slots available for '{fitness_class.name}'"
        )
        return data

#reducing slots upon available booking
    def create(self, validated_data):
        fitness_class = validated_data['fitness_class']
        fitness_class.available_slots -= 1
        fitness_class.save()

        return booking_requests.objects.create(**validated_data)