from datetime import datetime

from rest_framework import serializers

from .models import *


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        del representation['user']
        return representation


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        del representation['user']
        return representation


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        del representation['user']
        return representation

    def validate_section(self, section):
        if section and self.initial_data['user'] != section.user.id:
            raise serializers.ValidationError("wrong section")
        return section

    def validate_status(self, status):
        if status and self.initial_data['user'] != status.user.id:
            raise serializers.ValidationError("wrong status")
        return status

    def validate(self, data):
        start = None
        end = None
        if 'start_datetime' in data:
            start = data['start_datetime']
        elif self.instance:
            start = self.instance.start_datetime
        if 'due_datetime' in data:
            end = data['due_datetime']
        elif self.instance:
            end = self.instance.due_datetime
        if not end:
            return data
        if start > end:
            raise serializers.ValidationError(
                "start_datetime could not be greater than due_datetime")
        return data
