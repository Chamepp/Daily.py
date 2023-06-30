import random
import string

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_email():
    username = generate_random_string(8)
    domain = generate_random_string(5)
    return f"{username}@{domain}.com"

def generate_random_age(min_age, max_age):
    return random.randint(min_age, max_age)

def generate_test_data(num_records):
    test_data = []
    for _ in range(num_records):
        first_name = generate_random_string(6)
        last_name = generate_random_string(8)
        email = generate_random_email()
        age = generate_random_age(18, 65)

        test_data.append({
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'age': age
        })

    return test_data

# Example usage
num_records = 10
test_data = generate_test_data(num_records)

# Print the generated test data
for record in test_data:
    print(record)

