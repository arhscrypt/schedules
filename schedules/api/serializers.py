from rest_framework import serializers
from .models import mSchadules

class ser_schedule (serializers.ModelSerializer):
    class Meta:
        model = mSchadules
        fields = ('schedule_name','schedule_time')