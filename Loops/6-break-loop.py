dog_breeds_available_for_adoption = ["French bulldog", "Dalmation", "Shi Tzu", "Poodle", "Collie", "Labrador"]

dog_breed_I_want = "Dalmation"

for dog_breed in dog_breeds_available_for_adoption:
    print(dog_breed)
    if dog_breed == dog_breed_I_want:
        print("They have the dog I want!")
        break