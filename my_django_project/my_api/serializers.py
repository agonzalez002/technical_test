from rest_framework import serializers

from my_api.models import Person


class PersonSerializer(serializers.ModelSerializer):
    """Person model serializer."""

    class Meta:
        model = Person
        fields = "__all__"
