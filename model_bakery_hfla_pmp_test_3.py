
'''
this is beutiful.
but, it's not what hfla needs.
it needs fewer projects and permissions, and more members.
'''


import os
import django
import csv
import pathlib  # NEW: For lean folder management
from faker import Faker

# setup django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import sys
sys.path.append(os.getcwd())
django.setup()

from model_bakery import baker
from projects.models import Permission

faker = Faker() # hate caps i need to use.

def main():
    filename = "hfla_mock_data.csv"
    output_dir = pathlib.Path("data")
    
    # Create the 'data' folder if it doesn't exist. 
    # parents=True means it creates any middle folders needed.
    # exist_ok=True means it won't crash if the folder is already there.
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"🚀 📋 Previewing mock data and saving to {output_dir}/{filename}...\n")

    # 'w' to write and newline='' to prevent extra blank rows in Windows/Excel
    with open(output_dir / filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # 1. Write the header
        writer.writerow(["Project", "Member", "Permission"])

        # 2. Generate and write the rows
        for _ in range(10):
            p = baker.prepare(
                Permission, 
                project__name=faker.company(),
                member__name=faker.name(),
                name=faker.job(), 
            )
            # ensuring clearn output.
            print(f"{p.project.name}, {p.member.name}, {p.name}")

            # Write directly to the CSV file
            writer.writerow([p.project.name, p.member.name, p.name])

    # don't use cat for this. -t = table, -s = separator
    print(f"\n✅ Success! You can now run: column -t -s, data/{filename}")

if __name__ == "__main__":
    main()