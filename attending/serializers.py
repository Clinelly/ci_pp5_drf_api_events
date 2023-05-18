from django.db import IntegrityError
from rest_framework import serializers
from attending.models import Attending


class AttendingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Attending model
    The create method handles the unique constraint on 'owner' and 'event'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Attending
        fields = ['id', 'created_at', 'owner', 'event']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'You cannot attend the same event more than once.'
            })
