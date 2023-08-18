from django.core.management.base import BaseCommand
from ...models import Post

class Command(BaseCommand):
    help = 'Удаление всех постов'
    requires_migrations_checks = True

    def handle(self, *args, **options):
        self.stdout.write('Хотите удалить все новости? да/нет')
        answer = input()
        if answer == 'да':
            Post.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Посты успешно удалены'))
            return
        self.stdout.write(self.style.ERROR('В удаление отказано'))