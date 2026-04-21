from django.core.management.base import BaseCommand

from django.contrib.auth.models import User
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):

        # Delete existing data
        for model in [User, Team, Activity, Leaderboard, Workout]:
            model.objects.all().delete()


        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users (super heroes) and store team as a string attribute
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password'),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='password'),
            User.objects.create_user(username='superman', email='superman@dc.com', password='password'),
        ]
        # Assign team as a string attribute (not ForeignKey)
        users[0].profile_team = 'Marvel'
        users[1].profile_team = 'Marvel'
        users[2].profile_team = 'DC'
        users[3].profile_team = 'DC'
        for user in users:
            user.save()


        # Create Activities
        for user in users:
            Activity.objects.create(user=user, type='run', duration=30)
            Activity.objects.create(user=user, type='cycle', duration=45)

        # Create Workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio for all')
        Workout.objects.create(name='Strength Training', description='Strength for all')

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
