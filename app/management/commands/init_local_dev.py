from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

ADMIN_ID = "admin"
ADMIN_PASSWORD = "admin"

class Command(BaseCommand):
    init_start_message = "Initialisation du projet pour un environnement local"
    database_delete_message = "Suppression du jeu de données existant..."
    superuser_create_message = "Création d'un super utilisateur..."
    init_end_message = "Initialisation terminée !"

    def handle(self, *args, **options):

        self.stdout.write(self.style.MIGRATE_HEADING(self.init_start_message))

        self.stdout.write(self.style.WARNING(self.database_delete_message))
        User.objects.all().delete()

        self.stdout.write(self.style.MIGRATE_HEADING(self.superuser_create_message))
        User.objects.create_superuser(ADMIN_ID, "admin@example.com", ADMIN_PASSWORD)

        self.stdout.write(self.style.SUCCESS(self.init_end_message))
