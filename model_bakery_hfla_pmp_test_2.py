'''
wow, what a mess. hate it.
lets try to clean this up using faker.
'''

import os
import django
from faker import Faker

# setup django environmet
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import sys
sys.path.append(os.getcwd())
django.setup()

from model_bakery import baker
from projects.models import Permission

faker = Faker()

def main():
    # Adding \n inside the string for a gap after the title
    
    print("📋 Previewing mock data (Not saving to database)...\n")
    print(f"Created: ")
    print(f"project, member, name")
    for _ in range(10):
        p = baker.prepare(
            Permission, 
            project__name=faker.company(),
            member__name=faker.name(), # Added missing comma
            name=faker.job(), 
        )
        # Using f-string with \n to create a gap between results
        print(f"\n{p.project.name}, {p.member.name}, {p.name}")        

if __name__ == "__main__":
    main()