from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size too large. Must be 2MB or less.'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image too wide. Must be 4096px wide or less. '
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image too tall. Must be 4096px tall or less. '
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Event
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'title',
            'description', 'location', 'start_time', 'end_time', 'image',
            'is_owner',
        ]
