from faker import Faker

fake = Faker()

#creates a fake name
name = fake.name()

#creates a fake email
email = fake.email()

#creates a fake phone number
phone_number = fake.phone_number()

print(name + "'s phone number is " + phone_number + ", and their email is " + email)