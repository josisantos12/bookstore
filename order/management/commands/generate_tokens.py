from django.core.management.base import BaseCommand
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Gera tokens para todos os usuários'

    def handle(self, *args, **kwargs):
        for user in User.objects.all():
            Token.objects.get_or_create(user=user)
        self.stdout.write(self.style.SUCCESS('Tokens gerados com sucesso!'))