import csv
import os
from django.core.management.base import BaseCommand
from projects.models import Project, Member, Permission

class Command(BaseCommand):
    help = 'Imports projects, members, and permissions from a CSV file'

    def handle(self, *args, **options):
        # Path to your CSV
        file_path = os.path.join('data', 'hfla_mock_data.csv')

        if not os.path.exists(file_path):
            self.stderr.write(f"File not found at {file_path}")
            return

        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            count = 0

            for row in reader:
                # get_or_create returns a tuple: (object, created_boolean)
                # We only care about the object, so we use _ for the second part.
                project, _ = Project.objects.get_or_create(name=row['Project'])
                member, _ = Member.objects.get_or_create(name=row['Member'])

                # Create the permission
                # This will respect your unique_together Meta constraint
                try:
                    Permission.objects.get_or_create(
                        project=project,
                        member=member,
                        name=row['Permission']
                    )
                    count += 1
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f"Skipped duplicate: {row['Member']} on {row['Project']}"))

        self.stdout.write(self.style.SUCCESS(f"Successfully imported {count} records!"))