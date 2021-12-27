import graphene
from graphql_auth.schema import UserQuery, MeQuery
from graphql_jwt.decorators import login_required
from scheduler.models import Schedule, Reservation
from scheduler.mutations import *




class Query(UserQuery, MeQuery, graphene.ObjectType):

    my_schedules = graphene.List(ScheduleType)
    user_schedules = graphene.List(ScheduleType, user_id=graphene.Int())

    @login_required
    def resolve_my_schedules(self, info):
        data = Schedule.objects.filter(user_id=info.context.user.id)
        return data

    def resolve_user_schedules(self, info, user_id):
        data = Schedule.objects.filter(user_id=user_id)
        return data

class Mutation(AuthMutation, graphene.ObjectType):

    create_schedule = CreateSchedule.Field()
    update_schedule = UpdateSchedule.Field()
    delete_schedule = DeleteSchedule.Field()
    create_reservation = CreateReservation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)