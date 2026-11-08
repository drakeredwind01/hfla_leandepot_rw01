import os
import django

# setup django environmet
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hfla_leandepot_rw01.settings')
django.setup()

from model_bakery import baker
from projects.models import Project, Member, Permission

def main():
    print("🚀 Generating lean mock data efficiently...")

    # this one line generates permissions in one go
    # and automatically creates 10 projects, 10 members to link them to!
    permissions = baker.make(Permission, _quantity=10)

    for p in permissions:
        print(f"Generated: {p}")

if __name__ == "__main__":
    main()