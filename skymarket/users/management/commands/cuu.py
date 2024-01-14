from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='shafiyev29@yandex.ru',
            username='shafiyev09',
            first_name='shafiyev',
            last_name='shafiyev',
            phone=None,
            role='user',
            is_active=True
        )

        user.set_password('12345qwerty')
        user.save()
