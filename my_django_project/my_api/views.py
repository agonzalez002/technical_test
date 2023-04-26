from datetime import datetime, date

from rest_framework import viewsets
from rest_framework.response import Response

from my_api.models import Person
from my_api.serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """Person view."""
    queryset = Person.objects.all().order_by('lastname')
    serializer_class = PersonSerializer

    def create(self, request):
        """Create new person."""
        data = request.POST
        today = date.today()

        birthday = datetime.strptime(data.get('birthday', False), '%Y-%m-%d')
        if today.year - birthday.year >= 150:
            return Response({'error': 'The person must have under 150 years old'}, status=409)

        Person.objects.create(
            lastname=data.get('lastname'),
            firstname=data.get('firstname'),
            birthday=birthday
            )
        return Response(status=200)


