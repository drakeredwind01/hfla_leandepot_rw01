import os
import django
import csv
import pathlib
import random # For picking from your lists
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import sys
sys.path.append(os.getcwd())
django.setup()

from model_bakery import baker
from projects.models import Project, Member, Permission

faker = Faker()

def main():
    # 1. Setup the folder
    output_dir = pathlib.Path("data")
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = output_dir / "hfla_mock_data.csv"

    # 2. Define our specific constraints
    PERM_TYPES = ['admin', 'view_only', 'editor']

    print(f"🚀 Creating 3 Projects and 10 Members...")
    
    # Pre-create our pools
    # We use .prepare so we don't hit the DB, but we could use .make
    projects = baker.prepare(Project, _quantity=3, name=lambda: f"{faker.company().title()}")
    members = baker.prepare(Member, _quantity=20, name=lambda: faker.name())

    print(f"📊 Generating 15 Permission relationships and saving to {filename}...\n")
    print("Project, Member, Permission")

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Project", "Member", "Permission"])

        # 3. Create the junction data
        for _ in range(20):
            # We pick a random project and member from our pre-made lists
            p = baker.prepare(
                Permission,
                project=random.choice(projects),
                member=random.choice(members),
                name=random.choice(PERM_TYPES)
            )
            
            output = f"{p.project.name}, {p.member.name}, {p.name}"
            print(output)
            writer.writerow([p.project.name, p.member.name, p.name])

    print(f"\n✅ Done! Now you'll see overlapping projects and specific roles.")

if __name__ == "__main__":
    main()

# uv run python manage.py runserver
# use uv run manage.py import_permissions to, well, 
# import permissions.