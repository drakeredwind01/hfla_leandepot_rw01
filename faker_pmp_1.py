from faker import Faker

fake = Faker()

# show off leandepo efficiency
for _ in range (10):
    print (f"{fake.businesses_ogrn()}, {fake.name()}, {fake.bs()}")