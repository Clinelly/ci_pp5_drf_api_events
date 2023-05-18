from rest_framework import serializers
from .models import Event
from likes.models import Like
from attending.models import Attending


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    attending_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    attending_count = serializers.ReadOnlyField()

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

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, event=obj
            ).first()
            return like.id if like else None
        return None

    def get_attending_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            attending = Attending.objects.filter(
                owner=user, event=obj
            ).first()
            return attending.id if attending else None
        return None

    class Meta:
        model = Event
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'title',
            'description', 'location', 'start_time', 'end_time', 'image',
            'is_owner', 'profile_id', 'profile_image', 'like_id',
            'attending_id', 'likes_count', 'comments_count', 'attending_count'
        ]
