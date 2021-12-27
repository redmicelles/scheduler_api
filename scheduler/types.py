from graphene_django import DjangoObjectType
from scheduler.models import Schedule, Reservation
from django.contrib.auth import get_user_model

class UserType(DjangoObjectType):

    class Meta:

        model = get_user_model()
        fields = "__all__"

class ScheduleType(DjangoObjectType):

    class Meta:

        model = Schedule
        fields = "__all__"

class ReservationType(DjangoObjectType):

    class Meta:

        model = Reservation
        fields = "__all__"