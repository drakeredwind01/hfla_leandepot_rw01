'''
wow, what a mess. hate it.
lets try to clean this up using faker.
'''

import os
import django

# setup django environmet
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import sys
sys.path.append(os.getcwd())
django.setup()

from model_bakery import baker
from projects.models import Permission

def main():
    print("📋 Previewing mock data (Not saving to database)...")

    # Change .make to .prepare for a dry run
    # Note: Because it's not saving to the DB, it won't have IDs yet!
    review_permissions = baker.prepare(Permission, _quantity=10)

    for p in review_permissions:
        print(f"")

if __name__ == "__main__":
    main()