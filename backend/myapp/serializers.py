from django.contrib.auth import get_user_model
from rest_framework import serializers

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'user_type')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Remove the password from the validated_data dictionary
        password = validated_data.pop('password', None)
        # Create the user instance
        instance = self.Meta.model(**validated_data)
        # Check if password is present and set it
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
