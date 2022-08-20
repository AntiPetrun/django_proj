from rest_framework import serializers
from schedule.models import Classroom


class ClassroomSerializer(serializers.ModelSerializer):
    """Список курсов"""
    class Meta:

        model = Classroom
        fields = '__all__'
