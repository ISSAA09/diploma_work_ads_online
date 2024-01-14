from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='iska29@inbox.ru',
            username='issaa09',
            first_name='ismail',
            last_name='shafiyev',
            phone=None,
            role='admin',
            is_active=True,

        )
        user.set_password('12345qwerty')
        user.save()
